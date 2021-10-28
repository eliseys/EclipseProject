#!/bin/bash



c2="18:46:05.5"

echo $c2

# while [ "$c2" != "$t" ]; do
#     t=$(date +%T)
#     echo -ne "\t time" $t
#     #echo -ne "\e[0K\r"
    
#     echo -ne "\r"
#     sleep 0.1
# done

while [ "$c2" != "$t" ]; do
    t=$(date +%T.%1N)
    echo -n $t
    echo -ne "\r"
done



# end=$((SECONDS+3))

# while [ $SECONDS -lt $end ]; do
#     #echo $SECONDS
#     :
# done


# gphoto2 \
#     --camera='Canon EOS 7D MarkII' --set-config viewfinder=1 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1000ms \
#     --camera='Canon EOS 7D MarkII' --set-config drivemode=2 \
#     --camera='Canon EOS 7D MarkII' --set-config shutterspeed=1/1000 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \
#     --camera='Canon EOS 7D MarkII' --wait-event 1300ms \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=4 \
#     --camera='Canon EOS 7D MarkII' --set-config eosremoterelease=5 \    
