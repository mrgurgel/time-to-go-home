# time-to-go-home
Simple command line app which calculates and sum your working periods

## Description
This command-line argument will request the periods that you have worked on certain day.  
The pattern is: HH:MM with comma-separeted values  

**Input example:**
```10:08, 12:09, 13:57, 17:43, 17:54, 20:07```

If the number of entries are odd the system comples the last occurrence with the current hour/minute.  
E.g.:  

For the input ``10:08, 12:09, 13:57`` and considering that the current time is 18:00 the system will threat the following values:
```
10:08, 12:09, 13:57, 18:00
```

## Screenshot
![Time to go home screenshot](https://raw.githubusercontent.com/mrgurgel/time-to-go-home/master/misc/images/time-to-go-home.png)


## Pre requisites
sudo apt install python-pip  

pip install datetime  

## Installing (Debian-based distributions only)

```mkdir ~/.local/bin  
cd ~/.local/bin  
git clone https://github.com/mrgurgel/time-to-go-home.git
echo -e '#!/bin/bash\npython3 ~/.local/bin/time-to-go-home/lifter/calculator.py' >> calculate-time-go-home  
chmod +x ~/.local/bin/calculate-time-go-home
```


## Using

**Execute:**  
``calculate-time-go-home``

## Removing

```rm ~/.local/bin/calculate-time-go-home  
rm -rf ~/.local/bin/time-to-go-home   
```

