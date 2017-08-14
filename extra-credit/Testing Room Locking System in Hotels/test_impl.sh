#!/bin/bash

pushd $1

test_folder="testing_impl"
if test -e $test_folder
then rm -rf $test_folder
fi

if test -e impl.py ; then
  mkdir $test_folder
  pushd $test_folder

  cp ../impl.py .
  cp ../../extra-credit-project/correct_tests.py .

  py.test -p no:django -v correct_tests.py > ./results.txt 2>&1

  popd
fi

popd
