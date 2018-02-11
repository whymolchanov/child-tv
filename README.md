## Add videos to USB flash
On empty usb flash make `video` folder, and put inside it folder for every cartoon (script will unite it for play)  
**Requirements for filename:** they mustn't have space inside of filename (e.g. 'some file.avi' doesn't play at all)
```
video --
	first_cartoon --
		video1.mp4
		...
		...
	second_cartoon --
		video1.mp4
		...
		...
```


## Initial setup  

First we need automount flash on system startup

- clone this repository to RasPI
- run `setup.py` with sudo *it will add usb to `fstab`, create mount folder and mount*
- run `pip install -r requirements.txt`

## Add main script to .bashrc
inside `.bashrc` *or .zshrc if you use zshell* add `python %some folder where you hold script%/main.py` to auto run script on system start

[IR receiver installation guide and omxplayer integration (RU)](IR-receiver-installation-guilde.md)
