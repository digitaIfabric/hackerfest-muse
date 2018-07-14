#!/usr/bin/env python

import argparse
import math
import numpy
import time

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 57120)
atimer = time.time()
btimer = time.time()

def alpha_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    global atimer
    if ch1 + ch2 + ch3 + ch4 > 3 and time.time() - atimer > 0.2:
        print("alpha")
        frequency_multiplier = 100
        client.send_message("/beep", 65.406)
        client.send_message("/beep", 82.407)
        client.send_message("/beep", 97.999)
        client.send_message("/beep", 123.47)
        atimer = time.time()

def beta_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    global btimer
    if ch1 + ch2 + ch3 + ch4 > 2.7 and time.time() - btimer > 0.2:
        print("beta")
        frequency_multiplier = 500
        client.send_message("/beep", 261.63)
        client.send_message("/beep", 329.63)
        client.send_message("/beep", 392)
        client.send_message("/beep", 493.88)
        btimer = time.time()
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/elements/alpha_absolute", alpha_handler, "EEG")
    dispatcher.map("/muse/elements/beta_absolute", beta_handler, "EEG")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
