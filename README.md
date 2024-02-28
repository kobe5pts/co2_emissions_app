# CO2 Emissions Search Application

The CO2 Emissions Search Application is a web-based tool that allows users to search 
for CO2 emissions data by country and year. This application is developed using Python 
with the Flask framework for the backend and SQLite for the database.
The datasets were obtained from open source https://zenodo.org/records/10562476 and 
https://www.kaggle.com/datasets/yoannboyere/co2-ghg-emissionsdata?select=co2_emission.csv
A smaller subset (data from year 2000 to 2014) of the original datasets was taken to meet the requirements for this project.

## Features

- Search for CO2 emissions data by specifying a country and a year.
- View search results including additional carbon projection data.
- Handle invalid inputs and database errors with appropriate error messages.
- User-friendly interface with HTML templates and CSS styling.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>

2. Navigate to the project directory:
    cd CO2_emissions

3. Install dependencies:
    pip install -r requirements.txt

4. Run the application:
    pyenv install 3.7.9pyenv 
    local 3.7.9
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install flask
    export FLASK_APP=co2_emissions.py
    export FLASK_ENV=development
    python3 -m flask run -h 0.0.0.0

5. Access the application in a web browser by navigating to http://localhost:5000.

6. Enter a country and a year to search for CO2 emissions data.

7. View search results and additional details.

8. Navigate back to the home page or perform a new search.

PROJECT STRUCTURE:  
CO2_emissions/
│
├── co2_emissions.py               # Flask application file
├── requirements.txt     # Dependencies
│
├── templates/           # HTML templates
│   ├── entity_not_found.html
│   ├── entity_not_provided.html
│   ├── invalid_entity.html
│   ├── search_co2_emissions.html
│   ├── search_results_co2_emissions.html
│   ├── year_not_provided.html
│   └── index.html
│
├── co2_emissions_data.db    # SQLite database file
├── CO2_emissions_data/      # CO2 emissions data directory
│   └── CO2_emissions_data.csv
│
└── test.py              # Unit tests
|__README.md

CONTRIBUTION
Contributions are welcome! 
Feel free to open issues or pull requests for any improvements
or features you'd like to see in the application.