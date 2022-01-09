

def outer():
      print("Inside outer fuction")

     
      def Inner():
            print("Inside Inner fuction")


      return Inner #return hashcode ,returning Inner fuction Object if Inner() then call function 


def main():
      func_name=outer()#its call to the outer function 

      func_name()#its call to inner fuction
      #func_name()=Inner()


if __name__=="__main__":
      main()