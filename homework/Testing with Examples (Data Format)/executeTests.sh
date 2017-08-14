#!/bin/bash

if test -f out.txt; then
  rm out.txt
fi 

for i in `ls -1 impl-*.py`; do 
  j="out-${i%.py}.txt"
  echo "########################################" >> $j
  echo $i >> $j
  cp $i impl.py
  nosetests-3.4 >> $j 2>&1
done

#for i in `ls -1 impl-*.py`; do 
#  echo "########################################" >> out.txt
#  echo $i >> out.txt
#  cp $i impl.py
#  nosetests-3.4 >> out.txt 2>&1
#done
