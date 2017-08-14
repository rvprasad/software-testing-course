#!/bin/bash

echo "Command line arguments will be passed on to py.test"

for i in `ls -1 *correct_impl*.py`; do 
  echo $i
  j="out-${i%.py}.txt"
  if test -f $j; then
    rm $j
  fi 

  cp $i impl.py

  while :
  do 
    echo "########################################" > $j
    echo $i >> $j
    py.test -p no:django correct_tests.py $* >> $j 2>&1
    grep -q "Unsatisfiable" $j
    if [ $? -eq 1 ]
    then break
    else echo "  Rexecuting" ; rm $j 
    fi
  done
done

grep -E "correct_tests.py " out*txt | sed "s/\(.*\):\(.*\)/\2 \1/g" > test_testing.txt

#for i in `ls -1 impl-*.py`; do 
#  echo "########################################" >> out.txt
#  echo $i >> out.txt
#  cp $i impl.py
#  nosetests-3.4 >> out.txt 2>&1
#done
