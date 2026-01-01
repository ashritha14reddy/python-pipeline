PostgreSQL to MongoDB Data Pipeline
A Python-based ETL (Extract, Transform, Load) pipeline designed to migrate relational data from PostgreSQL to MongoDB. This project focuses on data cleaning, secure configuration, and automated schema creation.

🚀 Overview
This pipeline automates the transition from structured SQL tables to flexible NoSQL documents. It handles connection management, data preprocessing with Pandas, and ensures data types are compatible across both environments.

Key Features
Automated Extraction: Streamlined data retrieval from PostgreSQL.

Data Transformation: Automated cleaning (deduplication, null handling) via Pandas.

Type Safety: Converts PostgreSQL date fields into MongoDB-compatible BSON datetime objects.

Flat Schema: Preserves row-level data as flat key-value documents for high-speed querying.

Secure Config: Uses environment variables (.env) for database credentials.

Auto-Provisioning: Automatically creates MongoDB databases and collections if they don't exist.

🏗️ Data Flow
PostgreSQL → Pandas DataFrame → Data Cleaning/Processing → MongoDB

📁 Project Structure
main.py – Orchestrates the pipeline and handles data transformation logic.

pg_handler.py – Manages PostgreSQL connection and data extraction.

mongo.py – Manages MongoDB connection and bulk insertion.

.env – Stores sensitive database configuration.

requirements.txt – List of project dependencies.

🛠️ Installation & Setup
1. Prerequisites
Python 3.x

PostgreSQL (Running and accessible)

MongoDB (Local, Docker, or Atlas)

2. Clone & Install
Bash

# Clone the repository
git clone https://github.com/yourusername/pg-to-mongodb.git
cd pg-to-mongodb

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
3. Configuration
Create a .env file in the root directory:

Code snippet

# PostgreSQL
PG_HOST=localhost
PG_PORT=5432
PG_DATABASE=your_db
PG_USER=your_user
PG_PASSWORD=your_password
PG_TABLE=your_table

# MongoDB
MONGO_URI=mongodb://localhost:27017/
MONGO_DB_NAME=migrated_db
MONGO_COLLECTION_NAME=data_collection
🏃 Execution
To run the pipeline, execute the main script:

Bash

python main.py
Expected Output:
Logs indicating the connection status.

Total number of records extracted from PostgreSQL.

Confirmation of successful insertion into MongoDB.

🎯 Use Cases
SQL to NoSQL Migration: Moving legacy data to modern cloud environments.

Data Engineering Portfolio: Demonstrating proficiency in Python, SQL, and NoSQL.

ETL Practice: Building a foundation for complex data pipelines and backend tasks.