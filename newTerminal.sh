#!/bin/sh
osascript -e "tell application \"Terminal\" to do script \"python /Users/badescuga/easysub/script.py $1 && exit\"" > /dev/null 