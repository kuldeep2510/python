import os


def main():
      print("inside main")
      print("PID of current process:",os.getpid())
      print("PID of parents process",os.getppid())



if __name__=="__main__":
      main()