name=input("\n Enter Your Name: ")
if len(name)>=3:
    # defining the minimum length of name.. 
    print('\n Hello',name,end=", How are you? ")
    # "end" parameter used to add string.. 
else:
    print("Enter minimum three as input")