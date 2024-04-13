import os

DB_PORT = os.getenv('DB_PORT', '5432')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

DB_URL = os.environ.get('DB_URL', f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
DB_ENCRYPTION_KEY = os.getenv('DB_ENCRYPTION_KEY')

DATABRICKS_HOST = os.getenv('DATABRICKS_HOST')
DATABRICKS_TOKEN = os.getenv('DATABRICKS_TOKEN')
DATABRICKS_CLUSTER_ID = os.getenv('DATABRICKS_CLUSTER_ID')

JWT_KEY = os.getenv('JWT_KEY')
