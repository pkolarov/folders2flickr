# How to install and run Windows standalone executable #

1) Unzip into some folder (e.g. c:\folders2flickr)

2) edit **uploadr.ini** (change the folder where all your pictures are located and their visibility in flickr)

3) Run:  c:\folders2flickr\uploadr.exe

4) First time you run the tool it will open a web browser and ask for your permission to authorize Folders2Flicks. Accept permissions answer Y in the console window.

5) Check the logs and your flickr account if it works as expected.

6) Use Windows Task Scheduler to schedule running c:\folders2flickr\uploadr.exe in some regular intervals e.g. every other night.



# For Linux/MAC - running it as Python script #

If you are not using the standalone windows executable of this tool and you prefer to run it as a Python script, here is how:


0) Make sure you have Python 2.5 or later version installed (not version 3 and up though)

1) Unrar/Unzip into some folder (e.g. c:\folders2flickr)

2) edit **uploadr.ini**

3) first run from cmd line (or later as a cron job) : **python uploadr.py**

**NOTE:** If running for the first time the tool will look for .token file - if it does not find it, it will open default web browser and will ask you for authorization and permission (Delete level) on Flickr web site.

4) After running please look at logs and see if there is problems or whats it doing