



from venv import create


def main():
      print("Enter the file name that you want to create:")
      name=input()

      fd=open(name,"w")

      print("Enter the data you want to write in the file")
      data=input()

      fd.write(data)

      fd.close()



if __name__=="__main__":
      main()

