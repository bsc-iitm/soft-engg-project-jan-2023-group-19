# Project Setup Instructions
The project is organized in two main directories:
1. server -- Server API
2. UI -- Client App

## Server setup
Change to server directory like so:

`cd server`

Create a python virtual environment (venv):

`python3 -m venv venv`

Activate the venv"

`. venv/bin/activate`

Install python dependencies using pip3 and requirements.txt

`pip3 install -r requirements.txt`

### Data Load
Sample data in the db/sql/fixtures.sql file needed to be loaded
after the DB backend is configured through the config.yml file.

### Starting the API Server

Start the API server like so:

python3 run.py

The application should start in dev mode at http://localhost:8000

## OpenAPI Spec

The server's API have been speced using OpenAPI 3.0.0 in the 
`openapi.yml` file. It has sample examples to run. The YAML file
can be loaded and tested using swagger.