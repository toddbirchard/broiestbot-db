# broiestbot-db

![Python](https://img.shields.io/badge/Python-^3.12-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-^3.0.3-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Dash](https://img.shields.io/badge/Dash-^2.18.2-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-^3.1.1-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/broiestbot-db.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/toddbirchard/broiestbot-db/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/broiestbot-db.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/toddbirchard/broiestbot-db/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/broiestbot-db.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/toddbirchard/broiestbot-db/network)

Lightweight Python GUI for exploring commands available to Chatango chatbot, [broiestbot](https://github.com/toddbirchard/broiestbot).

UI is branded version of [pythonmyadmin](https://github.com/toddbirchard/pythonmyadmin)

## Getting Started

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

Ensure your **.env** configuration is included in a **.gitignore** file before adding or committing secrets by accident.

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_DEBUG`: The environment to run your app in (either `development` or `production`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database.

⚠️*Never to commit secrets saved in **.env** files to Github.*

### Start Locally

Get up and running with `make run`:

```shell
$ git clone https://github.com/toddbirchard/broiestbot-db.git
$ cd broiestbot-db
$ make run
```
