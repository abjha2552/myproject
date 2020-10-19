"CMS"
"""Operatios: Add Customer, Search Customer, Delete Customer, Modify Customer,
Display All Customers, Exit
Particular Customer: id,name,age,mob
Object is the real time entity and class is a blueprint of object 
"""
#BLL
import pickle
import json
class Customer:
    cuslist=[]      #[1000,2000,3000]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addCustomer(self):
        Customer.cuslist.append(self)
    def searchCustomer(self):   #self=8000,self.id=20, self.name=0, self.age=0, self.mob=0
        for e in Customer.cuslist:
            if(e.id==self.id):      #Firste=1000, Seconde=2000
                self.name=e.name         #8000.name=self.name="Anil"
                self.age=e.age
                self.mob=e.mob
                return
        raise ValueError("Id not Found")
    @staticmethod
    def deleteCustomer(id):     #id=20
        for e in Customer.cuslist:
            if(e.id==id):
                Customer.cuslist.remove(e)
                return
    def modifyCustomer(self):   #self=12000, self.id=30, self.name="Sonu", self.age=22, self.mob=5555
        for e in Customer.cuslist:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return
                # return 1
        raise ValueError("Id not Found")
        # return 0
    def __str__(self):
        s="Cust ID:"+str(self.id)+" Cust Name: "+self.name+" Cust Age:"+str(self.age)+" Cust Mob:"+str(self.mob)
        return s
    @staticmethod
    def sortbyId(ob):
        return ob.id

    @staticmethod
    def mySort():
        Customer.cuslist.sort(key=Customer.sortbyId)        #[30,10,20]
    @staticmethod
    def savetoPickle():
        f=open("D:/cetpa/cmspickle.txt","wb")
        pickle.dump(Customer.cuslist,f)
        f.close()

    @staticmethod
    def loadfromPickle():
        f = open("D:/cetpa/cmspickle.txt", "rb")
        Customer.cuslist=pickle.load(f)
        f.close()
        
    @staticmethod
    def savetoJson():
        f = open("D:/cetpa/cmsjson.txt", "w")
        json.dump(Customer.cuslist,f,default=Customer.convtoDict)
        f.close()

    @staticmethod
    def convtoObj(d):   #d={"id": "10", "name": "Vikas", "age": "39", "mob": "1234"}
        cus=Customer()
        cus.id=d["id"]
        cus.name = d["name"]
        cus.age = d["age"]
        cus.mob = d["mob"]
        return cus

    @staticmethod
    def loadfromJson():
        f = open("D:/cetpa/cmsjson.txt", "r")
        Customer.cuslist = json.load(f,object_hook=Customer.convtoObj)
        f.close()


      
#PL
print("Welcome to Prashant's CMS")
def showCustomer(cus):      #cus=8000
    print("Cust ID:",cus.id,"Cust Name:",cus.name,"Cust Age:",cus.age,"Cust Mob:",cus.mob )
while(1):
    print("Enter 1 for Add Cust, 2 for Search Cust")
    print("3 for Delete Cust, 4 for Modify Cust")
    print("5 for Display All Cust, 6 for Exit")
    print("7 for sort, 8 to save to Pickle, 9 to load from Pickle")
    print("10 to save to JSON, 11 to load from JSON")
    choice=input("Enter Choice 1 to 11:")
    if(choice=="1"):    #Add Customer
        try:
            cus=Customer()  #cus=1000, cus.id=0, cus.name=0, cus.age=0, cus.mob=0
            cus.id=input("Enter Cust Id:")      #10
            cus.name = input("Enter Cust Name:")    #"Vikas"
            cus.age = input("Enter Cust Age:")      #39
            cus.mob = input("Enter Cust Mob:")      #"1234"
            cus.addCustomer()   #formal=actual, self=cus
            print("Customer Added Successfully")
        except Exception as err:
            print("Error!",err)
    elif(choice=="2"):  #Search Customer
        try:
            cus=Customer()  #cus=8000, cus.id=0, cus.name=0, cus.age=0, cus.mob=0
            cus.id=input("Enter Cust Id:")  #cus.id=20, cus.name=0, cus.age=0, cus.mob=0
            cus.searchCustomer()    #cus.name=8000.name="Anil", cus.age=41, cus.mob=2345
            # showCustomer(cus)
            print(cus)      #cus.__str__()
        except Exception as err:
            print("Error:", err)
    elif(choice=="3"): #Delete Customer: Static Method
        id=input("Enter Cust Id:")  #id=20
        Customer.deleteCustomer(id)
        print("Customer Deleted Successfully")
    elif(choice=="5"):  #Display All Customer:
        for e in Customer.cuslist:
            showCustomer(e)
    elif (choice == "4"):  # Modify Customer
        try:
            cus = Customer()  # cus=12000, cus.id=0, cus.name=0, cus.age=0, cus.mob=0
            cus.id = input("Enter Cust Id:")  # 30
            cus.name = input("Enter Cust Updated Name:")  # "Sonu"
            cus.age = input("Enter Cust Updated Age:")  # 22
            cus.mob = input("Enter Cust Updated Mob:")  # "5555"
            # flag=cus.modifyCustomer()  # formal=actual, self=cus
            cus.modifyCustomer()
            print("Customer Modified Successfully")
            #showCustomer(cus)
            # if(flag==1):
            #     print("Customer Modified Successfully")
            # else:
            #     print("Customer Id not Found")
        except Exception as err:
            print("Error:",err)
    elif (choice == "6"):  # Exit
        print("Thanks for using Prashant's CMS")
        break
    elif(choice=="7"):  #Sort Customers
        Customer.mySort()
        print("Customers Sorted Successfully")
    elif (choice == "8"):  # Save to Pickle
        Customer.savetoPickle()
        print("Data Saved in Pickle Format Successfully")
    elif (choice == "9"):  # Load from Pickle
        Customer.loadfromPickle()
        print("Data Loaded from Pickle Format Successfully")
    elif (choice == "10"):  # Save to JSON
        Customer.savetoJson()
        print("Data Saved to JSON Format Successfully")
    elif (choice == "11"):  # Load from JSON
        Customer.loadfromJson()
        print("Data Loaded from JSON Format Successfully")

