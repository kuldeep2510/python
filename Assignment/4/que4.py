from functools import reduce

def Range(no):
      if no%2==0:
            return no

def Square(no):
      return no*no

def MUL(a,b):
      return (a+b)

def main():
      data=[]
      print("Enter size of list:")
      size=int(input())
      print("Enter elemnts:")
      for i in range(size):
            data1=int(input())
            data.append(data1)
            
      print(data)
      newdata=list(filter(Range,data))

      print("Data after filter:",newdata)

      incrementData=list(map(Square,newdata))

      ret=reduce(MUL,incrementData)

      print("Data after reduce:",ret)





if __name__=="__main__":
      main()
