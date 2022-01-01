def Digit(value):
      iSum=0
      while(value!=0):
            
            no=value
            value=value//10
            po=value
            value=value*10
            no=no-value
            iSum=iSum+no
          
            value=po
      return iSum            

      


def main():
      print("enter number:")
      no=int(input())
      ret=Digit(no)

      print("Addition of digits are:",ret)
    


if __name__=="__main__":
      main()