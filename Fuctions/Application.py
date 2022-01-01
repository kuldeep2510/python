#import Marvellous
#from Marvellous import *;
import Marvellous as M
import Infosystems

def main():
      print("Inside Module",__name__)
      no1=int(input("enter first number"))
      no2=int(input("enter second number"))

      ret=M.Addition(no1,no2)
      print("Addition is", ret)

      ret=Infosystems.Substraction(no1,no2)
      print("Substraction is", ret)

if __name__=="__main__":
      main()      