

import array as ARR



def main():


      data=ARR.array('f',[10.2,20.2,30.1,40.2,50.5]) #i for integer

      print(data)

      print("length of array:",len(data))

      print("Type is:",type(data))

      print(data[0])

      for i in range(0,len(data)):
            print("data from array;",data[i])

      for no in data:
            print(no,end="\t")

            

     
      print("Typecode of Array is",data.typecode)

if __name__=="__main__":
      main()