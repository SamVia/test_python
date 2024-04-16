import git 
import os
#repo = git.Repo(r"C:\Users\ACER\Desktop\testa\test_python")


# username= "SamVia"
# password = 
# remote = f"https://{username}:{password}@github.com/SamVia/test_python"

# git.Repo.clone_from(remote, r"C:\Users\ACER\Desktop\testa\test_python\test")


def print_dir(basepath):
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                print(entry.name + " DIR")
                print_dir(entry.path)
            else: print(entry.name + " FILE")

# Example usage
basepath = os.getcwd()
print_dir(basepath)
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
