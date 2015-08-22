#from https://subliminal.readthedocs.org/en/latest/user/usage.html#cli

from __future__ import unicode_literals
import os
from babelfish import *
from subliminal import *
import urlparse
import os.path
import sys

#print len(sys.argv)

if len(sys.argv) > 1:
	moviePath = sys.argv[1]
	print"found movie path! "+moviePath 
else:
	moviePath = "/Users/badescuga/Downloads/Rick.and.Morty.S02E03.Auto.Erotic.Assimilation.720p.WEBRip.AAC2.0.H.264-Phr0stY.mkv"
	print "no path found.. using test one"


movieName = os.path.basename(urlparse.urlsplit(moviePath).path)
video = Video.fromname(movieName)
print video
#print video.video_codec
#print video.release_group

my_region = region.configure('dogpile.cache.memory')

print 'started downloading subs..'
best_subtitles = download_best_subtitles([video], {Language('eng')}, providers=None)
#print best_subtitles[video]
print 'number of best subtitles: ' + str(len(best_subtitles)) 
#print len(best_subtitles[video])
best_subtitle = best_subtitles[video][0]

#save subtitle

#subPath = os.path.splitext(moviePath)[0] + ".srt"

parentFolderPath = os.path.abspath(os.path.join(moviePath, os.pardir))

##check if /subs/ dir exists and create it if not
subsFolderPath = parentFolderPath+'/subs/'
if not os.path.exists(subsFolderPath):
    os.makedirs(subsFolderPath)

subPath = subsFolderPath+movieName + '.srt'

print subPath

file_ = open(subPath, 'w')
file_.write(best_subtitle.content)
file_.close()


#print best_subtitle.content.split(b'\n')[2]

#os.system("alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'")
os.system("/Applications/VLC.app/Contents/MacOS/VLC " + moviePath + " --sub-file "+subPath +" &")
print 'exiting..'
exit(0)


