# Demonstration of File Handling Operations in Python
# 1. Open a file in write mode and write data
file = open ("demo_file.txt", "w")
file.write("Hello! This is the first line in the file. \n") 
file.write("Python file handling demonstration. \n") 
file.close() #Properly closing the file
print("Data written successfully. \n")

# 2. Open the file in read mode and read contents
file = open("demo_file.txt", "r")
print ("Reading file contents:")
content = file.read()
print (content) 
file.close()

#3. Open the file in append node and add more content 
file = open("demo_file.txt", "a")
file.write("This line is added later using append mode. \n") 
file.close()

print("Data appended successfully. \n")

# 4. Read the file again to see updated content
file = open("demo_file.txt", "r")
print("Updated file contents:")
updated_content = file.read()
print (updated_content)
file.close()
