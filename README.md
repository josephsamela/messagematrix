## What is LED Message Matrix?
The message matrix is an internet connected display YOU can send messages! 

![Hey Y'all!](/static/video.gif)

This display has **ONE** job. Recieve POST requests with messages and display the message!

Awesome integration with *Home Automation* projects! 

* Working on a smart weather-station? Send weater reports to the display!
* Smart coffee maker? Get notified when your brew is ready!
* Smart sprinkler system? Get notfications to water your plants!
* Email alerts!
* Calendar reminders!
* Git commits!
* Music artist information!
* Package delivery status!
* Solar panel performance!
* Any project can be integrated, just send a post request!

If you can POST it, you can display it with ***Message Matrix***!

## Running code!
For this project I'm using a 32x32 LED matrix with a Raspberry Pi using the [Adafruit RGB Matrix Hat](https://www.adafruit.com/product/2345).

Start the application with:
```
$ python main.py
```
In a web-browser navigate to `host_local_address:5000` and if you see this webpage, it works!

![Demo Site](/static/demo_site.png)
