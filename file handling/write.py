fileobject=open("file1.txt",'w')
fileobject.write('''hai this iss file handling\n
                 
                 there are 4 modes\n1.write\n2.read\n3.append\n4.exclusive''')
fileobject.write("\nhai this is nothing")
fileobject=open("file1.txt",'a')
fileobject.write('\nthis is append mode')