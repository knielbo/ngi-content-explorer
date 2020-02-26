#!/usr/bin/env bash

# example of usage
start=`date +%s`
#echo pipeline init
#while true;do echo -n '>';sleep 1;done &

python qd-test.py --dataset ../dat/comments_MachineLearning --tag '["parent_id", "author", "created_utc", "body"]'

#kill $!; trap 'kill $!' SIGTERM
#echo
#echo ':)'

end=`date +%s`
runtime=$((end-start))
echo $runtime
