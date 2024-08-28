import re
import subprocess

# Step 1: Function to identify programming language
def identify_language(code):
    if re.search(r'\bimport\b', code) and re.search(r'def\b', code):
        return "Python"
    elif re.search(r'#include\b', code) and re.search(r'\bint main\b', code):
        return "C/C++"
    elif re.search(r'public class\b', code) and re.search(r'\bSystem\.out\.print', code):
        return "Java"
    elif re.search(r'<html>', code) and re.search(r'</html>', code):
        return "HTML"
    else:
        return "Unknown"

# Step 2: Function to save code to a file
def save_code_to_file(language, code):
    if language == "Python":
        filename = "user_code.py"
    elif language == "C/C++":
        filename = "user_code.c"
    elif language == "Java":
        filename = "user_code.java"
    elif language == "HTML":
        filename = "user_code.html"
    else:
        return None

    with open(filename, 'w') as file:
        file.write(code)
    
    return filename

# Step 3: Function to run the code based on the language
def run_code(language, filename):
    if language == "Python":
        subprocess.run(["python", filename])
    elif language == "C/C++":
        subprocess.run(["gcc", filename, "-o", "user_code.out"])
        subprocess.run(["./user_code.out"])
    elif language == "Java":
        subprocess.run(["javac", filename])
        subprocess.run(["java", filename.replace('.java', '')])
    elif language == "HTML":
        print("Open the file in a web browser to view the HTML content.")
    else:
        print("Cannot run the code: Unsupported language.")

# Main function
def main():
    user_name = input("Enter your name: ")
    print(f"Hello {user_name}, please paste your code below:")
    user_code = input("Paste your code here:\n")

    language = identify_language(user_code)
    print(f"Detected Programming Language: {language}")

    if language != "Unknown":
        filename = save_code_to_file(language, user_code)
        if filename:
            run_code(language, filename)
    else:
        print("Could not identify the programming language.")

if __name__ == "__main__":
    main()
