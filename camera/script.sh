#!/bin/bash
. ./camera_functions

# run script without camera
DRY_RUN=0

OUTER_OFFSET=5
INNER_OFFSET=10
TOTALITY_DURATION=50


#test
C2=$(echo "($(date +%s.%N) + $OUTER_OFFSET)" | bc -l)
C3=$(echo "($C2 + $TOTALITY_DURATION)" | bc -l)


#T1=$(echo "($(date +%s.%N) + 13.5)" | bc -l)
#T2=$(echo "($C2 + $TOTALITY_DURATION)" | bc -l)

#echo $T2 "T2"

# example
#C2=$(date -d 2022-06-15T18:44:15,100+03:00 +%s.%N)
#C3=$(date -d 2022-06-15T18:44:55,100+03:00 +%s.%N)


C2O=$(echo "$C2 - $OUTER_OFFSET" | bc -l)
C2I=$(echo "$C2 + $INNER_OFFSET" | bc -l)
C3O=$(echo "$C3 + $OUTER_OFFSET" | bc -l)
C3I=$(echo "$C3 - $INNER_OFFSET" | bc -l)


T1=$(date -d 2022-07-16T21:46:15.700308+03:00 +%s.%N)
T2=$(date -d 2022-07-16T22:54:36.943683+03:00 +%s.%N)
T3=$(date -d 2022-07-17T02:24:13.064888+03:00 +%s.%N)
T4=$(date -d 2022-07-17T03:32:34.962535+03:00 +%s.%N)



#INTERVAL $T1 $T2 15

#INTERVAL $T3 $T4 15


# set camera configuration
#SETUP

# baily beads
BURST $C2O $C2 1/4000

# inner corona
AEB $C2 $C2I  1/1000 1 7 4 LTC

# outer corona
AEB $C2I $C3I 1/8    1 7 4 LTC

# inner corona
AEB $C3I $C3  1/1000 1 7 4 ROT

# baily beads
BURST $C3 $C3O 1/4000


echo "done"
