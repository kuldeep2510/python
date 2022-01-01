
def FactorialAdd(value):
      iSum=0
      for i in range(1,value):
            if(value%i==0):
                  iSum=iSum+i
      
      return iSum      

                       




def main():
      print("Enter number:")
      no=int(input())
      ret=FactorialAdd(no)

      print("Factor Addition is:",ret)




if __name__=="__main__":
      main()