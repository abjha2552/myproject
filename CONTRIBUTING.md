 @staticmethod
    def convtoDict(ob):
        # print(ob.__dict__)  #{"id":10,"Name":"Vikas","age":39,"Mob":1234}
        return ob.__dict__

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
        
    help me out to design functions that i want to implement in choice no.8,9,10 and 11 to save and load data from file in pickle as well as json format.
