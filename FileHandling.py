import os

def createFile():
    try:
        user_input = input("Enter the file name to create: ")
        text_content = input("Enter the content to write: ")
        with open(user_input, "w") as f:
            f.write(text_content)
        print("✅ File created successfully!\n")
    except Exception as e:
        print("Error creating file:", e, "\n")

def appendText():
    try:
        user_input = input("Enter the file to append text: ")
        text_content = input("Enter the text to append in file: ")
        with open(user_input, "a") as f:
            f.write(text_content)
        print("✅ Text appended successfully!\n")
    except Exception as e:
        print("Error appending text:", e, "\n")

def replaceText():
    try:
        user_input = input("Enter the file name to replace text: ")
        text_content = input("Enter the new content: ")
        with open(user_input, "w") as f:
            f.write(text_content)
        print("✅ Text replaced successfully!\n")
    except Exception as e:
        print("Error replacing text:", e, "\n")

def readTextFromFile():
    try:
        user_input = input("Enter the file name to read: ")
        with open(user_input, "r") as f:
            print("\n--- File Content ---")
            print(f.read())
            print("--------------------\n")
    except Exception as e:
        print("Error reading file:", e, "\n")

def renameFile():
    try:
        old_file = input("Enter the old name of the file: ")
        new_file = input("Enter the new name for the old file: ")
        os.rename(old_file, new_file)
        print("✅ File renamed successfully!\n")
    except Exception as e:
        print("Error renaming file:", e, "\n")

def deleteFile():
    try:
        file_to_delete = input("Enter the file that you want to delete: ")
        os.unlink(file_to_delete)
        print("✅ File deleted successfully!\n")
    except Exception as e:
        print("Error deleting file:", e, "\n")

def getCurrentWorkingDirectory():
    print("Current working directory:", os.getcwd(), "\n")

def changeDirectory():
    try:
        path = input("Enter the path to move: ")
        os.chdir(path)
        print("✅ Directory changed successfully!\n")
    except Exception as e:
        print("Error changing directory:", e, "\n")

def listofDirectory():
    try:
        path = input("Enter the path for getting list of files: ")
        print("\nFiles in directory:")
        print(os.listdir(path))
        print()
    except Exception as e:
        print("Error listing directory:", e, "\n")

# --- Iterative Menu ---
while True:
    print("Choose an option:")
    print("1. Create file")
    print("2. Append text to file")
    print("3. Rename file")
    print("4. Replace text in file")
    print("5. Read text from file")
    print("6. Delete file")
    print("7. Show current working directory")
    print("8. Change directory")
    print("9. List directory contents")
    print("0. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        createFile()
    elif user_choice == "2":
        appendText()
    elif user_choice == "3":
        renameFile()
    elif user_choice == "4":
        replaceText()
    elif user_choice == "5":
        readTextFromFile()
    elif user_choice == "6":
        deleteFile()
    elif user_choice == "7":
        getCurrentWorkingDirectory()
    elif user_choice == "8":
        changeDirectory()
    elif user_choice == "9":
        listofDirectory()
    elif user_choice == "0":
        print("THANK YOU")
        break
    else:
        print("Invalid choice. Please try again.\n")

