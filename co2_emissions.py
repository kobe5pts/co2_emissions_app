
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Route for the home page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route for displaying the CO2 emissions search page
@app.route('/co2_emissions', methods=['GET'])
def search_co2_emissions_page():
    return render_template('search_co2_emissions.html') 

# Route for displaying entity not found page
@app.route('/entity_not_found')
def entity_not_found():
    return render_template('entity_not_found.html')

# Route for displaying year not provided page
@app.route('/year_not_provided')
def year_not_provided():
    return render_template('year_not_provided.html')           

# Route for handling CO2 emissions search request
@app.route('/search_results_co2_emissions', methods=['POST'])
def search_co2_emissions():
    if request.method == 'POST':
        entity = request.form.get('entity')
        year = request.form.get('year')

        if not entity:
            return render_template('entity_not_provided.html')

        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('co2_emissions_data.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            # Check if the entity exists in the emissions table
            cur.execute("SELECT COUNT(*) FROM emissions WHERE Entity = ?", (entity,))
            entity_count = cur.fetchone()[0]

            if entity_count == 0:
                return render_template('invalid_entity.html', entity=entity)

            # Check if the year is provided
            if not year:
                return render_template('year_not_provided.html')

            # Construct SQL query for joining emissions and globalcarbonprojection tables
            # LEFT JOIN globalcarbonprojection g to enrich emissions data with global carbon projection information
            query = """
                SELECT e.Entity, e.Year, e.Annual_CO2_emissions, g.Total, g.Coal, g.Oil, 
                       g.Gas, g.Cement, g.Flaring, g.Other, g.Per_Capita
                FROM emissions e
                LEFT JOIN globalcarbonprojection g 
                ON e.Entity = g.Country AND e.Year = g.Year
                WHERE 1=1 AND e.Entity = ? AND e.Year = ?
            """
            params = (entity, year)

            # Execute the SQL query
            cur.execute(query, params)
            rows = cur.fetchall()

            if not rows:
                return render_template('entity_not_found.html', entity=entity)

            # Render the search results template with the retrieved data
            return render_template('search_results_co2_emissions.html', rows=rows)

        except sqlite3.Error as e:
            # Log database errors
            error_msg = "Database error: {}".format(e)
            app.logger.error(error_msg)
            return render_template('500.html'), 500

        finally:
            # Close the database connection
            if 'conn' in locals():
                conn.close()

    # If the request method is not POST, render the CO2 emissions search page
    return render_template('search_co2_emissions.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
