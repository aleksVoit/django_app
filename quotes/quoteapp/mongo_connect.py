from mongoengine import connect
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

user = os.getenv('MG_USER')
password = os.getenv('MG_PASS')
cluster = os.getenv('MG_CLUSTER')
domain = os.getenv('MG_DOMAIN')
db_name = os.getenv('MG_DB')

# print(user, password, cluster, domain, db_name)


connect(
    db=db_name,
    host=f'mongodb+srv://{user}:{password}@{cluster}.{domain}',
    tlsCAFile=certifi.where()
)

#mongodb+srv://oleksandrvoitushenko:<password>@clusterhw8.gaxzbkd.mongodb.net/
