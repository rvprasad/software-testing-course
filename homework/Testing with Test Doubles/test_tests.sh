#!/bin/bash

function output () {
  o1=`grep -c "def $2(" pytest-output.txt`  
  o2=''
  if [[ $1 == $2 ]]
  then o2='*'
  fi
  or="$o1$o2"
}

for i in `ls -1 authentication_component_impl_*py` ; do 
  cp $i temp/authentication_component_impl.py 
  pushd temp > /dev/null 
  pytest test_impl.py -v > pytest-output.txt
#i="impl_fail-friends_of_friends-raises_wrong_exception_for_non_string_name.py"
  j="$i" 
  tmp1=`grep -c 'test_.*FAILED$' pytest-output.txt`
  j="$j F$tmp1"
  tmp1=`grep -c 'test_.*ERROR$' pytest-output.txt`
  j="$j E$tmp1"
  k=`echo $i | cut -d'-' -f2`
  for l in "create_user" "login_user" "change_password" "rename_user" ; do 
    output $k $l
    j="$j $or"
  done
  echo $j
  mv pytest-output.txt pytest-output-$i.txt
  popd > /dev/null 
done

echo "The columns are correspond to the following methods: create_user login_user change_password rename_user"

pushd temp > /dev/null
grep "test_.*\(FAILED\|ERROR\)$" pytest-output-authen* | sed -E "s/pytest-output-authentication_component_(.*).py.txt:test_impl.py::([^\[]*)(\[.*\])? (.*)/\2 \4 \1/" | sort -u > _temp1_

grep "test_.*\(FAILED\|ERROR\)$" pytest-output-authen* | sed -E "s/pytest-output-authentication_component_(.*).py.txt:test_impl.py::([^\[]*)(\[.*\])? (.*)/\1 \4 \2/" | sort -u > _temp2_

k="" 
while read i ; do 
  j=`echo $i | cut -f1 -d' '` 
  if [[ "$k" != "$j" ]] 
  then 
    echo "---------" 
    k=$j 
  fi 
  echo $i
done < _temp1_ > tests-vs-impl.txt
rm _temp1_

k="" 
while read i ; do 
  j=`echo $i | cut -f1 -d' '` 
  if [[ "$k" != "$j" ]] 
  then 
    echo "---------" 
    k=$j 
  fi 
  echo $i
done < _temp2_ > impl-vs-tests.txt
rm _temp2_

tests_to_exclude=`grep "pass-" impl-vs-tests.txt | sed -E "s/.* .* (.*)/\1/"`
cp tests-vs-impl.txt _temp1_
for i in $tests_to_exclude ; do
  fgrep -v "$i" _temp1_ > _temp2_
  cp _temp2_ _temp1_
done
uniq _temp1_ > tests-to-consider-vs-impl.txt
rm _temp?_
popd > /dev/null

