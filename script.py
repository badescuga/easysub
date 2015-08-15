#from https://subliminal.readthedocs.org/en/latest/user/usage.html#cli

from __future__ import unicode_literals
import os
from babelfish import *
from subliminal import *
import urlparse
import os.path
import sys
import xmlrpc_client

print len(sys.argv)
if len(sys.argv) > 1:
	moviePath = sys.argv[1]
else:
	moviePath = "/Users/badescuga/Downloads/Rick.and.Morty.S02E02.HDTV.x264-BATV.mp4"
print "eeee"

movieName = os.path.basename(urlparse.urlsplit(moviePath).path)
video = Video.fromname(movieName)
print video
print video.video_codec
print video.release_group

my_region = region.configure('dogpile.cache.memory')

best_subtitles = download_best_subtitles([video], {Language('eng')}, providers=['podnapisi'])
best_subtitles[video]
best_subtitle = best_subtitles[video][0]

#save subtitle

subPath = os.path.splitext(moviePath)[0] + ".srt"
print subPath
file_ = open(subPath, 'w')
file_.write(best_subtitle.content)
file_.close()


#print best_subtitle.content.split(b'\n')[2]

#os.system("alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'")
os.system("/Applications/VLC.app/Contents/MacOS/VLC " + moviePath + " --sub-file "+subPath)
