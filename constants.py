import os
from dotenv import load_dotenv

load_dotenv()

LOCATION = os.environ.get("LOCATION")
PROJECT_ID = os.environ.get("PROJECT_ID")
MODEL_NAME = os.environ.get("MODEL_NAME")

CLOUD_SQL_CONNECTION = {
    "host": "127.0.0.1",
    "database": os.environ.get("DATABASE_NAME"),
    "user": "anpenma",
    "password": os.environ.get("PASSWORD"),
    "port": 5432,    
}
print(CLOUD_SQL_CONNECTION)

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

Note:
- Use PostgreSQL syntax
- Include proper table aliases when joining
- Use appropriate PostgreSQL functions
- Ensure proper handling of NULL values
- Consider table relationships when joining
- Use table descriptions to understand the context better

Respond only with the SQL query, no additional text or explanations.

Output Format:
```json
{{
    "query": "<sql query>"
}}
```
"""