#!/usr/bin/env bash

source ./waypoint.source

# ------------ a waypoint which requires escaped double quotes...
waypoint echo "\">>>>>>>>>>>> Test for waypoints <<<<<<<<<<<<\""


# ------------ a waypoint with options...
waypoint uname -a

waypoint echo $*

# ------------ a waypoint interspersed with "non-waypoints"...
waypoint date
date
date
date
date
date
waypoint date


# ------------ a waypoint inside a bash loop...
counter=1
until [ $counter -gt 10 ]
do
  waypoint echo counter = $counter
  ((counter++))
done


# ------------ more waypoints...
waypoint whoami
waypoint id
waypoint pwd

# ------------ more waypoints with environment variables...
waypoint echo my pid is $$
waypoint echo my home is $HOME
waypoint echo this script has been running for $SECONDS seconds

