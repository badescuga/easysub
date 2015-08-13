#from https://subliminal.readthedocs.org/en/latest/user/usage.html#cli

from __future__ import unicode_literals
import os
from babelfish import *
from subliminal import *

video = Video.fromname('The.Big.Bang.Theory.S05E18.HDTV.x264-LOL.mp4')
print video
print video.video_codec
print video.release_group

my_region = region.configure('dogpile.cache.memory')

best_subtitles = download_best_subtitles([video], {Language('eng')}, providers=['podnapisi'])
best_subtitles[video]
best_subtitle = best_subtitles[video][0]
print best_subtitle.content.split(b'\n')[2]