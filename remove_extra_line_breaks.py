data = ""
with open("/home/cornucopia/in_file") as file:
	for line in file.readlines():
             data = data.lstrip(" ")
             if line == "\n":
                 data = data + "\n\n"
             else:
                 data = data + " " + line.lstrip(" ").rstrip("\n")
print(data)
