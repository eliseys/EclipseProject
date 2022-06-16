#!/bin/bash
. ./camera_functions


OUTER_OFFSET=5
INNER_OFFSET=10
TOTALITY_DURATION=50

#test
C2=$(echo "($(date +%s.%N) + $OUTER_OFFSET)" | bc -l)
C3=$(echo "($C2 + $TOTALITY_DURATION)" | bc -l)

# example
#C2=$(date -d 2022-06-15T18:44:15,100+03:00 +%s.%N)
#C3=$(date -d 2022-06-15T18:44:55,100+03:00 +%s.%N)


C2O=$(echo "$C2 - $OUTER_OFFSET" | bc -l)
C2I=$(echo "$C2 + $INNER_OFFSET" | bc -l)
C3O=$(echo "$C3 + $OUTER_OFFSET" | bc -l)
C3I=$(echo "$C3 - $INNER_OFFSET" | bc -l)


# set camera configuration
SETUP

# baily beads
BURST $C2O $C2 1/8000           

# inner corona
AEB $C2 $C2I  1/1000 1 7 4 LTC 

# outer corona
AEB $C2I $C3I 1/8    1 7 4 LTC

# inner corona
AEB $C3I $C3  1/1000 1 7 4 ROT

# baily beads
BURST $C3 $C3O 1/8000           


echo "done"
