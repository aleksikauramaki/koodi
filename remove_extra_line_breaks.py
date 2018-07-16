import pyperclip

data = ""

# Get data from clipboard
clip = pyperclip.paste().splitlines()

# Remove extra line breaks, but leave empty lines
for line in clip:
    data = data.lstrip(" ")
    if line == "":
        data += "\n\n"
    else:
        data += ' ' + line

# Initialize variables for second round of modification
data_tmp = data.split("\n")
data_final = ""

# Remove leading whitespaces from otherwise ready text
for line in data_tmp:
    if line == "":
        data_final += "\n\n"
    else:
        data_final += line.lstrip(" ")

# Copy the modified text to clipboard and notify user
pyperclip.copy(data_final)
print("Modified data added to clipboard!")