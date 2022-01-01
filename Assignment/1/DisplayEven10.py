def Display(size):
      for i in range(1,(size*2+1)):
            if(i%2==0):
                  print(i)
      
def main():
      print("Enter size")
      size=int(input())
      Display(size)

if __name__=="__main__":
      main()
