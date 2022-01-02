


class Demo:
      A=10
      def __init__(self):
            print("Inside Constructor")
            self.B=20
      
      def fun_instance(self):
            print("Inside Instance method")
            print(self.B)
            print(Demo.A)

      @classmethod
      def fun_class(cls):
            print("Inside class method")
            print(cls.A)
            print(Demo.A)
          #  print(cls.B)  error obj did not created while calling
      
      @staticmethod
      def fun_static():
            print("Inside static method")
            print(Demo.A)
           # print(Demo.B)

      def __del__(self):
            print("Inside Destructor")

def main():
      print("Inside main")
     
      obj=Demo()
      obj.fun_instance()

      Demo.fun_class()
      obj=None   #garbage collecor explicitly call by None

      Demo.fun_static()

  


if __name__=="__main__":
      main()
          

#instance method 
# No decorator
# self as a parameter
# call by obj name
# can access instance as well as class variable
# 
# 
# 
# class method 
# @classmethod
# cls as a parameter
# call by  class name
# can access class variable
# 
# 
# satic method
# @static method
# no parameter
# call by class name  
# can access class variable using class name      