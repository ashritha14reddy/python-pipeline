from db_handler.pg import load_data_from_postgres
from db_handler.mongo import insert_into_mongo
import pandas as pd 
import datetime
def process_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep all columns as-is.
    Only minimal cleaning.
    """

    print("🔧 Processing data (all columns, flat)...")

    # Remove duplicate rows (optional but safe)
    df = df.drop_duplicates()
        # 🔥 FIX: Convert date -> datetime
    if "date" in df.columns:
        df["date"] = df["date"].apply(
            lambda x: datetime.datetime.combine(x, datetime.time())
            if isinstance(x, datetime.date)
            else x
        )

    # MongoDB does not like NaN → convert to None
    df = df.where(pd.notnull(df), None)

    return df
def main():
    print("🚀 Pipeline started")

    # Load data from PostgreSQL
    df = load_data_from_postgres()
    print(f"📥 Loaded rows: {len(df)}")
    print(f"📊 Columns: {list(df.columns)}")

    # Process (no transformation)
    processed_df = process_dataframe(df)
    print(f"🧹 Rows after processing: {len(processed_df)}")

    # Insert into MongoDB
    insert_into_mongo(processed_df)
    print("📤 Data inserted into MongoDB")

    print("✅ Pipeline completed successfully")


if __name__ == "__main__":
    main()