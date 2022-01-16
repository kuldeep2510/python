



def fact(num):
      
      if num==0:
            return 1

      else:
            
            sum=(num*fact(num-1))

            
            return sum
            
            
      







def main():
      
      num=int(input("Enter number:"))
      ret=fact(num)

      print("factorial is:",ret)



if __name__=="__main__":
      main()