def Division(A,B):
      Ans=0.0
      Ans=A/B
      return Ans

def SmartDivision(Func_Name):
      def Inner(A,B):


            if A<B:
                  A,B=B,A

            return Func_Name(A,B)
      return Inner

Division=SmartDivision(Division)# exicute this line first then /if/ starter

def main():
      
      No1=0
      No2=0
      print("Enter 1st number")
      No1=int(input())

      No2=int(input("Enter second number:"))

      ret=Division(No1,No2)
      print("Division is",ret)


if __name__=="__main__":
      main()