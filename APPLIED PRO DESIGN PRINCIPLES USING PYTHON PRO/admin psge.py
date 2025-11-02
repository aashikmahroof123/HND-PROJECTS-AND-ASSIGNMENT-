class Admin:
    count=0
    def __init__ (self,username,password):
        if (Admin.count==0):
            self.username = username
            self.password = password
            Admin.count = Admin.count + 1
        else :
            print ("Admin already exists")

    def logon(self):
       print("Data analytics and visual representation of Dream Book Shop")
       print("------***--------------***************---------------***-----------")
       un = input ("Enter the User Name :")
       pw = input ("Enter the Password :")
       if (un == self.username and pw == self.password):
          selector = strategyselector()
          selector.run() 
       else:
           print("Incorrect User Name OR Password")


#main methodes
a1 = Admin("MOHAMMED AASHIK","1234567")
a1.logon()
