# import os
# import streamlit as st
# import sqlite3 as sq
# import random
# import base64
# from github import Github
# import git

# word = st.text_input("test", key="test")
# repo_dir = "/mount/src/test_python/database"
# username = "SamVia"

# remote = f"https://{username}:{word}@github.com/SamVia/Policumbent-Database.git"


# def decode_base64_file(input_file_path, output_file_path):
#     # Read the base64-encoded content from the input file
#     with open(input_file_path, "rb") as file:
#         encoded_content = file.read()

#     # Decode the base64-encoded content
#     decoded_content = base64.b64decode(encoded_content)

#     # Write the decoded content to the output file
#     with open(output_file_path, "wb") as file:
#         file.write(decoded_content)


# try:
#     if os.path.isdir(repo_dir):
#         # If the directory already exists, just pull the changes
#         st.write("pulling")
#         repo = git.Repo(repo_dir)
#         repo.remotes.origin.pull()
#         decode_base64_file("/mount/src/test_python/database/test.db","/mount/src/test_python/database/test.db")
#     else:
#         #If the directory doesn't exist, clone the repository
#         st.write("cloning")
#         git.Repo.clone_from("https://github.com/SamVia/test_python.git", repo_dir, branch='master', depth=1, auth=("token", word))
#         repo = git.Repo(repo_dir)
#         decode_base64_file("/mount/src/test_python/database/test.db","/mount/src/test_python/database/test.db")
# except: pass
# os.chdir("/mount/src/test_python/database")
# word = st.text_input("test")
# g = Github(word)


# # Then get the specific repo
# repo = g.get_user().get_repo("test_python")

# # Get the ref for the file
# contents = repo.get_contents("test.db")



# os.chdir("/mount/src/test_python/database")






# # try:
# #     subprocess.check_call(["git", "clone", remote, "/mount/src/test_python/database"])
# #     subprocess.check_call(["git", "config", "user.name", "Your Name"])
# #     subprocess.check_call(["git", "config", "user.email", "you@example.com"])
# # except subprocess.CalledProcessError as e:
# #     print(f"An error occurred: {str(e)}")

# def print_dir(basepath):
#     with os.scandir(basepath) as entries:
#         for entry in entries:

#             if entry.is_dir():
#                 print(entry.name + " DIR")
#                 st.write(entry.path + " DIR")
#                 print_dir(entry.path)
#             else: 
#                 print(entry.name + " FILE")
#                 st.write(entry.path + " FILE")
#                 if os.path.exists(entry.path):
#                     if os.access(entry.path, os.R_OK):
#                         print(f"Read permission is granted for '{entry.path}'.")
#                     else:
#                         print(f"Read permission is not granted for '{entry.path}'.")
                    
#                     if os.access(entry.path, os.W_OK):
#                         print(f"Write permission is granted for '{entry.path}'.")
#                     else:
#                         print(f"Write permission is not granted for '{entry.path}'.")
                    
#                     if os.access(entry.path, os.X_OK):
#                         print(f"Execute permission is granted for '{entry.path}'.")
#                     else:
#                         print(f"Execute permission is not granted for '{entry.path}'.")
#                 else:
#                     print(f"The file '{entry.path}' does not exist.")

# # Example usage
# basepath = os.getcwd()
# st.write(f"basepath: {basepath}")
# #print_dir(basepath)
# os.chmod("/mount/src/test_python/database/test.db", 0o777)
# os.chmod("/mount/src/test_python/database", 0o777)
# st.write(os.access("/mount/src/test_python/database/test.db", os.X_OK))



# def create_connection(db_file):
#     conn = None
#     try:
#         conn = sq.connect(db_file)
#         print(sq.version)
#     except:
#         pass
#     return conn

# def create_table(conn, table_sql):
#     try:
#         c = conn.cursor()
#         c.execute(table_sql)
#     except:
#         pass
        
# def generate_str_table(name):
#     sql_create_table = f"CREATE TABLE IF NOT EXISTS {name} (\n"
#     sql_create_table += "id INTEGER PRIMARY KEY,\n"
#     sql_create_table += "velocity REAL NOT NULL,\n"
#     sql_create_table += "day INTEGER NOT NULL,\n"
#     sql_create_table += "timestamp TEXT NOT NULL\n"
#     sql_create_table += ");"
#     return sql_create_table

# def insert_create(conn, element, name):
#     try:
#         sql_insert = f"INSERT INTO {name}(id, velocity, day, timestamp) VALUES(?, ?, ?, ?)"
#         cur = conn.cursor()
#         cur.execute(sql_insert, (element["id"], element["velocity"], element["day"], element["timestamp"]))
#         conn.commit()
#         return cur.lastrowid
#     except:
#         pass
# day = random.randint(0,31)

# table_name =  f"_{4000}_{4}_{day}"
# db = r"/mount/src/test_python/database/test.db"
# conn = create_connection(db)


# if conn is not None:
#     table = generate_str_table(table_name)
#     create_table(conn, table)
#     print("connection successful")
    
    
#     for i in range(3):
#         element = {
#             "id": i,
#             "velocity": random.randint(0, 10) + random.randint(0, 10)/10,
#             "day": day,
#             "timestamp": f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0, 59)}"
#         }
#         insert_create(conn, element, table_name)
#         print("Inserting element")
# else:
#     print("no connection established")

# cursor = conn.cursor()
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# table_names = [table[0] for table in tables]
# st.write(table_names)
# conn.close()

# if st.button("commit"):
#     try:
#         with open("/mount/src/test_python/database/test.db", "rb") as file:
#             content = file.read()
#             content_encoded = base64.b64encode(content)
#     except:
#         pass
#     try:
#         repo.update_file(path=contents.path, message="<commit_message>", content=content_encoded.decode(), sha=contents.sha)
#         print("File updated successfully.")
#     except: pass
# os.chdir("/mount/src/test_python")

# g.close()

import streamlit as st
from google.cloud import firestore
import time
from random import randint
from datetime import datetime
import json
from google.oauth2 import service_account

key = st.secrets["key"]
db = firestore.Client.from_service_account_json(key)
timed = datetime.now()
print(f"{timed.hour}:{timed.minute}:{timed.second}:{round(timed.microsecond/1000)}")

#use caching to avoid establishing the connection every rerun of the app
@st.cache_resource
def connect_to_db():
	key_dict = json.loads(st.secrets["textkey"])
	creds = service_account.Credentials.from_service_account_info(key_dict,)
	credentials = firestore.Client(credentials=creds)
	return credentials

db = connect_to_db()


"""press the button to start the stream of data!
"""
if st.button("start", key = "start_stream"):
    for i in range(0, 3000):
        timed = datetime.now()
        
        
        doc_ref = db.collection(f"_{timed.year}_{timed.month}_{timed.day}").document(str(timed.time()))
        doc_ref.set({
            "id":i,
            "velocity": randint(0,100)+randint(0,10)/10,
            "day": f"{timed.day}",
            "timestamp": f"{timed.hour}:{timed.minute}:{timed.second}:{round(timed.microsecond/1000)}"
        })
        time.sleep(0.3)