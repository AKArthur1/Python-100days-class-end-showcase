### Python Showcase File Methods ###
print("Beginning of the Python File Methods Showcase\n\n\n")


Close_def = "Close: The close() method closes an open file. You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file."
print(f"\n{Close_def}")
print("    Close_f = open('demofile.txt', 'r')")
print("    print(Close_f.read())")
print("    Close_f.close()")






FileNo_def = "File No: The fileno() method returns the file descriptor of the stream, as a number. An error will occur if the operator system does not use a file descriptor."
print(f"\n{FileNo_def}")
print("    f = open('demofile.txt', 'r')")
print("    print(f.fileno()) = 3")




Flush_def = "Flush: The flush() method cleans out the internal buffer."
print(f"\n{Flush_def}")
print("    f = open('myfile.txt', 'a')")
print("    f.write('Now the file has one more line!')")
print("    f.flush()")
print("    f.write('...and another one!')")




IsAtty_def = "Is Atty: The The isatty() method returns True if the file stream is interactive, example: connected to a terminal device."
print(f"\n{IsAtty_def}")
print("    f = open('demofile.txt', 'r')")
print("    print(f.isatty()) = False")





Read_def = "Read: The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file."
print(f"\n{Read_def}")
print("    f = open('demofile.txt', 'r')")
print("    print(f.read()) = Hello! Welcome to demofile.txt This file is for testing purposes. Good Luck!")




Readable_def = "Readable: The readable() method returns True if the file is readable, False if not."
print(f"\n{Readable_def}")
print("    f = open('demofile.txt', 'r')")
print("    print(f.readable()) = True")




ReadLine_def = "Read Line: The readline() method returns one line from the file. You can also specified how many bytes from the line to return, by using the size parameter."
print(f"\n{ReadLine_def}")
print("    f = open('demofile.txt', 'r')")
print("    print(f.readline(5)) = Hello")




ReadLines_def = "Read Lines: The readlines() method returns a list containing each line in the file as a list item. Use the hint parameter to limit the number of lines returned. If the total number of bytes returned exceeds the specified number, no more lines are returned."
print(f"\n{ReadLines_def}")
print("    f = open('demofile.txt', 'r')")
print("    print(f.readlines(33)) = ['Hello! Welcome to demofile.txt', 'This file is for testing purposes.']")




Seek_def = "Seek: The seek() method sets the current file position in a file stream. The seek() method also returns the new postion."
print(f"\n{Seek_def}")
print("    f = open('demofile.txt', 'r')")
print("    f.seek(4)")
print("    print(f.readline()) = o! Welcome to demofile.txt")




Seekable_def = "Seekable: The seekable() method returns True if the file is seekable, False if not. A file is seekable if it allows access to the file stream, like the seek() method."
print(f"\n{Seekable_def}")
print("    f = open('demofile.txt', 'r')")
print("    print(f.seekable()) = True")




Tell_def = "Tell: The tell() method returns the current file position in a file stream. Tip: You can change the current file position with the seek() method."
print(f"\n{Tell_def}")
print("    f = open('demofile.txt', 'r')")
print("    print(f.tell()) = 0")




Truncate_def = "Truncate: The truncate() method resizes the file to the given number of bytes. If the size is not specified, the current position will be used."
print(f"\n{Truncate_def}")
print("    f = open('demofile2.txt', 'a')")
print("    f.truncate(20)")
print("    f.close()")
print("    #open and read the file after the truncate:")
print("    f = open('demofile2.txt', 'r')")
print("    print(f.read()) = Hello! Welcome to de")




Writable_def = "Writable: The writable() method returns True if the file is writable, False if not. A file is writable if it is opened using 'a' for append or 'w' for write."
print(f"\n{Writable_def}")
print("    f = open('demofile.txt', 'a')")
print("    print(f.writable()) = True")




Write_def = "Write: The write() method writes a specified text to the file. Where the specified text will be inserted depends on the file mode and stream position. 'a':  The text will be inserted at the current file stream position, default at the end of the file. 'w': The file will be emptied before the text will be inserted at the current file stream position, default 0."
print(f"\n{Write_def}")
print("    f = open('demofile2.txt', 'a')")
print("    f.write('See you soon!')")
print("    f.close()")
print("    #open and read the file after the appending:")
print("    f = open('demofile2.txt', 'r')")
print("    print(f.read()) = Hello! Welcome to demofile2.txt This file is for testing purposes. Good Luck!See you soon!")




WriteLines_def = "Write Lines: The writelines() method writes the items of a list to the file. Where the texts will be inserted depends on the file mode and stream position. 'a':  The texts will be inserted at the current file stream position, default at the end of the file. 'w': The file will be emptied before the texts will be inserted at the current file stream position, default 0."







print(f"\n{WriteLines_def}")
print("    f = open('demofile3.txt', 'a')")
print("    f.writelines(['See you soon!', 'Over and out.'])")
print("    f.close()")
print("    #open and read the file after the appending:")
print("    f = open('demofile3.txt', 'r')")
print("    print(f.read()) = Hello! Welcome to demofile2.txt This file is for testing purposes. Good Luck!See you soon!Over and out.")






print("\n\n\nEnd of the Python File Methods Showcase")

