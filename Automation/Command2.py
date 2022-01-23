from sys import *;


def main():

      print("Number of command line Argumen are:",len(argv))
      print("Name of Application is",argv[0])
      print("command line argument are:",argv[1])
      print("command line argument are:",argv[2])

      
      
      ans=int(argv[1])+int(argv[2])

      print("addition is:",ans)


if __name__=="__main__":
      main()

