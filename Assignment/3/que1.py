
def Display(list):
      mac=0
      for i in range(0,len(list)):

            mac=mac+list[i]
      return mac
      





def main():
      list=[]
      
      
      number=int(input("Enter list length:"))
      
      for i in range(0,number,1):
            data=int(input())
            list.append(data)

           

      ret=Display(list)
      print("Addition is:",ret)





if __name__=="__main__":
      main()
