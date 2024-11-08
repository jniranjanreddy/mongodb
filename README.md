## Pymongo
```
https://www.youtube.com/watch?v=VCZs1wfNts4&list=PL6yy_CdpgQmWTXXOxXcfI2KAlblYHOgmV
https://www.mongodb.com/resources/languages/python?utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_language_prosp-nbnon_gic-null_amers-us_ps-all_dv-all_eng_lead&utm_term=best%20database%20for%20python&utm_medium=cpc_paid_search&utm_ad=p&utm_ad_campaign_id=19248124983&adgroup=159746678764&cq_cmp=19248124983&gad_source=1&gclid=Cj0KCQjwmt24BhDPARIsAJFYKk1EUg9KQQ2LZBfuh4Bv9Nyu6qX8EiUNvKw3BcXoGn5oioX00KJNfIYaAgj5EALw_wcB
https://www.youtube.com/watch?v=8eJJe4Slnik&t=5s
```


```import pickle
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
collection = db['your_collection']

# Query data from MongoDB
documents = list(collection.find({}))

# Serialize the MongoDB data and save to a file
with open('mongodb_backup.pkl', 'wb') as file:
    pickle.dump(documents, file)

print("Backup completed successfully.")
```

```
import pickle
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
collection = db['your_collection']

# Load the MongoDB data from the pickle file
with open('mongodb_backup.pkl', 'rb') as file:
    documents = pickle.load(file)

# Insert the data back into MongoDB
if documents:
    collection.insert_many(documents)
    print("Restore completed successfully.")
```
