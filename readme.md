# Pomodoro technique
The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro.(Wikipedia)[https://en.wikipedia.org/wiki/Pomodoro_Technique]

That technique permit to foccus hard on a task like a bug or a complex algorithm.

## python logic
For use that methode without a real clock, I decide to use a ~~simple~~ python script to manage time and send a notification when time is over.

use time and unix notify-send to set when a task start and when a task end. 

## Install
Execute the simple install.sh

```shell
./install.sh
```

## Setup
I'm pretty sure that anybody want to know how I manage that part to use it everywhere. 

easy, just copy the Pomodoro.py and launch it with a special keybinding or double click or whatever you want, it'll start a 2 hours long session (2 work and 1 pause)and offer you a delicious coffee (or tea) after.
![coffee](src/coffee.png)

## Notify screen

Start session of work
![Work start](src/work_start.png)

Finish the work session
![work finish](src/work_finish.png)

Session end
![session finish](src/session_finish.png)
