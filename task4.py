class TextFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"Error: The file at '{self.file_path}' was not found.")
        except IOError:
            print(f"Error: An error occurred while reading the file at '{self.file_path}'.")

    def count_lines(self):
        return len(self.content.splitlines())

    def count_words(self):
        return len(self.content.split())

    def count_characters(self):
        return len(self.content)

    def display_content(self):
        print(self.content)

file_path = "text.txt"  
reader = TextFileReader(file_path)

reader.read_file()
print("File Content:")
reader.display_content()
print("\nNumber of lines:", reader.count_lines())
print("Number of words:", reader.count_words())
print("Number of characters:", reader.count_characters())
