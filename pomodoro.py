#!/bin/python3
import sys, time, os

Minutes = 60
Work_session=25*Minutes
Semi_work=Work_session/2
Pause_session= 5*Minutes
Semi_pause = Pause_session/2
Stop = 4 # 2 hour of pomodoro and need a big break
Timer="" #icon empty
Timer_start="" # icon sand up
Timer_stop="" # flag
Timer_cofee="" # cofee

def bar(icon):
	bar = open("/tmp/pomodoro","w+")
	bar.write(icon)
	bar.close()

def read_stat():
	stat=open("/tmp/pomostat","r")
	status = int(stat.readline())
	return status

def write_stat(status):
	stat=open("/tmp/pomostat", "w+")
	stat.write(status)
	stat.close()

#start 25 min work
def Session_start(Work_session):
	if read_stat() == 0:
		os.system("notify-send -a Pomodoro " + f"\"Work is starting {Timer_start}\"")
		bar(Timer_start)
		while Work_session != 0:
			if read_stat() == 0:
				time.sleep(Minutes)
				Work_session -=Minutes
			else:
				print("work finish")
				sys.exit()
		os.system("notify-send -a Pomodoro "+ f"\"Finish work {Timer_stop}\"")

#start 5 min break
def Session_pause(Pause_session):
	if read_stat() == 0:
		os.system("notify-send -a Pomodoro " + f"\"Pause is starting {Timer_start}\"")
		bar(Timer_stop)
		while Pause_session != 0:
			if read_stat() == 0:
				time.sleep(Minutes)
				Pause_session -=Minutes
			else:
				print("pause finish")
				sys.exit()
		os.system("notify-send -a Pomodoro "+ f"\"Finish Pause {Timer_stop}\"")

#Loop call at start for 2 hours
def start_pomodoro():
	Session_start(Work_session)
	time.sleep(1*Minutes)
	Session_pause(Pause_session)

def main(Stop):
	if len(sys.argv) == 1:
		os.system("notify-send -a Pomodoro \"need argument\"")
	elif sys.argv[1].capitalize() == "Start":
		write_stat("0")
		while Stop != 0:
			if read_stat()==0:
				start_pomodoro()
				Stop -=1
			else:
				sys.exit()

	elif sys.argv[1].capitalize() == "Stop":
		os.system("notify-send -a Pomodoro stop")
		write_stat("1")
		bar(Timer)
	else:
		os.system(f"notify-send -a Pomodoro {sys.argv[1]}")
		bar(Timer)

main(Stop)