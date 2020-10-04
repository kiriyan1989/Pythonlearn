hello = open("/Users/kiriyan/VS Code/1/hello.txt", "r") 
print(hello.read()) # read and print all content
hello.close()

hello2 = open("/Users/kiriyan/VS Code/1/hello.txt", "a") # append (add to end) vs write (over write)
hello2.write("\n text file add in new line") # write to file
hello2.close() # always close file.

## if the file name does not exist, it will make a file
#hello3.txt did not exist
hello3 = open("/Users/kiriyan/VS Code/1/hello3.txt", "w") # over write file
hello3.write("new file and new text") # write content to file
hello3.close() # always close file.


#make an HTMl file using Python
web = open("/Users/kiriyan/VS Code/1/html_file.html", "w") #  make a file or over write file 
web.write("<p> This is HTML <p>") # write content to file
web.close() # always close file.