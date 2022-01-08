class Demo:
      Value=0

      def __init__(self,no1,no2):
            self.no1=no1
            self.no2=no2
      def fun(self):
            print(self.no1)

      def gun(self):
            print(self.no2)      


      






def main():
      print("enter the value 1:")
      no1=int(input())
      
      print("enter the value 2:")
      no2=int(input())
      
      obj1=Demo(11,21)
      obj2=Demo(51,101)
      obj=Demo(no1,no2)

      obj1.fun()
      obj2.fun()
      obj1.gun()
      obj2.gun()

      obj.fun()
      obj.gun()




if __name__=="__main__":
      main()