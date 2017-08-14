#!/bin/bash

for i in `ls -1 *impl_*.py`; do 
  echo $i
  j="out-${i%.py}.txt"
  if test -f $j; then
    rm $j
  fi 

  echo "########################################" >> $j
  echo $i >> $j
  cp $i impl.py
  py.test -p no:django --timeout=3 --timeout-method=thread >> $j 2>&1
done

grep "test_impl.py " *txt | sed "s/\(.*\):\(.*\)/\2 \1/g"

#for i in `ls -1 impl-*.py`; do 
#  echo "########################################" >> out.txt
#  echo $i >> out.txt
#  cp $i impl.py
#  nosetests-3.4 >> out.txt 2>&1
#done
