This tool (python script) will automatically **upload and organize** pictures on Flickr.It is best used with Cron or some task scheduler so you don't have to worry about your pictures not being backed up.

The tool is still in development so use at your own risk.

For those who want to use it, it provides following:

1) Automatically uploads all pictures and movies from the given directory and **ALL** subdirectories to flickr (it filters files using extensions).

2) It uses directory names to **automatically tag pictures** with tags being all words in all parent directories, plus the picture file name. It may also add additional tags to picture from EXIF information of the pciture  e.g. it will add tags from 'Image XPKeywords' used by Kodak cameras to tag pictures in camera using EXIF.

3) It will use these tags to **automatically create flickr sets** e.g. picture located in /Vacations/Malta 2008/img3430.jpg will be tag with 'Vacations, Malta, 2008, img3430, jpg' and it will be placed in Set called 'Vacations Malta 2008'


4) The tool creates an maintains its own database of already uploaded files thus it can be run as a task every day and it will upload only newly added pictures that have been placed in the folder structure below the main directory e.g. c:\pictures

5) If you loose the local database (history of uploaded pictures), the tool will try to first recreate the history file by comparing flickr content with local folders. This feature will also delete duplicate pictures from Flickr by comparing special tags that start with #. Do not remove or change these special tags since they are the link to your pictures on your local drive.

6) If you remove picture from automatically created set the picture will be placed back in this set by the tool

7) If you delete picture from flickr you will see an error in the error log saying "can not find a picture with tags... in flickr" or something along those lines

8) If you remove picture from local folder the tool will **NOT** delete it from flickr in another words flickr is the authoritative resource for information on picture existance

9) Recently an option to delete entire flickr collections has been added - please use this feature with cuation!

For instructions on running the tool using python please see **Wiki.**

**For Windows users there is also standalone executable in downloads which does not require Python to be installed. Just run/schedule the uploadr.exe**

PS: If you find a bug feel free to comment and even better fix it :)

PS2: If you will find this tool helpful and working to your satisfaction feel free to donate using PayPal to pkolarov@gmail.com

Enjoy!
