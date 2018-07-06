#!/bin/bash
fileline=`tail -n 1 /var/log/img.log|awk -F '/' '{print $3}'`
git add /img/$fileline >/dev/null
git commit -a -m 'add $fileline' >/dev/null
git push origin master >/dev/null
echo https://raw.githubusercontent.com/ananzhoujiaan/img/master/$fileline
