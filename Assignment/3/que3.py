
def Manimum(list):
      min=999999999999
      for i in range(len(list)):
            if min>list[i]:
                  min=list[i]

      return min

def main():
      list=[]
      size=int(input("Enter size"))
      for i in range(size):
            data=int(input())
            list.append(data)
      ret=Manimum(list)

      print("Manimum number is:",ret)            







if __name__=="__main__":
      main()