"""---- r mode
will throw error if file is not present """

# File_Object=open("Mukesh.txt","r")
# f=File_Object.read()
# print(f)

"""w--Mode
if file no exist no error 
it will create new file
will override the content"""
# F=open("f2.txt","w")
# F.write("Dont Sleep Mukesh")
""""""
# F=open("f2.txt","r")
# print(F.read())


"""r+ mode
-- Normally Do first Read Then Write
If you Do Write operation First Then The Curser Will Write from The Begining and will stop at the end point of write content"""
# f1=open("f2.txt","r+")
# print(f1.tell())
# f1.write(" Oops")
# print(f1.tell())
# print(f1.read())

"""W+ Mode
override the data
"""
# F3=open("RCB.txt","w+")
# print(F3.tell())

# F3.write("Rcb Won yesterday")
# print(F3.tell())
# F3.seek(0)
# print(F3.read())
# print(F3.tell())
""" a mode
only write no read"""
# File4=open("Append.txt","a")
# File4.write("Thank You")
# print(File4.read())

"""a+ mode"""
f=open("Append.txt","a+")
f.write("Welcome")
print(f.tell())
f.seek(0)
print(f.read())
#summary of file io
# File Object=open("File.txt","w+")
File_Object.write("Hello World")        
File_Object.seek(0)  # Move the cursor to the beginning of the file
print(File_Object.read())  # Read the content of the file   
File_Object.close()  # Close the file to free up resources
# File_Object=open("File.txt","r")      
# print(File_Object.read())  # Read the content of the file
# File_Object.close()  # Close the file to free up resources
# File_Object=open("File.txt","a")  
# File_Object.write("Hello World")  # Append content to the file
# File_Object.close()  # Close the file to free up resources        

with open("File.txt", "w+") as File_Object:
    File_Object.write("Hello World")
    File_Object.seek(0)
    print(File_Object.read())