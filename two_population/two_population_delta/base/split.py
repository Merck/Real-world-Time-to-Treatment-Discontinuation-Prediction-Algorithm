
import random
import sys

random.seed(sys.argv[1])

#death_status.txt  feature.txt  observation_date.txt

STATUS=open('death_status.txt','r')
FEATURE=open('feature.txt','r')
OBSERVATION=open('observation_date.txt','r')
GS=open('gs_train.dat','w')
GS_val=open('gs_val.dat','w')
GS_test=open('gs_test.dat','w')
NEW_FEATURE=open('new_feature.dat','w')

pid=0
for status in STATUS:
    feature=FEATURE.readline()
    observation=OBSERVATION.readline()

    status=status.rstrip()
    feature=feature.rstrip()
    observation=observation.rstrip()

    rrr=random.random()
    if (rrr<0.75):
        GS.write('Patient_'+str(pid)+'\t'+observation+'\t'+status+'\n')
    else:
        GS_val.write('Patient_'+str(pid)+'\t'+observation+'\t'+status+'\n')

    NEW_FEATURE.write('Patient_'+str(pid)+'\t'+feature.replace(' ','\t')+'\n')
    pid=pid+1




STATUS=open('test_death_status.txt','r')
FEATURE=open('test_feature.txt','r')
OBSERVATION=open('test_observation_date.txt','r')
GS_test=open('gs_test.dat','w')
pid=0
for status in STATUS:
    feature=FEATURE.readline()
    observation=OBSERVATION.readline()

    status=status.rstrip()
    feature=feature.rstrip()
    observation=observation.rstrip()

    GS_test.write('Patient_'+str(pid)+'\t'+observation+'\t'+status+'\n')
    NEW_FEATURE.write('Patient_'+str(pid)+'\t'+feature.replace(' ','\t')+'\n')

    pid=pid+1




