import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection details
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def execute_sql_file(file_path):
    """
    Executes SQL commands from a file.
    """
    with open(file_path, 'r') as f:
        sql_commands = f.read()
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute(sql_commands)
        conn.commit()
        print(f"Executed SQL from {file_path}")
    except Exception as error:
        print(f"Error executing SQL from {file_path}: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()

def load_data_to_postgres(data_file="data/processed/real_estate_transformed.csv", table_name="real_estate"):
    """
    Loads data from a CSV file into a PostgreSQL table.
    """
    try:
        df = pd.read_csv(data_file)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data from {data_file} loaded into {table_name} table.")
    except Exception as error:
        print(f"Error loading data into {table_name}: {error}")

# Main execution
if __name__ == "__main__":
    # Step 1: Create table
    execute_sql_file('sql/create_table.sql')
    
    # Step 2: Load data
    load_data_to_postgres()
    
    # Step 3: Create views
    execute_sql_file('sql/analysis_queries.sql')



