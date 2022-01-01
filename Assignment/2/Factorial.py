
def Factorial(value):
      new=1
      for i in range(1,value+1):
      
            new=new*i
            
      return new


                       




def main():
      print("Enter number:")
      no=int(input())
      ret=Factorial(no)

      print("Factorial of no is:",ret)




if __name__=="__main__":
      main()