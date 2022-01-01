def Addition(Value1,Value2):
      ans=0
      ans=Value1+Value2

      return ans


def main():
      no1=0
      no2=0
      ret=0

      print("Enter first nuumber")
      no1=int(input())

      print("Enter second number")
      no2=int(input())

      ret=Addition(no1,no2)

      print("Addition is:",ret)

      


if __name__=="__main__":
      main()