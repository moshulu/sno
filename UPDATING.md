# Updating your Sno system

The great thing about your Sno device is that it's completely off the internet! That means you can use your Sno device anywhere.

The bad thing about this is that when there's new stuff that's available for production, or an important fix needed to improve your device, it's hard to get to. Luckily, you're in luck! Updating is really easy.

### Steps

1. Connect your Sno system to a monitor, keyboard, and mouse.

2. Connect your Sno system to the internet

3. Open a command prompt (Ctrl + Alt + t)

4. Type
```
cd /var/www/
```
and press "Enter"

5. Type
```
sudo git clone https://github.com/moshulu/sno
```

That's it! Your Sno device now has the latest light sequences, schematics, and (if you're using it) web app.

*Note: this will NOT update the iOS or Android application. To update the iOS or Android application, use the respective app stores.*
