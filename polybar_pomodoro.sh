#! /bin/bash

if [[ -e /tmp/pomostat ]]
then
	stat=$(cat /tmp/pomostat)
	if [[ $stat == 0 ]]
	then
		echo "%{F#ff10ff}"
	elif [[ $stat == 1 ]]
 	then
		echo "%{F#009900}"
	else
		echo "%{F#ff0505}"
	fi
else 
	echo "%{F#ff1010}"
fi
