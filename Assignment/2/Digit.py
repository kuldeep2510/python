def Digit(value):
      iCnt=0
      while(value!=0):
            
            iCnt=iCnt+1
            value=value//10
            print(value)
      return iCnt            

      


def main():
      print("enter number:")
      no=int(input())
      ret=Digit(no)

      print("Number of digits are:",ret)
    


if __name__=="__main__":
      main()