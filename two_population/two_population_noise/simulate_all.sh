#!/bin/bash


for noise in 0.01 0.05 0.1 0.5 1 5 10 50 100
do
    for noise_test in 0.01 0.05 0.1 0.5 1 5 10 50 100
        do
            cp -rf base code_${noise}_${noise_test}

            cd code_${noise}_${noise_test}
            sh bash_all.sh ${noise} ${noise_test} &
            cd ../
    done

done
