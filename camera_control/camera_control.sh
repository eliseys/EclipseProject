#!/bin/bash

gphoto2 \
    --set-config viewfinder=1 \
    --wait-event 1000ms \
    --set-config shutterspeed=1/250 \
    --set-config eosremoterelease=5 \
    --wait-event 950ms \
    --set-config eosremoterelease=4 \
    --set-config shutterspeed=0.5 \
    --set-config eosremoterelease=5 \
    --wait-event 10800ms \
    --set-config eosremoterelease=4 \
    --set-config shutterspeed=1/250 \
    --set-config eosremoterelease=5 \
    --wait-event 950ms \
    --set-config eosremoterelease=4 \
    --set-config shutterspeed=0.5 \
    --set-config eosremoterelease=5 \
    --wait-event 10800ms \
    --set-config viewfinder=0 \





    
    # --set-config eosremoterelease=4 \
    # --set-config shutterspeed=1/1000 \
    # --set-config eosremoterelease=5 \
    # --wait-event 800ms \
    # --set-config eosremoterelease=4 \
    # --set-config shutterspeed=1/1000 \
    # --set-config eosremoterelease=5 \
