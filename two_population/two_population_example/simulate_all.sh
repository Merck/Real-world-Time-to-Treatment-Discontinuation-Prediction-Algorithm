#!/bin/bash


for numberexample in 100 500 1000 5000 10000
do
    for numberexample_test in 100 500 1000 5000 10000
        do
            cp -rf base code_${numberexample}_${numberexample_test}

            cd code_${numberexample}_${numberexample_test}
            sh bash_all.sh ${numberexample} ${numberexample_test} &
            cd ../
    done

done
