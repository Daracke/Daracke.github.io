#!/bin/bash
echo "Content-type: text/html"
echo ""

countries=`grep -o "@[A-Z].*:" world95.txt | sort -u | sed "1d" \
| sed 's/@//g;s/://g'`

#majorheads=`grep -o "@[A-Z].*:.*" world95.txt | sed 's/@.*://g;s/Defense Forces/Defense_Forces/g' | sort -u`
#echo "$majorheads"

declare -a majorheads=('@Afghanistan:Geography' '@Afghanistan:People' '@Afghanistan:Government' '@Afghanistan:Economy' '@Afghanistan:Transportation' '@Afghanistan:Communications' '@Afghanistan:Defense Forces' '_')
#list1="@Afghanistan:Geography"
#list2="@Afghanistan:People"
#list3="@Afghanistan:Government"
#list4="@Afghanistan:Economy"
#list5="@Afghanistan:Transportation"
#list6="@Afghanistan:Communications"
#list7="@Afghanistan:Defense Forces"

#Counter for boxvals
i=`cat counter.txt`
b=16
c=32
d=56
e=76
f=83
g=87
echo "$i"
worldFile="world95.txt"
echo '<form method=get action="respond2form.cgi">'
echo "<h2>Select a Nation</h2>"
echo '<select name="countriesList">'
echo "$countries" | while read line; do
echo '<option>'$line'</option>'
done
echo '</select>'
echo '<br></br>'


echo '<h2>Select Heading(s) and/or Subcatagorie(s)</h2>'
c1=0
c2=1
 for ((z = 1; z <=7; z++)) ;do
	chkbx=`awk '/'"${majorheads[$c1]}"'/,/'"${majorheads[$c2]}"'/ {print $0}' $worldFile \
| sed 's/@.*://g;s/'"${majorheads[$c2]}"'//g' | grep -o "[A-Z].*:" | sed 's/://g'`
	var=`echo "${majorheads[$c1]}" | sed 's/@.*://g;'`
	((c1=c1+1))
	((c2=c2+1))
   echo "$var" | while read line; do
   echo '<table cellpadding="1" cellspacing="2">'
   echo    '<tr>'
   echo    "<td><strong><input type="checkbox" name="boxval"$((i++))"" size=30>"$var"</strong></td>"
   echo    '</tr>'
   echo    '<tr>'
echo "$i" > counter.txt
   echo "$chkbx" | while read line; do
   echo    "<td><input type="checkbox" name="boxval""$((i++))" size=30>"$line"</td>"
	
			if (("$i" % 6 == "0"  )) ; then
         		 echo '</tr>'
         		 echo '<tr>'
			fi       	
		   done	
echo "$i"	        
		done

echo    '</tr>'
echo    '</table>'
echo '<br>'
 done
#chkbx2=`awk '/'"$list2"'/,/'"$list3"'/ {print $0}' $worldFile \
#| sed 's/@.*://g;s/'"$list3"'//g' | grep -o "[A-Z].*:" | sed 's/://g'`
#var2=`echo "$list2" | sed 's/@.*://g;'`
#echo "$var2" | while read line; do
#echo '<table cellpadding="1" cellspacing="2">'
#echo    '<tr>'
#echo    "<td><strong><input type="checkbox" name="boxval"$((b))"" size=30>"$var2"</strong></td>"
#echo    '</tr>'
#done
#echo    '<tr>'
#echo "$chkbx2" | while read line; do
#echo    "<td><input type="checkbox" name="boxval""$((++b))" size=30>"$line"</td>"
#        if (("$b" % 6 == "0"  )) ; then
#         echo '</tr>'
#         echo '<tr>'
#        fi
#done
#echo    '</tr>'
#echo    '</table>'
#echo '<br>'

#chkbx3=`awk '/'"$list3"'/,/'"$list4"'/ {print $0}' $worldFile \
#| sed 's/@.*://g;s/'"$list5"'//g' | grep -o "[A-Z].*:" | sed 's/://g'`
#var3=`echo "$list3" | sed 's/@.*://g;'`
#echo "$var3" | while read line; do
#echo '<table cellpadding="1" cellspacing="2">'
#echo    '<tr>'
#echo    "<td><strong><input type="checkbox" name="boxval"$((c))"" size=30>"$var3"</strong></td>"
#echo    '</tr>'
#done
#echo    '<tr>'
#echo "$chkbx3" | while read line; do
#echo    "<td><input type="checkbox" name="boxval""$((++c))" size=30>"$line"</td>"
#	if (("$c" % 6 == "0"  )) ; then
#	 echo '</tr>'
#	 echo '<tr>'
#	fi
#done
#echo    '</tr>'
#echo    '</table>'
#echo '<br>'

#chkbx4=`awk '/'"$list4"'/,/'"$list5"'/ {print $0}' $worldFile \
#| sed 's/@.*://g;s/'"$list5"'//g' | grep -o "[A-Z].*:" | sed 's/://g'`
#var4=`echo "$list4" | sed 's/@.*://g;'`
#echo "$var4" | while read line; do
#echo '<table cellpadding="1" cellspacing="2">'
#echo    '<tr>'
#echo    "<td><strong><input type="checkbox" name="boxval"$((d))"" size=30>"$var4"</strong></td>"
#echo    '</tr>'
#done
#echo    '<tr>'
#echo "$chkbx4" | while read line; do
#echo    "<td><input type="checkbox" name="boxval""$((++d))" size=30>"$line"</td>"
#        if (("$d" % 6 == "0"  )) ; then
#         echo '</tr>'
#         echo '<tr>'
#        fi
#done
#echo    '</tr>'
#echo    '</table>'
#echo '<br>'

#chkbx5=`awk '/'"$list5"'/,/'"$list6"'/ {print $0}' $worldFile \
#| sed 's/@.*://g;s/'"$list6"'//g' | grep -o "[A-Z].*:" | sed 's/://g'`
#var5=`echo "$list5" | sed 's/@.*://g;'`
#echo "$var5" | while read line; do
#echo '<table cellpadding="1" cellspacing="2">'
#echo    '<tr>'
#echo    "<td><strong><input type="checkbox" name="boxval"$((e))"" size=30>"$var5"</strong></td>"
#echo    '</tr>'
#done
#echo    '<tr>'
#echo "$chkbx5" | while read line; do
#echo    "<td><input type="checkbox" name="boxval""$((++e))" size=30>"$line"</td>"
#        if (("$e" % 5 == "0"  )) ; then
#         echo '</tr>'
#         echo '<tr>'
#        fi
#done
#echo    '</tr>'
#echo    '</table>'
#echo '<br>'

#chkbx6=`awk '/'"$list6"'/,/'"$list7"'/ {print $0}' $worldFile \
#| sed 's/@.*://g;s/'"$list7"'//g' | grep -o "[A-Z].*:" | sed 's/://g'`
#var6=`echo "$list6" | sed 's/@.*://g;'`
#echo "$var6" | while read line; do
#echo '<table cellpadding="1" cellspacing="2">'
#echo    '<tr>'
#echo    "<td><strong><input type="checkbox" name="boxval"$((f))"" size=30>"$var6"</strong></td>"
#echo    '</tr>'
#done
#echo '<tr>'
#echo "$chkbx6" | while read line; do
#echo    "<td><input type="checkbox" name="boxval""$((++f))" size=30>"$line"</td>"
#        if (("$f" % 8 == "0"  )) ; then
#         echo '</tr>'
#         echo '<tr>'
#        fi
#done
#echo    '</tr>'
#echo    '</table>'
#echo '<br>'

#chkbx7=`awk '/'"$list7"'/,/_/ {print $0}' $worldFile \
#| sed 's/@.*://g;s/_//g' | grep -o "[A-Z].*:" | sed 's/://g'`
#var7=`echo "$list7" | sed 's/@.*://g;'`
#echo "$var7" | while read line; do
#echo '<table cellpadding="1" cellspacing="2">'
#echo    '<tr>'
#echo    "<td><strong><input type="checkbox" name="boxval"$((g))"" size=30>"$var7"</strong></td>"
#echo '</tr>'
#done
#echo '<tr>'
#echo "$chkbx7" | while read line; do
#echo    "<td><input type="checkbox" name="boxval""$((++g))" size=30>"$line"</td>"
#        if (("$g" % 3 == "0"  )) ; then
#         echo '</tr>'
#         echo '<tr>'
#        fi
#done
#echo '</tr>'
#echo '</table>'
echo '<input type ="submit" value ="Fetch Data">'
echo '<input type ="reset" value ="Clear Form">'
echo '</form>'
