#!/usr/bin/env python

import argparse
import math
import numpy

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 57120)

def concentration_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    if ch1 + ch2 + ch3 + ch4 > 4000:
        print("beep")
        frequency_multiplier = 0.1
        client.send_message("/beep", ch1*frequency_multiplier)
        client.send_message("/beep", ch2*frequency_multiplier)
        client.send_message("/beep", ch3*frequency_multiplier)
        client.send_message("/beep", ch4*frequency_multiplier)

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
    dispatcher.map("/muse/eeg", concentration_handler, "EEG")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
