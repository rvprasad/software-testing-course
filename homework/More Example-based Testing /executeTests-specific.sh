#!/bin/bash

for i in correct_impl.py incorrect_impl_ec_empty_graph.py incorrect_impl_ec_invalid_edges.py ; do 
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
    py.test -p no:django test_impl.py >> $j 2>&1
    grep -q "Unsatisfiable" $j
    if [ $? -eq 1 ]
    then break
    else echo "  Rexecuting" ; rm $j 
    fi
  done
done

grep -E "test_impl.py " out*txt | sed "s/\(.*\):\(.*\)/\2 \1/g"

#for i in `ls -1 impl-*.py`; do 
#  echo "########################################" >> out.txt
#  echo $i >> out.txt
#  cp $i impl.py
#  nosetests-3.4 >> out.txt 2>&1
#done
