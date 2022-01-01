

def Power(num):
      value=num*num
      return value

PowerX=lambda num:num*num



def main():
      print("Enter number:")
      num=int(input())

      ret=PowerX(num)

      print("Square of number is:",ret)





if __name__=="__main__":
      main()
