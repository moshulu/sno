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

Our objectives are relatively simple, and can be read in the [requirements](https://github.com/moshulu/sno/wiki/Requirements).

Our design can be seen in the [design document](https://github.com/moshulu/sno/wiki/Design-Document).

Working test plans can be seen in the [wiki](https://github.com/moshulu/sno/wiki/Test-Plan).
