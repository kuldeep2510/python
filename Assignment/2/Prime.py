
def Prime(value):
      flag=True;
         
      for i in range(2,value):
            if(value%i == 0):
                  flag=False
                       
      return flag



def main():
      print("Enter number:")
      no=int(input())
      ret=Prime(no)
      if(ret==True):

            print("It is prime number")
      else:
            print("It is not a prime number")            




if __name__=="__main__":
      main()