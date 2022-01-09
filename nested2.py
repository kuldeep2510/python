def fun():#0X100
      print("Inside fun")

def gun(func_name):#0X200
      print("Inside gun")
      func_name()#fun()

def main():
      gun(fun)#gun(0X100)
      



if __name__=="__main__":
      main()