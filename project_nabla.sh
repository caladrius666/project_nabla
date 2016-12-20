#!/bin/bash
for input in $1 $2 $3 $4
do
flag=no
for option in -ax -hg -sp -sa --show_approx --axis --hide_grid --show_podgon
do
if [ "$option" = "$input" ]
then
flag=yes
fi
done
if [ "$flag" = no ]
then
echo Шо вы несёте?
exit
fi
done
if [ "$5" != '' ]
then
echo Что вы задумали?
exit
fi
echo project_nabla активирован!!!
python3 <project_nabla path>/main.py <path to input> $1 $2 $3 $4
echo Готово!


