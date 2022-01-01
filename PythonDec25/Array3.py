

import array as ARR



def main():


      data=ARR.array('i',[10,20,30,40,50.5]) #i for integer

      print(data)

      print("length of array:",len(data))

      print("Type is:",type(data))

      print(data[0])

      for i in range(0,len(data)):
            print("data from array;",data[i])

      for no in data:
            print(no,end="\t")

            

     


if __name__=="__main__":
      main()