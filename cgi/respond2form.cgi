#!/bin/bash
#Alex Gramsky
#2nd cgi file for website
#file respond2form.cgi

echo 'Content-type: text/html'
echo ''

echo '<html>'
echo ''

#Getting the QUERY_STRING and setting the deliminators to &
list=`echo $QUERY_STRING | awk -F'&' '{print $1}' |\
sed 's/countriesList=//g' | sed "s/+/ /g;s/%27/\'/g;s/%28/\(/g;s/%29/\)/g"`
#Seding out the countries list, and replacing any %20 or such characters with
#Ascii characters

#Variable for the $worldFile file
worldFile="world95.txt"

echo '<body>'
echo '<hr>'
echo '<h2>The country you have selected is '"$list"'</h2>'

#Extract data from the QUERY_STRING from each line.
query=`echo $QUERY_STRING | sed 's/.*List=[^&]*&//'`

#Variables for the major headers, used in an awk statement to get info
list1="@$list:Communications"
list2="@$list:Defense Forces"
list3="@$list:Economy"
list4="@$list:Geography"
list5="@$list:People"
list6="@$list:Government"
list7="@$list:Transportation"

#Research into a loop to compact this. No luck so far.
#cntryArr=($(grep -o "@[A-Z].*:" $worldFile | sort -u | sed "1d" |
# sed "s/@//g;s/://g;s/ /_/g;s/%27/\'/g;s/%28/\(/g;s/%29/\)/g" |
#while read line ; do echo "$line" ; done ))

#This loop gets the boxvals out of the QUERY_STRING
#And also sets each checked box to "on"
for((i = 1; i <= 90; i++)) ;do
 echo $query | grep "boxval$i=" > /dev/null
  if [ "$?" = "0" ] ; then
   eval boxval$i=`echo $query | sed 's/boxval'"$i"'=\([^\&]*\).*/\1/'`
   query=`echo $query | sed 's/boxval'"$i"'=[^\&]*\&//'`
else
   eval boxval$i="off"
 fi
done

query2=`echo $QUERY_STRING | sed 's/.*List=[^&]*&//;s/=on/ /g;s/&//g'`
echo "$query2"
for ((j = 1; j <=90; j++)) ; do
 if [ "boxval$j" = "on" ] ; then
  getData=
  getData2=
  test1=`awk '/'"$getData"'/,/'"$getData2"'/{print $0}' $worldFile`
  echo "$test1"
  echo "<hr>"
 fi
done


























echo '</body>'
echo '</html>'

