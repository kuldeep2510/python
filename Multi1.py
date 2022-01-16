import os

def Fun():
      
      print("Inside fun")
      print("'PID is:",os.getpid())

      for i in range(5):
            print("fun",i)



def Gun():
      
      print("Inside gun")
      print("'PID is:",os.getpid())
      for i in range(5):
            print("gun",i)



def main():
      print("'PID is:",os.getpid())
      Fun()
      Gun()
     


if __name__=="__main__":
      main()