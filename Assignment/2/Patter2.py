
def Star(value):
      for i in range(0,value,1):
            for j in range(1,value+1,1):
                  print(j,end=" ")
                 
      
            print("\r")
                                        




def main():
      print("Enter number:")
      no=int (input())
      Star(no)




if __name__=="__main__":
      main()