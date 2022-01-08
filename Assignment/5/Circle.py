
class Circle:
      PI=3.14
      def __init__(self):
            self.Radious=0.0
            self.Area=0.0
            self.Circumfarance=0.0

      def Accept(self,Rad):
            self.Radious=Rad


      def CalculateArea(self):
            self.Area=Circle.PI*self.Radious*self.Radious
      
      def CalculateCircumfarance(self):
            self.Circumfarance=2*Circle.PI*self.Radious

      def Display(self):
            print("Radious of Circle:",self.Radious)
            print("Area of Circle:",self.Area)
            print("Circumfarance of the circle:",self.Circumfarance)







def main():

      print("Enter the radious :")
      Rad=float(input())

      obj=Circle()
      obj.Accept(Rad)
      obj.CalculateArea()
      obj.CalculateCircumfarance()

      obj.Display()



if __name__=="__main__":
      main()