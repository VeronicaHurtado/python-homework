# Function to write a string as a new line to a file
# The file argument must be of type <class '_io.TextIOWrapper'> (Output Path open as an object in "write" mode)
def write_to_file(file, lineString):
    file.write(lineString + '\n')