class Demo:
      A=10
      B=20

      def __init__(self):
            self.C=30
            self.D=40

def main():
      print("Value of A:",Demo.A)
      print("Value of B:",Demo.B)
      obj1=Demo()
      obj2=Demo()

      print("Vaue of C from obj1:",obj1.C)
      obj1.C=0
      print("Vaue of C from obj1:",obj1.C)
      print("Value of C from Obj2:",obj2.C)

if __name__=="__main__":
      main()                  


#static variable in python that is class variable