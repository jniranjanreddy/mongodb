import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URI from environment variable
mongo_uri = os.getenv("MONGO_URI")

# Create a MongoClient instance
client = MongoClient(mongo_uri)

# Example usage: Accessing a database and collection
db = client["reference_db"]                                 
collection = db["formulary_intelligence_reference_library"] # 

# Define your query and perform operations as needed
query = {"therapeutic_class":"Incretin Mimetic Agents (GLP-1 Receptor Agonists)"} 
results = list(collection.find(query))

if results:
    print(len(results))
    delete_result = collection.delete_many(query)
    print(f"Deleted {delete_result.deleted_count} records.")
else:
    print("No records found.")

# Close the connection
client.close()
