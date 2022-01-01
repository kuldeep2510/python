from functools import reduce

def Range(no):
      for i in range(2,no):
            if no%i==0:
                  break
            else:
                  return no
                        
def Square(no):
      return no*2

def MAX(a,b):
      if a>b:
            return a
      else:
            return b      

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

      ret=reduce(MAX,incrementData)

      print("Data after reduce:",ret)





if __name__=="__main__":
      main()
