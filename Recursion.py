
def DisplayX():
      i=0
      while(i<4):
            
            print("kuldeep")
            i=i+1


def DisplayR(no):
      if(no>0) :

            print("Marvellous")
            no=no-1
            DisplayR(no)
            


def main():
      DisplayR(4)

if __name__=="__main__":
      main()