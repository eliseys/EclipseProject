#!/bin/bash

if [ $ARGUMENT ]; then
    if [[ $ARGUMENT =~ .+\.[jpg|JPG] ]]
    then
    # Then next few lines are optional
    # Alternatively pass $ARGUMENT directly to your image viewer eg:-
    # /usr/bin/shotwell "$ARGUMENT" &
    DIRNAME=$(dirname "$ARGUMENT")
    BASENAME=$(basename "$ARGUMENT")
    NEWFILENAME="$DIRNAME/my_new_folder/$BASENAME"
    mv "$ARGUMENT" "$NEWFILENAME"
            /usr/bin/shotwell "$NEWFILENAME" &
    fi
fi
