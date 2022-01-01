def Maximum(Value1,Value2):
      if(Value1>Value2):
            return Value1
      else:
            return Value2




def main():
      print("Enter first number:")
      no1=int(input())
      
      print("Enter second number:")
      no2=int(input())

      ret=Maximum(no1,no2)

      print("Maximum number is:",ret)






if __name__=="__main__":
      main()