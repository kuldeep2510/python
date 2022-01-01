class Arithematic:
      def __init__(self,a,b):
            print("Inisde init(constructor)")
            self.no1=a
            self.no2=b

      def Addition(self):
            ans=self.no1+self.no2
            return ans

def main():
      print("Enter first number :")
      x=int(input())

      print("Enter second number:")
      y=int(input())

      obj=Arithematic(x,y)
      ret=obj.Addition()

      print("addition is:",ret)


if __name__=="__main__":
      main()



# self keyword similar as this 