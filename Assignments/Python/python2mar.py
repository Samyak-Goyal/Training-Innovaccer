##When I am specifying some value inside a class it means I am referring to an object. 
## A class is considered as a general Model where as objects are the real life example of a class 

#1
class Book:
    def __init__(self,pub='BPB') :
        self.publishername=pub


    def EnterBookDetail(self): 
        try:
            self.bookname=input("Enter Book Name :").strip().title() 
            self.author=input("Enter Author Name :").strip().title() 
            self.price=int(input("Enter Price :")) 
            #self.publishername=input("Enter Publisher Name :").strip().title() 
        except ValueError:
            print("Price can be only numeric")
        
    def ShowBookDetail(self): 
        print("Book Name =", self.bookname) 
        print("Author Name =" , self.author) 
        print("Book Price = ",self.price) 
        print("Publisher = ", self.publishername) 

    def AddFile(self):
        try: 
            fv= open("/home/user1/Training Innovaccer/Assignments/Python/BookList.txt","a")
            data =self.bookname +","+self.author + ","+ str(self.price)+ ','+ self.publishername+ '\n'
            fv.write(data)
            print("Record added Successfully")
        except PermissionError:
            print("Permission Denied")
        except FileNotFoundError:
            print("File could not be found") 
        except IOError:
            print("Input Output Error")          
        except:
            print("Sorry Exception Occured!!")    
        finally:
            fv.close()


book1=Book() 
book1.EnterBookDetail() # Book.EnterDetail(book1) 
book1.ShowBookDetail() 
book1.AddFile()
# book2=Book('Penguin')
# book2.EnterBookDetail()
# book2.ShowBookDetail()
# book2.AddFile()
# print("All Information Displayed") 
# print(type(book1)) 
# del(book1) 
# del(book2)
# print("All books entered")

# #2
# class furniture: 
#     def __init__(x ,cl="Brown"): 
#         x.color=cl 
        
#     def InputDetail(x): 
#         x.fname=input("Enter the Furniture Name").title().strip() 
#         x.price=int(input("Enter the Price")) 
#         x.material=input("Enter the Material").title().strip() 
        
#     def DisplayDetail(x): 
#         print("Furtniture Name =%s" %x.fname) 
#         print("Price = %d" %x.price) 
#         print("Material =%s " %x.material) 
#         print("Color =%s " %x.color) 

# class Chair(furniture): 
#     def GetDetail(x1): 
#         x1.No_Legs=int(input("Enter No of Legs")) 
#     def ShowDetail(x1): 
#         print("No of Legs = %d" %x1.No_Legs) 

# class Almirah(furniture): 
#     def EnterDetail(x1): 
#         x1.No_Shelf=int(input("Enter No of Legs")) 
        
#     def AllDetail(x1): 
#         print("No of Shelf = %d " %x1.No_Shelf) 


# myalmirah=Almirah() # Creating object of Almirah Class 
# mychair=Chair() # Creating an object Chair Class 
# mychair.InputDetail() 
# mychair.GetDetail() 
# mychair.DisplayDetail() 
# mychair.ShowDetail() 

# myalmirah.InputDetail()
# myalmirah.EnterDetail()
# myalmirah.DisplayDetail()
# myalmirah.AllDetail()


























































































































