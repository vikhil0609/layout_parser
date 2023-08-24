import os

folder_path = "dataset"  # Specify the path to your folder here

# Get a list of all the files in the folder
file_list = os.listdir(folder_path)



if 'train.json' in file_list:
    print('yes')

# # Loop through the files and rename them
# for index, filename in enumerate(file_list):
#     new_filename = f"201817015240_{index}.jpg"  # Construct the new filename
#     old_filepath = os.path.join(folder_path, filename)
#     new_filepath = os.path.join(folder_path, new_filename)

#     # Rename the file
#     os.rename(old_filepath, new_filepath)

#     print(f"Renamed: {filename} -> {new_filename}")
