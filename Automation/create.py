



from venv import create


def main():
      print("Enter the file name that you want to create:")
      name=input()

      fd=open(name,"x")

      print("File gets created with the info as:",fd)



if __name__=="__main__":
      main()

