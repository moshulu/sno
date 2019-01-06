# sno
framework for neopixel lightstrips to be controlled by an apache webserver on raspberry pi via php

## instructions for use by user
### setup
- connect raspberry pi to mobile hotspot only. If the raspberry pi was previously connected to a wifi/ethernet connection, edit /etc/wpa_supplicant/wpa_supplicant.conf to only include the mobile hotspot's credentials. Now, whenever the pi is powered on, it looks for that network and auto connects.

### connecting to the raspberry pi
2a. Go to the browser of your choice and type in

```
http://<your provided ip address>/
```

2b. Go to the iPhone app and type in the supplied ip address in the field

2c. Go to the Android app and type in the supplied ip address in the field

3. Select light mode

