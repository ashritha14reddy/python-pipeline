import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd

load_dotenv()


def insert_into_mongo(df: pd.DataFrame):
    """
    Inserts a Pandas DataFrame into MongoDB.
    Database & collection are created automatically if they do not exist.
    """

    try:
        host = os.getenv("mongo_host")
        port = int(os.getenv("mongo_port"))
        db_name = os.getenv("mongo_db")
        collection_name = os.getenv("mongo_collection")

        # Connect to MongoDB
        client = MongoClient(f"mongodb://{host}:{port}")
        db = client[db_name]
        collection = db[collection_name]

        # Convert DataFrame -> list of dicts (JSON-like)
        records = df.to_dict(orient="records")

        if not records:
            print("⚠️ No records to insert.")
            return

        # Insert records
        result = collection.insert_many(records)

        print(f"✅ Connected to MongoDB at {host}:{port}")
        print(f"📦 Database: {db_name}")
        print(f"📂 Collection: {collection_name}")
        print(f"📥 Inserted {len(result.inserted_ids)} documents")

        client.close()

    except Exception as e:
        print("❌ MongoDB insertion failed")
        print(e)