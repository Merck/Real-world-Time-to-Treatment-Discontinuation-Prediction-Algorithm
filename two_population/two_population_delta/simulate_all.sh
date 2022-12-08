#!/bin/bash


for delta in 0.0002 0.0004 0.0006 0.0008 0.0010 0.0012
do
    for delta_test in 0.0002 0.0004 0.0006 0.0008 0.0010 0.0012
        do
            cp -rf base code_${delta}_${delta_test}

            cd code_${delta}_${delta_test}
            sh bash_all.sh ${delta} ${delta_test} &
            cd ../
    done

done
