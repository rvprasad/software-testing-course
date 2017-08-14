#!/bin/bash

timeout=180

j="out-posted-coverage-1.txt"
rm $j
cp incorrect_bst_edge_case1_posted.py impl.py
py.test --cov-fail-under=100 --cov=. --cov-report=term-missing -s \
    --cov-config=coverage.rc --timeout=$timeout \
    --timeout_method=thread test_impl.py >> $j 2>&1

j="out-posted-coverage-2.txt"
rm $j
py.test --cov-fail-under=100 --cov=. --cov-report=term-missing -s \
    --cov-config=coverage.rc --timeout=$timeout \
    --timeout_method=thread test_impl.py >> $j 2>&1

j="out-posted-coverage-3.txt"
rm $j
py.test --cov-fail-under=100 --cov=. --cov-report=term-missing -s \
    --cov-config=coverage.rc --timeout=$timeout \
    --timeout_method=thread test_impl.py >> $j 2>&1

for i in `ls -1 *correct_*.py`; do 
  echo $i
  j="out-${i%.py}.txt"
  if test -f $j; then
    rm $j
  fi 

  echo "########################################" >> $j
  echo $i >> $j
  cp $i impl.py
  py.test -p no:django test_impl.py >> $j 2>&1
done

grep -E "test_impl.py |^impl.py " out*txt | grep -v "example" | sed "s/\(.*\):\(.*\)/\2 \1/g"

#for i in `ls -1 impl-*.py`; do 
#  echo "########################################" >> out.txt
#  echo $i >> out.txt
#  cp $i impl.py
#  nosetests-3.4 >> out.txt 2>&1
#done
