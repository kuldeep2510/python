
import sys

def main():
      no=sys.getrecursionlimit()

      print(no)
      no=sys.setrecursionlimit(__limit:2000)
      print(no)

if __name__=="__main__":
      main()