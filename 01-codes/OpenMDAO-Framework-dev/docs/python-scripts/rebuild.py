#!/usr/local/bin/python

# This script will build .png versions of all of our Dia diagrams that
# have changed since the last time they were built.

import os.path
from os import system

from PIL import Image

from compmodtimes import compmodtimes
from dirwalk import includingWalk


def resize_image(fname, max_width=620):
    im = Image.open(fname)
    width, height = tuple(im.getbbox()[2:])
    print 'height =', height, ' width =', width
    if width > max_width:
        wrat = max_width / float(width)
        new_w = int(width * wrat)
        new_h = int(height * wrat)
        newim = im.transform((new_w, new_h), Image.EXTENT,
                             im.getbbox(), Image.BICUBIC)
        newim.save(fname)


# Convert dia files to png, and resize
for diafile in includingWalk("..", ["*.dia"]):
    pth = os.path.split(diafile)
    dest = pth[1].split('.')[0]
    retcode = compmodtimes(diafile, 'generated_images/' + dest + '.png')
    if retcode == -1 or retcode == 0:
        print 'generated_images/' + dest + '.png is up-to-date'
    else:
        cmd = 'dia --export=generated_images/' + dest + '.png --filter=png-libart ' + diafile
        system(cmd)
        resize_image(os.path.abspath(os.path.join('generated_images', dest + '.png')))

# Copy over any static images to the build area also
# for staticpic in includingWalk("images", ["*.png"]):
#   stp = os.path.split(staticpic)
#   justname = stp[1]
#   cmd2 = 'cp '+staticpic+' _build/html/images/'+justname
#   system(cmd2)
