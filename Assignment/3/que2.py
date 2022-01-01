
def Maximum(list):
      max=0
      for i in range(len(list)):
            if max<list[i]:
                  max=list[i]

      return max

def main():
      list=[]
      size=int(input("Enter size"))
      for i in range(size):
            data=int(input())
            list.append(data)
      ret=Maximum(list)

      print("Maximum number is:",ret)            







if __name__=="__main__":
      main()