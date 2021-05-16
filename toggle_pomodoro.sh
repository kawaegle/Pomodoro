#/!/bin/bash

stat=`cat /tmp/pomostat`

if [[ $stat == 0 ]]
then
	pomodoro.py Stop
else
	pomodoro.py Start
fi

