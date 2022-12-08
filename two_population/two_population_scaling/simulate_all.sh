#!/bin/bash


for delta in 1 2 10 20 100 200 1000 2000
do
    for delta_test in 1 2 10 20 100 200 1000 2000
        do
            cp -rf base code_${delta}_${delta_test}

            cd code_${delta}_${delta_test}
            sh bash_all.sh ${delta} ${delta_test} &
            cd ../
    done

done
