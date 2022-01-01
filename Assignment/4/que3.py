from functools import reduce

def Range(no):
      if no>=70 and no<=90:
            return no

def Increment(no):
      return no+10

def MUL(a,b):
      return (a*b)

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

      incrementData=list(map(Increment,newdata))

      ret=reduce(MUL,incrementData)

      print("Data after reduce:",ret)





if __name__=="__main__":
      main()
