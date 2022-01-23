
import os


from venv import create


def main():
      print("Enter the file name that you want to create:")
      name=input()
      
      if os.path.exists(name):
           os.remove(name)
           print("File gets Deleted")
      else:
            print("There is no such a file")



if __name__=="__main__":
      main()

