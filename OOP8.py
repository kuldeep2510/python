class Demo:
      def __init__(self):
            self.A=10
            self.__B=20  #private variable of call


      def fun(self):
            print("Inside fun")

            self.__gun()


      def __gun(self):  #private method of class
            print("Inside gun")
          
      

def main():
      obj=Demo()
      print(obj.A)
      obj.fun()
     # obj.__gun()  Error


if __name__=="__main__":
      main()




 #fun is public 
 # gun is private     