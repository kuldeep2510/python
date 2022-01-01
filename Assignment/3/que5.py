
def Prime(list):
      list2=[]
      for i in range(0,len(list)):
            if list[i]==2:
                  list2.append(list[i])
            for j in range(2,list[i]):
                  if list[i]%j==0:
                        break
                  else:
                        list2.append(list[i])
                        break
                        


      return list2                                       

def main():
      list=[]
      size=int(input("Enter size:"))
      
      print("Enter elements:")
      for i in range(size):
            data=int(input())
            list.append(data)
      ret=Prime(list)

      print("Addition of prime number is:",ret)            




if __name__=="__main__":
      main()