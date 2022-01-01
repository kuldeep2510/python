class Demo:
      A=10  #class variable
      

      def __init__(self):
            self.B=30  #instance variable

      def fun(self):
            print("Inside instance variable method fun")

      @classmethod
      def gun(cls):  #class method
            print("inside class method")

            

def main():
      print("Value of class variable:",Demo.A)

      Demo.gun()

      obj1=Demo()
      print("Value of instance variable :",obj1.B)
      obj1.fun()
     
if __name__=="__main__":
      main()                  


