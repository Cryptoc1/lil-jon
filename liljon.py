#!/usr/bin/env python

##
#
# lil jon, it's like a magic8 ball, except for not really at all
# (c) Samuel Steele (cryptoc1)
#
##

import os, sys, wave, pyaudio, re, random

def main():
    sounds = get_sounds()
    sound = sounds[random.randrange(0, len(sounds) - 1, 1)]
    if not len(sys.argv) > 1:
        question = raw_input("Whatchu want ta know??\n\t:")
        yeeaahh(sound)
    elif len(sys.argv) > 1:
        yeeaahh(sound)
    else:
        print "Got, got, got an error!"

def get_sounds():
    sounds = []
    for sound in os.listdir('sounds'):
        if re.search(r'(.wav)', sound, re.M):
            sounds.append({"path": os.path.abspath('sounds/' + sound), "name": re.sub(r'[0-9.wav]', '', sound)})
    return sounds

def yeeaahh(sound):
    chunk = 1024
    f = wave.open(sound["path"], "rb")
    p = pyaudio.PyAudio()
    print sound["name"]
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()), channels=f.getnchannels(), rate=f.getframerate(), output=True) 
    data = f.readframes(chunk) 
    while data != '':  
        stream.write(data)  
        data = f.readframes(chunk)
    stream.stop_stream()  
    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()
