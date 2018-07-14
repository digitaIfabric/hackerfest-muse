#!/usr/bin/env python

import argparse
import math
import numpy
import time
import random

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 57120)

class timer:
    def __init__(self):
        self.timer = time.time()
        self.delay = 0.2
        self.lastDelay = time.time()

atimer = timer()
btimer = timer()
dtimer = timer()
gtimer = timer()
ttimer = timer()
# dtimer = time.time()
# gtimer = time.time()
# ttimer = time.time()
# blinktimer = time.time()
# Alpha
# Beta
# Delta
# Gamma
# Theta
# Mellow
# Concentration
# API http://developer.choosemuse.com/tools/available-data#Raw_EEG

def alpha_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    global atimer
    if time.time() - atimer.lastDelay > 3:
        atimer.delay = random.uniform(0.1,0.2)
        atimer.lastDelay = time.time()
    if ch1 + ch2 + ch3 + ch4 > 3 and time.time() - atimer.timer > atimer.delay:
        print("alpha")
        client.send_message("/abeep", 65.406)
        client.send_message("/abeep", 82.407)
        client.send_message("/abeep", 97.999)
        client.send_message("/abeep", 123.47)
        atimer.timer = time.time()

def beta_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    global btimer
    if time.time() - btimer.lastDelay > 3:
        btimer.delay = random.uniform(0.1,0.2)
        btimer.lastDelay = time.time()
    if ch1 + ch2 + ch3 + ch4 > 2.7 and time.time() - btimer.timer > btimer.delay:
        print("beta")
        client.send_message("/bbeep", 261.63)
        client.send_message("/bbeep", 329.63)
        client.send_message("/bbeep", 392)
        client.send_message("/bbeep", 493.88)
        btimer.timer = time.time()

def delta_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    global dtimer
    if time.time() - dtimer.lastDelay > 3:
        dtimer.delay = random.uniform(0.2,0.3)
        dtimer.lastDelay = time.time()
    if ch1 + ch2 + ch3 + ch4 > 2.5 and time.time() - dtimer.timer > dtimer.delay:
        print("delta")
        client.send_message("/beep", 1174.658)
        client.send_message("/beep", 587.3295)
        dtimer.timer = time.time()

def gamma_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    global gtimer
    if time.time() - gtimer.lastDelay > 3:
        gtimer.delay = random.uniform(0.2,0.3)
        gtimer.lastDelay = time.time()
    if ch1 + ch2 + ch3 + ch4 > 2.0 and time.time() - gtimer.timer > gtimer.delay:
        print("gamma")
        client.send_message("/beep", 784.9909)
        client.send_message("/beep", 391.9954)
        gtimer.timer = time.time()

# def blink_handler(unused_addr, args, blink):
#     if blink:
#         print("blink")
#         client.send_message("/beep", 16.35160)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5005,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/elements/alpha_absolute", alpha_handler, "EEG")
    dispatcher.map("/muse/elements/beta_absolute", beta_handler, "EEG")
    dispatcher.map("/muse/elements/delta_absolute", delta_handler, "EEG")
    dispatcher.map("/muse/elements/gamma_absolute", gamma_handler, "EEG")
    # dispatcher.map("/muse/elements/blink", blink_handler, "EEG")
    dispatcher.map("/muse/elements/")



    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
