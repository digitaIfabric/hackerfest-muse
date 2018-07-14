### hackerfest-muse
# The Sonification of Brainwaves using Muse-IO, Python-OSC, SuperCollider, and Ableton Live

# Developers
[!David Wawryko](https://github.com/digitalfabric92)
[!Jean-Christophe Buteau](https://github.com/trotrem)

#  Muse Tools use Open Sound Control (OSC) to pass data around. OSC is a simple protocol for sending data over a network. It was originally intended as a successor to MIDI, the well-known protocol for controlling electronic instruments, but it turns out to be really useful for all sorts of things, including Muse data.

# STEP 1
### Connect to MUSE headset via Bluetooth and initiate a UDP session on port 5000
muse-io --device Muse-6F35 --osc osc.udp://localhost:5002
### Replace Muse-6F35 with the name of your device

# STEP 2
### Run the sonification.py, you might need to install the python dependencies first using PIP3 (python-osc, numpy, etc)
python3 sonification.py

# STEP 3
Install SuperCollider, Boot the server under the language menu and execute synth-3.scd

# STEP 4
Route 

RESSOURCES
https://github.com/ShaPOC/node-muse
https://en.wikipedia.org/wiki/Piano_key_frequencies
