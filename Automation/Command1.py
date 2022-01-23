from sys import *;


def main():
      print("Number of command line Argumen are:",len(argv))
      print("Name of Application is",argv[0])

      print("command line argument are:")
      for data in argv:
            print(data)


if __name__=="__main__":
      main()

