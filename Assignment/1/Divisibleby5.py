def CheakDivisible(value):
     if(value%5==0):
           return True
     else:
            return False           
     
def main():
      print("enter number:")
      no=int(input())
      ret=CheakDivisible(no)
      if(ret==True):
            print("Number is Divisible by 5")
      else:
            print("Number is not divisbile by 5")            



if __name__=="__main__":
      main()
