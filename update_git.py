import git 
import os
import streamlit as st
import sqlite3 as sq
import random
import datetime
#repo = git.Repo(r"C:\Users\ACER\Desktop\testa\test_python")


username= "SamVia"
password = st.text_input("input text")
remote = f"https://{username}:{password}@github.com/SamVia/test_python"
try:
    git.Repo.clone_from(remote, r"/mount/src/test_python/database")
except:
    pass

def print_dir(basepath):
    with os.scandir(basepath) as entries:
        for entry in entries:

            if entry.is_dir():
                print(entry.name + " DIR")
                st.write(entry.path + " DIR")
                print_dir(entry.path)
            else: 
                print(entry.name + " FILE")
                st.write(entry.path + " FILE")
                if os.path.exists(entry.path):
                    if os.access(entry.path, os.R_OK):
                        print(f"Read permission is granted for '{entry.path}'.")
                    else:
                        print(f"Read permission is not granted for '{entry.path}'.")
                    
                    if os.access(entry.path, os.W_OK):
                        print(f"Write permission is granted for '{entry.path}'.")
                    else:
                        print(f"Write permission is not granted for '{entry.path}'.")
                    
                    if os.access(entry.path, os.X_OK):
                        print(f"Execute permission is granted for '{entry.path}'.")
                    else:
                        print(f"Execute permission is not granted for '{entry.path}'.")
                else:
                    print(f"The file '{entry.path}' does not exist.")

# Example usage
basepath = os.getcwd()
st.write(f"basepath: {basepath}")
print_dir(basepath)
os.chmod("/mount/src/test_python/database/test.db", 0o777)
st.write(os.access("/mount/src/test_python/database/test.db", os.X_OK))



def create_connection(db_file):
    conn = None
    try:
        conn = sq.connect(db_file)
        print(sq.version)
    except:
        pass
    return conn

def create_table(conn, table_sql):
    try:
        c = conn.cursor()
        c.execute(table_sql)
    except:
        pass
        
def generate_str_table(name):
    sql_create_table = f"CREATE TABLE IF NOT EXISTS {name} (\n"
    sql_create_table += "id INTEGER PRIMARY KEY,\n"
    sql_create_table += "velocity REAL NOT NULL,\n"
    sql_create_table += "day INTEGER NOT NULL,\n"
    sql_create_table += "timestamp TEXT NOT NULL\n"
    sql_create_table += ");"
    return sql_create_table

def insert_create(conn, element, name):
    sql_insert = f"INSERT INTO {name}(id, velocity, day, timestamp) VALUES(?, ?, ?, ?)"
    cur = conn.cursor()
    cur.execute(sql_insert, (element["id"], element["velocity"], element["day"], element["timestamp"]))
    conn.commit()
    return cur.lastrowid
day = random.randint(0,31)
timed = datetime.now()
table_name =  f"_{timed.year+4}_{timed.month+4}_{day}"
db = r"/mount/src/test_python/database/test.db"
conn = create_connection(db)


if conn is not None:
    table = generate_str_table(table_name)
    create_table(conn, table)
    print("connection successful")
    
    
    for i in range(3):
        element = {
            "id": i,
            "velocity": random.randint(0, 10) + random.randint(0, 10)/10,
            "day": day,
            "timestamp": f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0, 59)}"
        }
        insert_create(conn, element, table_name)
        print("Inserting element")
else:
    print("no connection established")
print("DONE")
conn.close()



cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
table_names = [table[0] for table in tables]
st.write(table_names)






# repo.git.add(r"C:\Users\ACER\Desktop\testa\test_python\test.db")
# repo.index.commit("pushed db")

# origin = repo.remote(name="origin")
# origin.push()
# print(os.path.realpath("test_python/test.tb"))


# import git
# import os
# import traceback

# def push_db_file_to_repo(file_path, commit_message, github_username, github_pat):
#     try:
#         # Get the current working directory
#         repo_path = os.path.realpath(r"test_python")

#         # Open the repository
#         repo = git.Repo(repo_path)

#         # Stage the file for commit
#         repo.index.add([file_path])

#         # Commit the changes
#         repo.index.commit(commit_message)

#         # Push the changes to GitHub with credentials in URL
#         origin = repo.remote(name='origin')
#         origin_url = origin.config_reader.get("url")
#         url_with_credentials = origin_url.replace("://", f"://{github_username}:{github_pat}@")
#         origin.push(refspec='HEAD', progress=True, auth=(github_username, github_pat), url=url_with_credentials)

#         print(f"File '{file_path}' pushed to GitHub successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         traceback.print_exc()  # Print full traceback

# # Example usage
# file_path = r"C:\Users\ACER\Desktop\testa\test_python\test.db"
# commit_message = 'Added test.tb'
# github_username = 'SamVia'
# github_pat = 

# # # password = ""
# # # remote = f"https://{username}:{password}@github.com/SamVia/test_python"

# push_db_file_to_repo(file_path, commit_message, github_username, github_pat)
