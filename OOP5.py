class Demo:
      A=10
      def __init__(self):
            print("Inside Constructor")
            self.B=20
      
      def fun_instance(self):
            print("Inside Instance method")

      @classmethod
      def fun_class(cls):
            print("Inside class method")
      
      @staticmethod
      def fun_static():
            print("Inside static method")

      def __del__(self):
            print("Inside Destructor")

def main():
      print("Inside main")
      Demo.fun_class()
      Demo.fun_static
      obj=Demo()
      obj.fun_instance

     # obj.fun_static()
     # obj.fun_class()
     


if __name__=="__main__":
      main()
          

#instance method 
# No decorator
# self as a parameter
# call by obj name
# 
# 
# 
# class method 
# @classmethod
# cls as a parameter
# call by  class name
# 
# 
# 
# satic method
# @static method
# no parameter
# call by class name         