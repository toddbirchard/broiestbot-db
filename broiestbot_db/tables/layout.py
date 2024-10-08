"""Override base HTML template."""

app_layout = """<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="table-template">
        <header>
            <nav>
                <div class="left-nav">
                    <a href="/"><i class="fas fa-robot"></i>
                        <h1>BROIESTBOT</h1>
                      </a>
                </div>
            </nav>
            </header>
            <main class="layout-container">
                {%app_entry%}
            </main>
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>"""
