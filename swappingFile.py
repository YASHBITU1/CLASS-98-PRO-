def swapFileData():
    file1 = input("enter the first file name")
    file2 = input("enter tht second file name")
    with open(file1,'r')as a:
        file1_data = a.read()

    with open(file2,'r')as a:
        file2_data = a.read()    

    with open(file1,'w')as a:
        a.write(file2_data)    
        
    with open(file2,'w')as a:
        a.write(file1_data) 

swapFileData()       