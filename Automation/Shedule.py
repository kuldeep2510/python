from gettext import install




import time
import datetime
import schedule

def Task():
      print("Task after each minute gets exicuted")
      print("Current time is:",datetime.datetime.now())
def main():
      print("Inside main fuction")
      print("Shedule starts.....")

      schedule.every(1).minutes.do(Task)
      iCnt=0
      while True:
            schedule.run_pending()
            time.sleep(1)
            
            iCnt=iCnt+1

            if(iCnt==10):
                  exit()



if __name__=="__main__":
      main()