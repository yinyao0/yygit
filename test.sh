#!/bin/sh
cat trs.log|grep WEB-RELEASE|grep user|grep modules|grep -v err > 1
cat trs.log|grep ICAFE|grep pid|grep qas|grep -v receive > 2
cat trs.log|grep ICAFE|grep modules > 3
python test1.py > r1
python test2.py > r2
python test3.py > r4
a=$1
b=$2
python test4.py $a $b
