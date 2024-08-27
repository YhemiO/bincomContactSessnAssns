import pandas as pd
import psycopg2

# Load the CSV file into a pandas DataFrame
csv_file_path = r"C:\Users\yemmys_pc\python_dev_beginner\bincomContactSessnAssns\contactSessn3Assn\popularity_in_2008.csv"
data = pd.read_csv(csv_file_path)

# Define the database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',  
    'password': 'admin123',
    'host': 'localhost',
    'port': 5432
}

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute('DROP TABLE IF EXISTS popularity_in_2008')
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS popularity_in_2008 (
        id SERIAL PRIMARY KEY,
        male_name TEXT NOT NULL,
        female_name TEXT NOT NULL
    )
    '''
    cur.execute(create_table_query)
    conn.commit()

    # Insert data into the table
    for _, row in data.iterrows():
        insert_query = '''
        INSERT INTO popularity_in_2008 (male_name, female_name)
        VALUES (%s, %s);
        '''
        # Grabbing the content of both the male and female names in the DataFrame
        cur.execute(insert_query, (row['Male name'], row['Female name']))

    # Commit the transaction
    conn.commit()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        cur.close()
        conn.close()

print("Data inserted successfully.")
