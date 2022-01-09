class Demo:
      def __init__(self):
            self.i=10
            self.j=20

      def Add(self,a):  # we loose this method after calling second method
            print("Inside add with one parameter")
      
      def Add(self,a,b):
            print("Inside add with two parameter")





def main():
      obj=Demo()

      obj.Add(10,21)



if __name__=="__main__":
      main()


      #No support overloading