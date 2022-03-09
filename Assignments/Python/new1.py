# How To Read the Records From a File 
# How can I Count No. of Records And The Size of the File? 
# import os 
##1
# try: 
#     fv=open("/home/user1/Training Innovaccer/Assignments/Python/BookList.txt","r") 
#     mydata=fv.read()
#     filesize=os.path.getsize("/home/user1/Training Innovaccer/Assignments/Python/BookList.txt")
#     print("File size=%d" %filesize)
#     print("File records are: ")
#     print(mydata)
#     lines=mydata.split('\n')
#     print("no. of records= %d" %(len(lines)-1))
    
# except FileNotFoundError: 
#     print("Sorry File is Not Found") 
# except PermissionError: 
#     print("Sorry...Read Permission Denied") 
# except IOError: 
#     print("Sorry IO Error Occured...") 
# except MemoryError: 
#     print("Sorry...Memory is Insufficient") 
# except: 
#     print("Sorry...Some Exception Raised") 



##2
# import PyPDF2 
# from PyPDF2 import PdfFileReader # Creating a pdf file object and Opening the File in rb Mode pdf is the File Handler 
# try:
#     pdf = open("/home/user1/Training Innovaccer/Assignments/Python/notes2mar", "rb") # Creating pdf reader object. 
#     pdf_reader = PyPDF2.PdfFileReader(pdf) # Checking total number of pages in a pdf file. 
#     print("Total number of Pages:", pdf_reader.numPages) 
# except FileNotFoundError:
#     print("The File is not Present")
# except PermissionError:
#     print("Permission Denied")


# import pandas
# mydata=pandas.read_csv("notes2mar2")    #index values will come automatically in the left hand side
# #print(mydata)

# mydata1=mydata.to_string(index=False)
# print(mydata1)

#pandas is a package which internally uses some other different packages as well. eg-numpy, openpyxl, xlrd...etc  
#pandas was introduced in Python in 2016 and further python got tremendous popularity in the IT Market 







# ##3
# import ipaddress
# try: 
#     pp=ipaddress.ip_address(input("Enter Valid IP Address")) 
#     print("IP Address Obtained : " + str(pp)) 
# except ValueError: 
#     print("Invalid IP Address") 






# from numpy import maximum
# import pandas
# mydata=pandas.read_csv("notes2mar2") 
# max_death=mydata["Total_Deaths"].max()
# print("Max death : ",max_death)
# min_death=mydata["Total_Deaths"].min()
# print("Min death : ",min_death)
# avg_death=mydata["Total_Deaths"].mean()
# print("Avg death : ",avg_death)
# mydata2=mydata.dropna

##os.system(cp firstfilepath newfilepath) #copies the file
























































