#!/bin/bash
python simulate_train.py ${1} ${2} 0
python simulate_test.py ${2} ${1} 0
sh bash.sh 0


python simulate_train.py ${1} ${2} 1
python simulate_test.py ${2} ${1} 1
sh bash.sh 1

python simulate_train.py ${1} ${2} 2
python simulate_test.py ${2} ${1} 2
sh bash.sh 2

python simulate_train.py ${1} ${2} 3
python simulate_test.py ${2} ${1} 3
sh bash.sh 3

python simulate_train.py ${1} ${2} 4
python simulate_test.py ${2} ${1} 4
sh bash.sh 4




