#!/usr/bin/env python

# The MIT License (MIT)

# Copyright (c) 2015 onlyjedis

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
from pygame import mixer
import random
import glob
import sys

if len(sys.argv) != 4:
    print "usage: " + sys.argv[0] + " background_file sample_file sample_propability"
    exit

background_noise=sys.argv[1]
sample_dir=sys.argv[2]
sample_p = float(sys.argv[3])

def update_samples(sample_dir):
    samples = glob.glob(sample_dir + "/*.ogg")
    random.shuffle(samples)
    return samples

mixer.init()

background_sound = mixer.Sound(background_noise)
background_sound.set_volume(1.)
background_channel = background_sound.play(-1)

samples = update_samples(sample_dir)

current_sound = None
current_channel = None

while True:
    time.sleep(1)
    if (not current_channel == None) and current_channel.get_busy():
        continue
    else:
        background_channel.unpause()
    if random.random() < sample_p:
        if len(samples) == 0:
            samples = update_samples(sample_dir)
        current_sound = mixer.Sound(samples.pop())
        current_sound.set_volume(1.)
        background_channel.pause()
        current_channel = current_sound.play(maxtime=10000)
    
