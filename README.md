# time-to-go-home
Simple command line app which calculates your working periods

## Installing (Debian-based distributions only)

sudo apt install python-pip

pip install datetime

mkdir ~/.local/bin

cd ~/.local/bin

git clone https://github.com/mrgurgel/time-to-go-home.git

echo "#!/bin/bash\npython3 ~/.local/bin/time-to-go-home/lifter/calculator.py" >> calculate-time-go-home

chmod +x ~/.local/bin/calculate-time-go-home
