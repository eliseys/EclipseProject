#!/bin/bash

# gphoto2 \
#     --set-config output=0 \
#     --set-config output=1 \
#     --set-config aeb=0 \
#     --set-config drivemode=1 \
#     --set-config shutterspeed=1/4000 \
#     --set-config eosremoterelease=5 \
#     --wait-event 4000ms \
#     --set-config eosremoterelease=4 \
#     --wait-event 1500ms \
#     --set-config aeb=3 \
#     --set-config shutterspeed=1/1000 \
#     --set-config eosremoterelease=5 \
#     --wait-event 2000ms \
#     --set-config eosremoterelease=4 \
#     --set-config shutterspeed=1/8 \
#     --set-config eosremoterelease=5 \
#     --wait-event 2000ms \
#     --set-config eosremoterelease=4 \
#     --set-config output=0 \


    
# gphoto2 \
#     --wait-event 1000ms \


gphoto2 \
    --set-config eosremoterelease=5 \
    --wait-event 300s \
    --set-config eosremoterelease=4 \


# gphoto2 \
#     --wait-event 1000ms \
