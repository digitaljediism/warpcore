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
import itertools
import natsort

if len(sys.argv) != 4:
    print "usage: " + sys.argv[0] + " background_dir sample_dir sample_propability"
    sys.exit(255)

background_dir=sys.argv[1]
sample_dir=sys.argv[2]
sample_p = float(sys.argv[3])

background_samples = glob.glob(background_dir + "/*.ogg")

if len(background_samples) == 0:
    print "No background_samples found in " + background_dir
    sys.exit(253)

background_samples = natsort.natsorted(background_samples)
background_iterator = itertools.cycle(background_samples)

def update_samples(sample_dir):
    samples = glob.glob(sample_dir + "/*.ogg")
    if len(samples) == 0:
        print "No samples found in " + sample_dir
        sys.exit(254)

    random.shuffle(samples)
    return samples

mixer.init()
random.seed()

background_sound = mixer.Sound(background_iterator.next())
background_sound.set_volume(1.)
background_channel = background_sound.play()

samples = update_samples(sample_dir)

while True:
    if background_channel.get_queue() == None:
        background_channel.queue(mixer.Sound(background_iterator.next()))
    time.sleep(1)
    print it.next()

    if random.random() < sample_p:
        if len(samples) == 0:
            samples = update_samples(sample_dir)
        background_channel.queue(mixer.Sound(samples.pop()))
                
