#!/bin/bash


for delta in 0.0002 0.0004 0.0006 0.0008 0.001 0.0012
do
        cp -rf base code_${delta}

        cd code_${delta}
        sh bash_all.sh ${delta} &
        cd ../

done
