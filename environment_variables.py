from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
Collection_Name = os.getenv('collection_name')
Client_Url = os.getenv('client_url')
Database_Name = os.getenv('database_name')

