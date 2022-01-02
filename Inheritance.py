


class Base:
      def __init__(self):
            print("Inside base constructor")
            self.A=10  #did not get memory due to did not call init
      
      def fun(self):  #get memory in text section before obj create
            print("Base fun")
            self.C=30

      

########################################################
class Derived(Base):
      def __init__(self):
            Base.__init__(self)
            #super().__init__() upper and this line are same
            print("Inside Derived constructor")
            self.B=20

      def gun(self):
            print("Derived gun")

      



def main():
      dobj=Derived()
      dobj.fun()
      dobj.gun()
      print(dobj.A)




if __name__=="__main__":
      main()



