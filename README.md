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

## Installation and Running of the App

1. Clone the repository:
   ```bash
   git clone <https://github.com/kobe5pts/co2_emissions_app.git>

2. Navigate to the project directory:
    cd CO2_emissions

3. Install dependencies:
    pip install -r requirements.txt

4. Run the application:
    pyenv install 3.7.9
    pyenv local 3.7.9
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install flask
    export FLASK_APP=co2_emissions.py
    export FLASK_ENV=development
    python3 -m flask run -h 0.0.0.0

5. Access the application in a web browser by navigating to https://carrotalex-denmarkmicro-5000.codio-box.uk/

6. Enter a country and a year to search for CO2 emissions data.

7. View search results and additional details.

8. Navigate back to the home page or perform a new search.

## Render deploymentURL:  
https://co2-emissions-app-m99m.onrender.com

## App maintenance:

To ensure the continued smooth operation and longevity of the application, it's important to follow best practices for maintenance. Here are some key aspects to consider:

*Regular Updates: Keep the application and its dependencies up-to-date. Periodically check for updates to Flask, Python, and any third-party libraries used in the project. Updating to the latest versions can provide performance improvements, security patches, and new features.

*Monitoring: Implement monitoring tools to track the application's performance, uptime, and error rates. Monitoring helps detect issues early and allows for proactive maintenance. 

*Backups: Regularly backup the application data, configuration files, and database. In case of data loss or corruption, having backups ensures that you can restore the application to a previous state without significant downtime.

*Security Audits: Conduct security audits periodically to identify and address potential vulnerabilities. This includes reviewing code for security best practices, implementing proper authentication and authorization mechanisms, and staying informed about common security threats and mitigation strategies.

*Performance Optimization: Continuously optimize the application for performance. This may involve profiling the code to identify bottlenecks, optimizing database queries, caching frequently accessed data, and leveraging asynchronous programming where applicable.

*Documentation: Maintain comprehensive documentation for the application, including installation instructions, configuration settings, API endpoints (if applicable), and troubleshooting guides. Clear and up-to-date documentation makes it easier for developers to understand and contribute to the project.

*Bug Fixes: Address reported bugs and issues promptly. Maintain an issue tracker or bug tracking system to keep track of reported issues and their resolutions. Encourage users to report bugs and provide feedback to help improve the application.

*User Support: Provide timely support to users who encounter problems or have questions about the application. This may include setting up a dedicated support channel, such as a mailing list or forum, and responding to user inquiries in a helpful and courteous manner.

By following these maintenance practices, you can ensure that the Flask application remains robust, secure, and reliable over time. 

## App testing:

Testing is a critical aspect of ensuring the reliability, functionality, and performance of our Flask application. Here's how we approach testing:

*Unit Testing: We utilize unit tests to validate the functionality of individual components, such as functions, methods, and classes, in isolation from the rest of the application. These tests focus on specific units of code and help ensure that each component behaves as expected. We use the unittest framework, which is part of Python's standard library, to write and run our unit tests.

## unittest procedure:
To perform the test, run the test.py file as follows:
*In the terminal, navigate to the project directory - cd CO2_emissions
*run the following commands;
    pyenv install 3.7.9
    pyenv local 3.7.9
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install flask
    export FLASK_APP=co2_emissions.py
    export FLASK_ENV=development
*finally, run python3 test.py
    
## CONTRIBUTION
Contributions are welcome! 
Feel free to open issues or pull requests for any improvements
or features you'd like to see in the application.# co2_emissions_app
