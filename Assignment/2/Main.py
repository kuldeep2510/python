from Arithmetic import *;

def main():
      print("Enter number 1:")
      no1=int(input())

      print("Enter number 2:")
      no2=int(input())
      ret=Add(no1,no2)

      print("Addition is:",ret)

      ret=Sub(no1,no2)
      print("Subtraction is:",ret)

      ret=Mul(no1,no2)
      print("Multiplicaton is:",ret)

      ret=Div(no1,no2)
      print("Division is:",ret)


if __name__=="__main__":
      main()