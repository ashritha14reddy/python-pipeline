import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
def load_data_from_postgres():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        query = "SELECT * FROM era5_wind_processed;"
        df = pd.read_sql_query(query, conn)

        conn.close()
        return df

        print("✅ Connected to PostgreSQL successfully!")
        print("PostgreSQL version:", db_version)

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Error while connecting to PostgreSQL")
        print(e)