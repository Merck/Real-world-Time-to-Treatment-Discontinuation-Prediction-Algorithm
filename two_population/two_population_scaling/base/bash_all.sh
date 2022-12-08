#!/bin/bash
python simulate_train.py ${1} 0
python simulate_test.py ${2} 0
sh bash.sh 0


python simulate_train.py ${1} 1
python simulate_test.py ${2} 1
sh bash.sh 1

python simulate_train.py ${1} 2
python simulate_test.py ${2} 2
sh bash.sh 2

python simulate_train.py ${1} 3
python simulate_test.py ${2} 3
sh bash.sh 3

python simulate_train.py ${1} 4
python simulate_test.py ${2} 4
sh bash.sh 4




