

def Rec(n):
      if n>0:
            Sum=0
            p=n%10
            Sum=Sum+p
            n=n/10
            
            
            
            
            Rec(n-1)
            print(Sum)
            

            




def main():
      n=int(input("Enter number:"))
      Rec(n)


if __name__=="__main__":
      main()