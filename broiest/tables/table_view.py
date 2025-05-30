"""Dash app for database table view."""

from typing import List, Optional

from dash import Dash, dcc, html
from dash.dash_table import DataTable
from dash.dependencies import Input, Output
from flask import Flask
from pandas import DataFrame

from clients import db

from .layout import app_layout


def create_dash_view(server: Flask) -> Flask:
    """
    Initiate Plotly Dash view.

    :param Flask server: Flask server object.

    :returns: Flask
    """
    external_stylesheets = [
        "/static/dist/css/style.css",
        "https://fonts.googleapis.com/css?family=Lato::300,400,500,700",
        "https://use.fontawesome.com/releases/v5.8.1/css/all.css",
    ]
    dash_app = Dash(
        server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix="/", title="Broiest"
    )

    # Override the underlying HTML template
    dash_app.index_string = app_layout

    # Get DataFrame
    table_df = db.get_table_data()
    dash_table = create_data_table(table_df)

    for column in table_df:
        db.column_dist_chart(table_df, column)

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = create_layout(dash_table, table_df)
    init_callbacks(dash_app, table_df)

    return dash_app.server


def create_layout(dash_table: DataTable, table_df: DataFrame) -> html.Div:
    """
    Create Dash layout for table editor.

    :param DataTable dash_table: Plotly Dash DataTable component.
    :param DataFrame table_df: DataFrame created from SQL table.

    :returns: html.Div
    """
    return html.Div(
        id="database-table-container",
        children=[
            html.Div(
                id="controls",
                children=[
                    dcc.Input(id="search", type="text", placeholder="Search by command"),
                    dcc.Dropdown(
                        id="type-dropdown",
                        options=[{"label": i, "value": i} for i in table_df.type.unique() if i],
                        multi=True,
                        placeholder="Filter by type",
                        maxHeight=400,
                        optionHeight=40,
                        style={"font-size": "1em"},
                    ),
                ],
            ),
            dash_table,
            html.Div(id="callback-container"),
            html.Div(id="container-button-basic", children=[html.Div(id="save-status")]),
        ],
    )


def create_data_table(table_df: DataFrame) -> DataTable:
    """
    Create Plotly DataTable component from Pandas DataFrame.

    :param DataFrame table_df: DataFrame created from SQL table.

    :returns: DataTable
    """
    table = DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in table_df.columns],
        data=table_df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=90000,
        # editable=True,
        cell_selectable=True,
        markdown_options={"link_target": "_blank", "html": True},
        style_cell={
            "font-family": "Lato,sans-serif",
            "font-size": ".85em",
            "background-color": "white",
            "color": "#636a73",
            "text-align": "left",
            "border": "0px solid #ffffff",
            "transition": "all 1s ease-out",
        },
        style_header={"font-size": "1em", "padding": "20px 10px"},
        style_data_conditional=[
            {
                "if": {"state": "selected"},
                "font-family": "Lato,sans-serif",
                "background-color": "#ddf0fa",
                "border": "1px solid #317ed1",
                "color": "#6a94bc !important",
                "text-align": "left",
            },
        ],
    )
    return table


def init_callbacks(dash_app: Dash, table_df: DataFrame):
    """
    Initialize callbacks for user interactions.

    :param Dash dash_app: Plotly Dash application object.
    :param DataFrame table_df: DataFrame created from SQL table.
    """

    @dash_app.callback(
        Output("database-table", "data"),
        [Input("type-dropdown", "value"), Input("search", "value")],
    )
    def filter_by_type(types: Optional[List[str]], search_query: Optional[str]) -> dict:
        """
        Filter data via text search or dropdowns.

        :param Optional[List[str]] types: Category associated with each row in a SQL table.
        :param Optional[str] search_query: Category associated with each row in a SQL table.

        :returns: dict
        """
        dff = table_df

        if types is not None and bool(types):
            dff = dff.loc[table_df["type"].isin(types)]

        if search_query:
            dff = dff.loc[dff["command"].str.contains(search_query.lower().strip())]

        return dff.to_dict("records")
