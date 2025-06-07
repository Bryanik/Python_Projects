import os
import shutil

#define create_folder
def create_folder(folderPath, folderName):
    #create subfolder path
    os.makedirs(folderPath, exist_ok=True)
    #Print "created # folder"
    print(f"Created new folder: {folderName}")

def main():
    print("Desktop Cleaner App")

    filepath = "C:/Users/user/Downloads"

    #if filepath doesn't exist print error
    if not os.path.exists(filepath):
        print(f"The specified filepath does not exist: ${filepath}")

    #list all items in filepath
    for item in os.listdir(filepath):
        itempath = os.path.join(filepath, item)

        #if item is a file
        if os.path.isfile(itempath):
            #assign variable for subfolder name with the extension
            subfolderName = f"{item.split('.')[-1].upper()} FILES"

            #assign variable for subfolder path
            subfolderPath = os.path.join(filepath, subfolderName)

            #if subfolder path doesn't exist execute create_folder
            if not os.path.exists(subfolderPath):
                create_folder(subfolderPath, subfolderName)
        
            #create new_location: subfolder path + item
            new_location = os.path.join(subfolderPath, item)

            #move itempath to new_location
            shutil.move(itempath, new_location)
            #Print moved #item to #subfolder name
            print(f"Created file '{item}' to folder '{subfolderName}'")

if __name__ == "__main__":
    main()