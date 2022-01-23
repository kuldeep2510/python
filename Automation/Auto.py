#import statements if necessar
from sys import *

#Entry point of Automation Script
def main():
      print("___________Automation1__________")
      print("Script Name:",argv[0])
      print("Number of Argument accepted:",len(argv)-1)

      if len(argv)> 3 or (len(argv))<2:
            print("Invalid Number of Arguments")
            exit()


      if argv[1]=="-u" or argv[1]=="-U":
            print("Usage:Script is use to perform Addtion of 2 numbers")
            
            exit()


      if argv[1]=="-h" or argv[1]=="-H":
            print("Help:Name of Script __First Argument__Second Argument")
            print("First Argument:Any numaric value")
            print("second Argument:Any numaric value")
            exit()

      
#starter of the Automation Script
if __name__=="__main__":
      main()

