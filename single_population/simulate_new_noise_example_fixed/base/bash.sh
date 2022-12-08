#!/bin/bash

python split.py ${1}

perl guanrank.pl
perl guanrank_time.pl
perl prepare_train.pl
python train.py ${1}
cut -f 2-3 gs_test.dat >tmp.txt
paste tmp.txt prediction.dat >input.txt

R CMD BATCH test_cv.R

mv cIndex.txt cIndex.txt.${1}

mv prediction_time.dat prediction_time.dat.${1}

mv gs_test.dat gs_test.dat.${1}
