class Base1:
      def __init__(self):
            self.A=10

      def fun(self):
            print("Inside Base1 fun")


class Base2:
      def __init__(self):
            self.B=20

      def fun(self):
            print("Inside Base2 gun")

class Derived(Base1,Base2):
      def __init__(self):
            self.C=30
            Base1.__init__(self)
            Base2.__init__(self)
            print("Inside derived")

      def sun(self):
            print("Inside Derived sun")


def main():
      dobj=Derived()
      dobj.fun()
      #dobj.gun()



if __name__=="__main__":
      main()



