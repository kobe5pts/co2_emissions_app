import csv
import sqlite3

# Open the connection to the database
conn = sqlite3.connect('co2_emissions_data.db')
cur = conn.cursor()

# Drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS emissions')
print("Table 'emissions' dropped successfully")

# Create table to store CO2 emissions data
conn.execute('''CREATE TABLE emissions (
                    Entity TEXT,
                    Code TEXT,
                    Year INTEGER,
                    Annual_CO2_emissions REAL
                )''')
print("Table 'emissions' created successfully")

# Open the file to read it into the database (CO2 emissions data)
with open('CO2_emissions_data/CO2_emissions_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # Skip the header line
    for row in reader:
        print(row)
        cur.execute('INSERT INTO emissions VALUES (?, ?, ?, ?)', row)

print("Data from 'CO2_emissions_data.csv' parsed and inserted successfully")

# Drop the data from the table if it exists
conn.execute('DROP TABLE IF EXISTS globalcarbonprojection')
print("Table 'globalcarbonprojection' dropped successfully")

# Create to store globalcarbonprojection data
conn.execute('''CREATE TABLE globalcarbonprojection (
                    Country TEXT,
                    ISO TEXT,
                    UN_M49 TEXT,
                    Year INTEGER,
                    Total REAL,
                    Coal REAL,
                    Oil REAL,
                    Gas REAL,
                    Cement REAL,
                    Flaring REAL,
                    Other REAL,
                    Per_Capita REAL
                )''')
print("Table 'globalcarbonprojection' created successfully")

# Open the file to read it into the database (co2_emissions_data)
with open('CO2_emissions_data/GlobalCarbonProjectfossil_CO2_emissions.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        values = [row['Country'], row['ISO 3166-1 alpha-3'], row['UN M49'], int(row['Year']), 
                  row['Total'], row['Coal'], row['Oil'], row['Gas'], 
                  row['Cement'], row['Flaring'], row['Other'], row['Per Capita']]
        cur.execute('INSERT INTO globalcarbonprojection VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', values)

# Commit changes and close the connection
conn.commit()
conn.close()
