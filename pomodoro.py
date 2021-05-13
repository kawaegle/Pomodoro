#!/bin/python3
import sys, time, os

Minutes = 60
Work_session=25*Minutes
Pause_session= 5*Minutes
loop = 4 # 2 hour of pomodoro and need a big break
Timer="" #icon empty
Timer_start="" # icon sand up
Timer_stop="" # flag
Timer_cofee="" # cofee

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
	os.system("notify-send -a Pomodoro " + f"\"Work is starting {Timer_start}\"")
	print("work start")
	while Work_session != 0:
		if read_stat() == 0:
			time.sleep(Minutes)
			Work_session -=Minutes
		else:
			sys.exit()
			write_stat("2")
	os.system("notify-send -a Pomodoro "+ f"\"Finish work {Timer_stop}\"")
	print("work stop")

#start 5 min break
def Session_pause(Pause_session):
	os.system("notify-send -a Pomodoro " + f"\"Pause is starting {Timer_start}\"")
	print("pause start")
	while Pause_session != 0:
		if  read_stat() == 1:
			time.sleep(Minutes)
			Pause_session -=Minutes
		else:
			sys.exit()
			write_stat("2")
	os.system("notify-send -a Pomodoro "+ f"\"Finish Pause {Timer_stop}\"")
	print("pause stop")

#Loop call at start for 2 hours
def start_pomodoro(loop):
	while loop != 0:
		write_stat("0")
		Session_start(Work_session)
		write_stat("1")
		Session_pause(Pause_session)
		write_stat("2")
		loop=loop-1
		print(loop)
	os.system("notify-send -a Pomodoro Finish")
	write_stat("2")

def main():
	if len(sys.argv) == 1:
		os.system("notify-send -a Pomodoro \"need argument\"")
	elif sys.argv[1].capitalize() == "Start":
		start_pomodoro(loop)
	elif sys.argv[1].capitalize() == "Stop":
		os.system("notify-send -a Pomodoro stop")
		write_stat("2")
	else:
		os.system(f"notify-send -a Pomodoro {sys.argv[1]}")

main()

