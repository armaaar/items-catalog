# Items Catalog Project
A catalog website for the "Item Catalog" Project in [Udacity](https://www.udacity.com).

The website's data is publicly available. To add or edit items, authentication is required using a Google account. also a JSON file with all categories and items can be requested through the app API

## Requirements
- Python 2 or Python 3
- Flask 0.10.1
- Flask-WTF 0.14.2
- WTForms 2.1
- OAuth2client 4.1.1
- SQLAlchemy 0.8.4

## How to start the server
- Using your favorite CLI program, `cd` to the project folder.
- "python index.py" to start the server.
- Open the website by going to http://localhost:5000/

## How to access the API
You can access all the websites categories and items using its API just by sending a `GET` request to http://localhost:5000/api/v1/

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
