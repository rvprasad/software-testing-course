#!/bin/bash


if test -e $1/testing_tests ; then
  pushd $1/testing_tests
  i=`grep "test_impl.py:\d\+: \(AssertionError\|Failed\)" out*txt -c | grep -v -c ":0"`
  j=`grep "test_impl.py:\d\+: \(AssertionError\|Failed\)" out*txt -c | grep -c ":0"`
  echo "$i faulty implementations were flagged while $j faulty implementations were not flagged" 
  popd
fi
