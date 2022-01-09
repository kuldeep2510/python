

def Rec(n):
      if n>0:
            
            
            
            print(n,end=" ")
            Rec(n-1)
            

            




def main():
      n=int(input("Enter number:"))
      Rec(n)


if __name__=="__main__":
      main()