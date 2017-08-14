#!/bin/bash

for i in `ls -1 impl_*.py`; do 
  echo $i
  j="out-${i%.py}.txt"
  if test -f $j; then
    rm $j
  fi 

  echo "########################################" >> $j
  echo $i >> $j
  cp $i impl.py
  py.test -v --timeout=3 --timeout-method=thread >> $j 2>&1
done

if [ -e out_matrix.txt ] ; then
  rm out_matrix.txt
fi

for i in `ls out-impl_*` ; do 
  t=`grep "test_stack.py::test" $i | sort | \
    sed -E -e "s/.* (.*)/\1/g" -e 's/PASSED/./g' -e 's/(FAILED)|(ERROR)/F/g' | \
    tr '\n' ' ' | sed -e 's/ //g'`
  echo "$t $i" >> out_matrix.txt
done


python evaluate_out_matrix.py

rm out_matrix.txt
