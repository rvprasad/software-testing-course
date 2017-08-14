#!/bin/bash

p=0
for i in `ls -1 src/impl_pass*py` ; do 
  cp $i src/impl.py
  behave > pass.txt
  c=`egrep -c "[1-9]+ features? passed, 0 failed" pass.txt`
  p=$(( $p + $c ))
  if [ $c -eq 0 ] ; then
    echo "$i incorrectly failed some features" | \
      sed -e "s/src\///g" 
  fi
  rm pass.txt
done

f=0
for i in `ls src/impl_fail*py` ; do 
  cp $i src/impl.py
  behave > fail.txt
  c=`egrep -c "features? passed, [1-9]+ failed" fail.txt`
  f=$(( $f + $c ))
  if [ $c -eq 0 ] ; then
    echo "$i incorrectly satisfied all features" | \
      sed -e "s/src\///g" 
  fi
  rm fail.txt
done

pcnt=`ls -1 src/impl_pass*py | wc -l | sed -e "s/ //g"`
echo "$p of $pcnt correct implementations satisfied all scenarios"
fcnt=`ls -1 src/impl_fail*py | wc -l | sed -e "s/ //g"`
echo "$f of $fcnt incorrect implementations failed some scenario"

d=`ls -1 src/impl_* | wc -l`
s=`echo "($f + $p) / $d * 10" | bc -l`
echo "Score: ${s:0:4} out of 10"
