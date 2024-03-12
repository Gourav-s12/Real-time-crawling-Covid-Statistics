import os
def list_files(folder_path):
    try:
        # Get a list of all folders (subdirectories) in the specified folder
        subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        
        # Get a list of all files in the specified folder
        files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # Get a list of all files in each subfolder
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            files.extend([os.path.join(subfolder_path, f).replace('\\', '/') for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))])


        return files
    except OSError as e:
        print(f"Error: {e}")
        return None
    
folder_path = "../../../module_2/part_1/response/"
file_list = list_files(folder_path)
print(file_list)

with open(file_list[0], 'r') as file:
    print("hello")
    for line in file:
        if ":" in line:
            # print(line.strip().split(":"))
            date,val = line.strip().split(":")
            print(f"{date} :- {val}")