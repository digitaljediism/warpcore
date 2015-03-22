#!/usr/bin/env python

#Copyright (c) 2015, Florian Weik <florian@weltraumserver.net>
#All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
print background_sound
print background_sound.set_volume(1.)
background_channel = background_sound.play(-1)

samples = update_samples(sample_dir)

print samples
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
    
