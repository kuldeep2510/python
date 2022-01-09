
def Division(A,B):
      ans=0.0

      try:ans=A/B
      except ZeroDivisionError as obj:
            print("Exception occoured in ZeroDivisionError")
            print("Exception statement:",obj)
      except Exception:
            print("Exception occore in Exception block")
      finally: print("Division succesfull")# block whic is use to dealocate the resources
      return ans


def main(): 
      no1=int(input("Enter first number:"))
      no2=int(input("enter second number:"))

      ret=Division(no1,no2)

      print("Division is:",ret)




if __name__=="__main__":
      main()