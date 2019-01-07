# sno
framework for neopixel lightstrips to be controlled by an apache webserver on raspberry pi via php

stay up to date with the newest changes! check out the [changelog](CHANGELOG.md)

## instructions for use by user
### setup
connect raspberry pi to mobile hotspot only. If the raspberry pi was previously connected to a wifi/ethernet connection, edit /etc/wpa_supplicant/wpa_supplicant.conf to only include the mobile hotspot's credentials. Now, whenever the pi is powered on, it looks for that network and auto connects.

open a terminal using

```
ifconfig
```

take a note of where it says "inet" under the section labeled

```
wlan0
```

the number in question should look something like "172.16.123.12." this is the ip address of the raspberry pi. it's important, and we'll use this later.


### connecting to the raspberry pi

##### using browser

Go to the browser of your choice and type in:

```
http://<your pi's ip address>/
```

##### using iPhone

Go to the iPhone app and type in the ip address that we looked at before in the field.

##### using Android

Go to the Android app and type in the ip address that we looked at before in the field.

### selecting the light mode

Select the light mode based on the lists provided, but *remember to turn off the lights when you're done!*

## instructions for replication

The raspberry pi is an incredibly versatile machine. It's low cost and highly efficient. It can run headless on a *full* desktop version of Linux. Certian boards have bluetooth connectivity and wifi chip *built in*. I love this machine with a passion, and I wanted to explore what the pi could do for me. It hasn't let me down yet.

Our objectives are relatively simple, and can be read in the [requirements](https://github.com/moshulu/sno/wiki/Requirements). Our design can be seen in the [design document](https://github.com/moshulu/sno/wiki/Design-Document). Working test plans can be seen in the [wiki](https://github.com/moshulu/sno/wiki/Test-Plan). MUCH more information about how I set everything up is in those documents, along with wiring diagrams, noted vulnerabilities, and constraints.

##### decisions I made

Essentially, we're using a mobile phone's wifi hotspot to send information to the raspberry pi and NeoPixel light strips. Why can't we use bluetooth/OBEX server? Bluetooth is incredibly hard to understand (despite it's ease of use on the user's end) and hard to validate with iPhones. OBEX server capabilites are only *easily* available on Android phones, as well. I could convert the pi into a wireless access point and connect a mobile device to that wifi access point to send commands to the pi, but that takes away internet capabilities from the user's mobile device. I couldn't very well make a hard P2P connection, because that would also take away the user's internet connectivity. My options were limited.

I ended up connecting the raspberry pi to the mobile device's hotspot (thus creating a LAN with the mobile device + pi, and keeping internet connectivity). With the LAN network, I was able to access the pi's apache webserver and using php's $\_GET functionality, I was able to send start and stop specific python scripts that controlled the NeoPixel lightstrips.

### hardware setup

Read the [design document](https://github.com/moshulu/sno/wiki/Design-Document) for a more technical description of what I did, and wiring diagrams.

Wire up the NeoPixel strip first. To do that, you need
- rosin core solder **DO NOT USE ANYTHING ELSE**
- soldering iron
- M2M, M2F, F2F wires that can hold ~5V
- wire strippers
- electrical tape/wire nut
- a steady hand

NeoPixel light strips come with GND, 5V, Din, and DGND wires. I wanted to connect the 5V and GND to a breadboard to free up space on the pi's GPIO pins, so I can have space for more lightstrips in the future. I connected the Din and DGND directly to the raspberry pi's GPIO pins. In my case I used a pi 3B+, and followed this diagram https://raw.githubusercontent.com/splitbrain/rpibplusleaf/master/rpiblusleaf.png

I then set up and powered the breadboard. Check the [design document](https://github.com/moshulu/sno/wiki/Design-Document) to see how I did that.

After soldering and making sure that the soldering was covered by electrical tape/wire nuts, I attached the 5V and GND to the breadboard, the Din to the GPIO pin of my choice, and the DGND to a GND pin on the pi. I think I can connect a DGND to a GND on the breadboard, but I didn't want to take any chances on my first go-round.

### powering on for the first time

Make sure your soldering is covered, and do it in a place that you're okay with catching on fire! You don't know what's going to happen, especially if you're inexperienced with soldering like me.

### installing necessary libraries

To control NeoPixels, I used a python library called Adafruit CircuitPython NeoPixel found [here](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel). It's important to note that the library depends on Adafruit CircuitPython, which can be found [here](https://github.com/adafruit/circuitpython).

### first test

Time to test the lightstrip for the first time!

It's *extremely important* to note that CircuitPython NeoPixel are Python3.x scripts must be run as root. This is because the scripts access GPIO pins directly. If you don't have Python3.x, get it now.

Navigate to wherever you cloned the CircuitPython NeoPixel library and navigate to the "examples" folder. Type in:

```
sudo python3 neopixel_simpletest.py
```

Congratulations!

If you get an error, make sure you have python3 installed. Make sure your libraries were installed correctly. Check your wiring again (that can get confusing).


