

def Rec(n):
      if n>0:
            
            
            
            
            Rec(n-1)
            print(n,end=" ")

            




def main():
      n=int(input("Enter number:"))
      Rec(n)


if __name__=="__main__":
      main()