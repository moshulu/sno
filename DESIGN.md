# Hardware

### Wiring Diagram

[This is the wiring diagram](https://imgur.com/a/e6vypxH).

Let's start at the battery. The battery I used was a 20000mAh power bank with both 1A out and 2A out. The Raspberry Pi must use the 2A out port, or else it won't have enough power to run the web server and light strips at the same time (well, it will - but the lights will do an odd flickering thing). 

From there, I connected the power to the breadboard. I decided to power all ports to the breadboard, to make it easy for connecting more NeoPixel light strips in the future.

On the breadboard, I directed the power to the NeoPixel strip via a diode, to make sure that there wasn't power being traced back to the breadboard (and thus the raspberry pi) that could potentially destroy the circuit.

The NeoPixel's Din and DGND wires were connected to the raspberry pi directly but in theory, the DGND strip could be connected to the breadboard.

One great thing about this design is that it can *absolutely* be scaled up to include more than one NeoPixel light strips, which is what different iterations will include.

### Network Diagram

[This is the LAN network diagram](https://imgur.com/a/mTQ3qrB).

The LAN network diagram is self-explanatory. It's important to note that with this configuration, the mobile device will retain internet capabilities *and also* create a LAN with the Pi.
