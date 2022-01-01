def Cheakpositive(value):
      if(value<0):
            print("Number is negative")

      elif(value==0):
            print("Zero")     
      else:
            print("number is Positive")
def main():
      print("enter number:")
      no=int(input())
      Cheakpositive(no)

if __name__=="__main__":
      main()
