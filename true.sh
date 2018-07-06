#!/bin/bash
fileline=`tail -n 1 /var/log/img.log|awk -F '/' '{print $3}'`
git add /img/$fileline >/dev/null 2>&1
git commit -a -m 'add $fileline' >/dev/null 2>&1
git push origin master >/dev/null 2>&1
echo https://raw.githubusercontent.com/ananzhoujiaan/img/master/$fileline
