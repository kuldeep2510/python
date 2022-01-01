from Marvellous import *;





def main():
      print("Total number of elemnt:")
      size=int(input())

     
      
      Data=[]
      print("Enter elemnts:")

      for i in range(size):
            no=int(input())
            Data.append(no)

      print("Your enterd data is :",Data)
      
      ret=Addition(Data)
      print("Addition is:",ret)



if __name__=="__main__":
      main()