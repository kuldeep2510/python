
def Frequency(list,ele):
      iCnt=0
      for i in range(len(list)):
            if list[i]==ele:
                  iCnt=iCnt+1
      return iCnt

def main():
      list=[]
      size=int(input("Enter size:"))
      ele=int(input("element to search:"))
      print("Enter elements:")
      for i in range(size):
            data=int(input())
            list.append(data)
      ret=Frequency(list,ele)

      print("Freq of number is:",ret)            




if __name__=="__main__":
      main()