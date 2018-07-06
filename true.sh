#!/bin/bash
fileline=`tail -n 1 /var/log/img.log|awk -F '/' '{print $3}'`
git add /img/$fileline
git commit -a -m 'add $fileline'
git push origin master
echo https://raw.githubusercontent.com/ananzhoujiaan/img/master/$fileline
