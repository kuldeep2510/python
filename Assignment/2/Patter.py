
def Star(value):
      for i in range(0,value,1):
            for j in range(value,0,-1):
                  print("* ",end="")
                 
      
            print("\r")
            value=value-j                             




def main():
      print("Enter number:")
      no=int (input())
      Star(no)




if __name__=="__main__":
      main()