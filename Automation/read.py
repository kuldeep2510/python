
import os


from venv import create


def main():
      print("Enter the file name that you want to create:")
      name=input()
      
      if os.path.exists(name):
            fd=open(name,"r")

            data=fd.read()
      

            print("Data from file is:",data)

            fd.close()

      else:
            print("There is no such a file")



if __name__=="__main__":
      main()

