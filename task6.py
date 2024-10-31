def read_txt_file(file_path):
    """Reads the contents of a text file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except IOError:
        return "Error: An error occurred while reading the file."

class UserExtractor:
    def __init__(self, file_path):
        """Initializes the UserExtractor with the file path and an empty dictionary for usernames."""
        self.file_path = file_path
        self.usernames = {}

    def extract_usernames(self):
        """Extracts usernames from the text file into the usernames dictionary."""
        content = read_txt_file(self.file_path)
        if "Error" in content:
            return content

        lines = content.splitlines()
        for line in lines:
            if ':' in line:
                username, _ = line.split(':', 1)  
                self.usernames[username] = line  

        return self.usernames

# Usage 
if __name__ == "__main__":
    file_path = 'text.txt'  
    extractor = UserExtractor(file_path)
    usernames = extractor.extract_usernames()
    if "Error" in usernames:
        print(usernames)
    else:
        print("Extracted Usernames:", usernames)
