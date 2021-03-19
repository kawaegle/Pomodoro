import sys, time, os

Minutes = 60
Work_session=25*Minutes
Semi_work=Work_session/2
Pause_session= 5*Minutes
Semi_pause = Pause_session/2
Stop = 4 # 2 hour of pomodoro and need a big break
Timer="" #icon empty
Timer_start="" # icon sand up
Timer_stop="" # flag
Timer_cofee="" # cofee

#start 25 min work
def Session_start(Work_session):
	os.system("notify-send -a Pomodoro "+ f"\"Work Start {Timer_start}\"")
	while(Work_session != 0):
		time.sleep(Minutes)
		Work_session -=Minutes
	os.system("notify-send -a Pomodoro " + f"\"Finish Work {Timer_stop}\"")

#start 5 min break
def Session_pause(Pause_session):
	os.system("notify-send -a Pomodoro " + f"\"Pause is starting {Timer_start}\"")
	while(Pause_session != 0):
		time.sleep(Minutes)
		Pause_session -=Minutes
	os.system("notify-send -a Pomodoro "+ f"\"Finish Pause {Timer_stop}\"")

#Loop call at start for 2 hours
while Stop != 0:
	print(f"it remain {Stop} loop")
	Session_start(Work_session)
	Session_pause(Pause_session)
	Stop -=1
os.system("notify-send -a Pomodoro " + f"\"Finish Session {Timer_cofee} Go take a cup of cofee.\"")