class Arithematic:


      def __init__(self):
            self.Value1=0
            self.Value2=0
      
      def Accept(self,Value1,Value2):
            self.Value1=Value1
            self.Value2=Value2

      def Addition(self):
            return self.Value1 + self.Value2

      def Substraction(self):
            return self.Value1 - self.Value2

      def Multiplication(self):
            return self.Value1 * self.Value2

      def Division(self):
            return self.Value1 / self.Value2



def main():

      print("Enter the value 1:")
      no1=int(input())

      print("Enter the value 2:")
      no2=int(input())

      obj=Arithematic()
      obj.Accept(no1,no2)

      Ret=obj.Addition()
      print("Addition of number is",Ret)
      Ret=obj.Substraction()
      print("Substraction of number is",Ret)
      Ret=obj.Multiplication()
      print("Multiplication of number is",Ret)
      Ret=obj.Division()
      print("Diviosion of number is",Ret)
    



if __name__=="__main__":
      main()