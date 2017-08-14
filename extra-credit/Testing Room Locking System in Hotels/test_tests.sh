#!/bin/bash

pushd $1

test_folder="testing_tests"
if test -e $test_folder
then rm -rf $test_folder
fi

if test -e test_impl.py ; then
  mkdir $test_folder
  pushd $test_folder

  cp ../test_impl.py .
  cp ../../extra-credit-project/*correct_impl*py .

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
      py.test -p no:django test_impl.py >> $j 2>&1
      grep -q "Unsatisfiable" $j
      if [ $? -eq 1 ]
      then break
      else echo "  Rexecuting" ; rm $j 
      fi
    done
  done

  grep -E "test_impl.py " out*txt | sed "s/\(.*\):\(.*\)/\2 \1/g" > ./results.txt 

  popd
fi

popd
