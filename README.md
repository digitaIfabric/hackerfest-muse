## Hackerfest 2018 - NEUROTECHX - Muse
## The Sonification of EEG data using Muse-IO, Python-OSC, SuperCollider, and Ableton Live

![image](https://github.com/digitalfabric92/hackerfest-muse/raw/master/muse-final.png)

## Developers
[Jean-Christophe Buteau](https://github.com/trotrem)

[David Wawryko](https://github.com/digitalfabric92)

[Kamy Moussavi](https://github.com/ogKamy)

#####  Muse Tools use Open Sound Control (OSC) to pass data around. OSC is a simple protocol for sending data over a network. It was originally intended as a successor to MIDI, the well-known protocol for controlling electronic instruments, but it turns out to be really useful for all sorts of things, including Muse data. We chose to develop a realtime sonification of this Muse data using existing music creation tools to inspire future musical instruments developed on the web.

## STEP 1
#### Connect to a Muse headset via Bluetooth and initiate a UDP session on port 5000
`muse-io --device Muse-6F35 --osc osc.udp://localhost:5000
#### Replace Muse-6F35 with the name of your device (visible on the headset/bluetooth settings). You can install MuseLab or other research tools from online http://developer.choosemuse.com/sdk/android/android-api-reference

## STEP 2
#### Run the sonification.py OSC script locally
`python3 sonification.py`
#### You might need to install the python dependencies first using PIP3 (python-osc, numpy, etc)

## STEP 3
Install SuperCollider, Launch the audio server under the language menu and execute synth-3.scd in the IDE.

## STEP 4
Route the audio from SuperCollider through Soundflower to Ableton Live 9 for Recording and control.

## Requirements
Muse headset (2014 edition used)
Ableton Live 9
Python
SuperCollider

RESSOURCES
https://en.wikipedia.org/wiki/Piano_key_frequencies
