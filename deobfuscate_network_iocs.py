# First open an output file and clear it. Then launch "read()" function.
def main():
  with open('out_file.txt', 'w') as out_file:
    out_file.write("")
  read()

# Open a file and read data from it line by line. First, see if the line
# contains both obfuscation methods "[.]" and "hxxp". If it does, replace
# both with deobfuscated substitutes and call the "write()" method  to write
# the deobfuscated line into the output file. Then do the same check, and if
# true, execute the same actions for both obfuscation methods ("[.]" and
# "hxxp")one by one. Continue until the end of file is reached.
def read():
  with open('in_file.txt', 'r') as in_file:
    for line in in_file.readlines():
      if '[.]' and 'hxxp' in line:
        write(line.replace('hxxp', 'http').replace('[.]', '.').
        strip('\n'))
      elif 'hxxp' in line:
        write(line.replace('hxxp', 'http').strip('\n'))
      elif '[.]' in line:
        write(line.replace('[.]', '.').strip('\n'))
      else:
        write(line.strip('\n'))
      continue

# Write (append) given input into the output file.
def write(written):
  with open('out_file.txt', 'a') as out_file:
    out_file.write(written+'\n')
    print(written)

# Call the "main()" function and start the program.
main()