import toml
#fill the path (relative or absolute) to the firebase key in json format
path_to_firebase_key = str(input("input key path in json format: "))
output_file = str(input("output path: ")) + "/secrets.toml"

#path_to_firebase_key = r""
#output_file = ".streamlit/secrets.toml"
#creates a folder in the directory with the streamlit project if not present, beware it *rewrites* the file content

#gathers data from json file
with open(path_to_firebase_key) as json_file:
    json_text = json_file.read()
#formats the data
config = {"textkey": json_text}
toml_config = toml.dumps(config)
#writes the data into final file
with open(output_file, "w") as target:
    target.write(toml_config)