






def main():
      print("Enter the file name that you want to open:")
      name=input()

      fd=open(name,"rb")# rb is binary mode

      data=fd.read(3)

      print("Data is",data)

      print("Current offset is:",fd.tell)


      fd.seek(-7,2)

      data=fd.read(7)

      print("Data is",data)


if __name__=="__main__":
      main()

#0  begining
#1  current
#2  end
#  kuldeep