## Pymongo
## https://mockaroo.com/
```
https://www.youtube.com/watch?v=VCZs1wfNts4&list=PL6yy_CdpgQmWTXXOxXcfI2KAlblYHOgmV
https://www.mongodb.com/resources/languages/python?utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_language_prosp-nbnon_gic-null_amers-us_ps-all_dv-all_eng_lead&utm_term=best%20database%20for%20python&utm_medium=cpc_paid_search&utm_ad=p&utm_ad_campaign_id=19248124983&adgroup=159746678764&cq_cmp=19248124983&gad_source=1&gclid=Cj0KCQjwmt24BhDPARIsAJFYKk1EUg9KQQ2LZBfuh4Bv9Nyu6qX8EiUNvKw3BcXoGn5oioX00KJNfIYaAgj5EALw_wcB
https://www.youtube.com/watch?v=8eJJe4Slnik&t=5s
```
![image](https://github.com/user-attachments/assets/09ae3cc2-7ee7-4ca2-b170-466a36ffb0af)
![image](https://github.com/user-attachments/assets/9626b1c4-f5b2-473a-b3ed-a5946eba248f)

## Studio 3T - https://www.youtube.com/watch?v=UJ_hiBLlhV4&list=PLRTey0Iqj9jjhDtF0hwDNQmRkuIwA1JXp


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
## use db_1  # id db doesn't exist, it will create

![image](https://github.com/user-attachments/assets/54ffc81d-d313-4815-8c9d-fcc50b2f19c0)

![image](https://github.com/user-attachments/assets/f49a34e6-38bf-450d-9520-3d01cf31e6e8)


