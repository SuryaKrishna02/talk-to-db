import os
import bcrypt
import pyrebase
from dotenv import load_dotenv

load_dotenv()
# Firebase Configuration
firebase_config = {
    "apiKey": os.getenv("FB_API_KEY"),
    "authDomain": os.getenv("FB_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FB_DB_URL"),
    "projectId": os.getenv("FB_PROJECT_ID"),
    "storageBucket": os.getenv("FB_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FB_MSG_SENDER_ID"),
    "appId": os.getenv("FB_APP_ID"),
    "measurementId": os.getenv("FB_MEASUREMENT_ID")
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

# Password hashing function
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

LOCATION = os.getenv("LOCATION")
PROJECT_ID = os.getenv("PROJECT_ID")
MODEL_NAME = os.getenv("MODEL_NAME")

CLOUD_SQL_CONNECTION = {
    "host": "127.0.0.1",
    "database": os.getenv("DATABASE_NAME"),
    "user": "anpenma",
    "password": os.getenv("PASSWORD"),
    "port": 5432,
}

TABLE_METADATA = {
    "customers": "Contains the information about customers",
    "invoice": "Stores invoice details of all orders for a given customer",
    "stock": "Contains all details of each unique product being sold."
}

GENERATION_CONFIG = {
    "max_output_tokens": 1024,
    "temperature": 1,
    "top_p": 0.95,
}

SYSTEM_PROMPT = "You are an expert in writing the error free PostgreSQL query based on the questions \
asked by the analyst who is analyzing the transactions of the e-commerce stores."
NL2SQL_PROMPT = """
The following is the information about table schema present in the PostgreSQL:
{context}

Convert this natural language query to PostgreSQL SQL Query:
"{nl_query}"

First, determine the operation type (INSERT, READ, UPDATE, or DELETE) and then generate the appropriate query.

Note:
- Use PostgreSQL syntax
- Include proper table aliases when joining
- Use appropriate PostgreSQL functions
- Ensure proper handling of NULL values
- Consider table relationships when joining
- Use table descriptions to understand the context better
- For INSERT operations, include RETURNING clause to get the created record
- For UPDATE operations, include RETURNING clause to get the updated record
- For DELETE operations, include RETURNING clause to get the deleted record

Respond with the operation type and SQL query in JSON format:
```json
{{
    "operation": "<OPERATION_TYPE>",
    "query": "<sql_query>"
}}
```
"""