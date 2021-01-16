import winsound
import sys
import os
import time
import random
import datetime
import json



class SetupPomodoro():

    def __init__(self,pomodoroDuration,pomodoroBreak,pomodoroTimes):

        self.pomodoroDuration = pomodoroDuration
        self.pomodoroBreak = pomodoroBreak
        self.pomodoroTimes = pomodoroTimes
        self.pomodoroDurationSecond = 60 * pomodoroDuration
        self.pomodoroBreakSecond = 60 * pomodoroBreak
        self.tuneHejaz = [[440,300],[466,300],[554,300],[587,300],[659,300],[587,400],[554,500],[466,600],[440,1000]]
        self.congrats = [[493,100],[440,125],[493,500],[329,1000],[523,100],[493,125],[523,250],[493,250],[440,1000],[523,100],[493,125],[523,500],[329,1000],[440,100],[392,125],[440,250],[392,250],[369,250],[440,250],[392,500]]
        self.alorsOnDance = [[415,500],[554,500],[830,650],[830,650],[830,400],[659,500],[880,500],[622,650],[622,650],[622,450]]
        self.history = {}

        #Alarm Sounds Loop
    def beepPlay(self,sound,loopTime):
        while loopTime != 0:
            for i in range(0,len(sound)):
                winsound.Beep(int(sound[i][0]),int(sound[i][1]))
            loopTime -= 1
        #Time Counter
    def countPomodoro(self,seconds):
        startPomodoro = seconds
        while startPomodoro != 0:
            sys.stdout.write("{} \r".format(self.converter(startPomodoro)))
            sys.stdout.flush()
            time.sleep(1)
            startPomodoro -= 1
        #Time Converter
    def converter(self,seconds):
        
        minutes = seconds // 60
        seconds = seconds % 60
        return "{} minutes {} seconds remain".format(minutes,seconds)
    # Run Pomodoro Session
    def sessionCalculate(self):
        
        sessionLoop = self.pomodoroTimes
        message="CONGRATS PROFESSOR YOU GOT ALL OF POMODOROSSSS !!!"
        dutyNo = 1

        while sessionLoop != 0:
            os.system("cls")
            #Input from user topic of pomodor session
            duty = input("Duty #{}:".format(dutyNo))
            startPomodoro = datetime.datetime.now()

            print("Session is Running\n")
            self.countPomodoro(self.pomodoroDurationSecond)
            os.system("cls")
            print("Session is done!")

            #Database logs for sessions
            with open ("pomodoroDB.json") as f:
                data = json.load(f)
                temp = data["History"]
            endPomodoro = datetime.datetime.now()
            dateLog = (startPomodoro.strftime("%X"),endPomodoro.strftime("%X"),endPomodoro.strftime("%x"))
            self.history["Duty #{}".format(len(temp))] = [{"pomodoroTask":duty,"dateLog":dateLog}]

            self.addNotes()
            #Clear Temporary History
            self.history = {}

            time.sleep(2)
            self.beepPlay(self.alorsOnDance,2)

            #Last Pomodoro Checker
            if sessionLoop - 1 != 0:
                os.system("cls")
                print("Break is running!\n")
                self.countPomodoro(self.pomodoroBreakSecond)
                os.system("cls")
                print("Break is done!")
                time.sleep(2)
                self.beepPlay(self.alorsOnDance,2)
            else:
                pass
            dutyNo += 1
            sessionLoop -= 1

        os.system("cls")

        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(random.randint(0,3)/10)
        self.beepPlay(self.congrats,2)

    #Write Sessions Data on DB
    def addNotes(self, fileName="pomodoroDB.json"):
        ''' ADD DUTY NOTES TO JSON DB'''
        with open("pomodoroDB.json") as jsonFile:
            data = json.load(jsonFile)
            temp = data["History"]
            temp.append(self.history)

        with open(fileName,"w") as f:
            f.write(json.dumps(data,indent=4,sort_keys=True))
            f.close()

if __name__ == "__main__":

    os.system("cls")
    print("""Welcome Sir!!! I hope you will study hard :D\n
    # We are going to ask you some questions about your pomodoro sessions.
    # Your answers should be an integer for (q1,q2,q3) and minutes for (q1,q2)
    # Your answer should be at least 2 for(q3) \n""",flush=True)

    q1 = "q1)How long does it take yours pomodoros ?\n"
    q2 = "q2) How long does it take your breaks ?\n"
    q3 = "q3) How many pomodoros you will be doing in this session ?\n"

    pomodoroObj = SetupPomodoro(float(input(q1)),float(input(q2)),int(input(q3)))

    history = {"History":[]}
    try:
        with open("pomodoroDB.json") as f:
            f.read()
    except FileNotFoundError:
        with open("pomodoroDB.json", "w") as f:
            f.write(json.dumps(history))

    os.system("cls")

    print("{} minutes pomodoro session is satrting is starting... ".format(pomodoroObj.pomodoroDuration))
    time.sleep(1)
    print("3")
    time.sleep(1)

    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    pomodoroObj.beepPlay(pomodoroObj.tuneHejaz,1)
    print("GO!!GO!!GO!!GO!!GO!!GO!!")

    os.system("cls")
    
    #Last Pomodoro Topic
    # WIP(in process)
    
    pomodoroObj.sessionCalculate()
























