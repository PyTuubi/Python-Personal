# Open so you're able to read
#testfile = open("testfile.txt")

# Print file
#print(testfile.read())
# *.seek(0) returns cursor to start of txt file

# Cam also save contents to a variable
#contents = testfile.read()
#print(contents)

# Print a list where the lines are seperated
#print(testfile.readlines())

# Close file to prevent errors
#testfile.close()
# To not worry about closing
#with open("testfile.txt") as testfile:
#    contents = testfile.read()

# Writing and overwriting
# mode="r" is read only
# mode="w" is write only (Will overwrite or create new file if doesn't exist)
# mode="a" is append only (Will add on to the end of the file)
# mode="r+" is reading and writing
# mode="w+" is writing and reading (Will overwrite or create new file if doesn't exist)
with open("testfile.txt",mode="a") as testfile:
    print(testfile.write("asd line"))

