# time-to-go-home
Simple command line app which calculates your working periods

## Installing (Debian-based distributions only)

sudo apt install python-pip &nbsp;
pip install datetime &nbsp;
mkdir ~/.local/bin &nbsp;
cd ~/.local/bin &nbsp;
git clone https://github.com/mrgurgel/time-to-go-home.git &nbsp;
echo -e '#!/bin/bash\npython3 ~/.local/bin/time-to-go-home/lifter/calculator.py' >> calculate-time-go-home &nbsp;
chmod +x ~/.local/bin/calculate-time-go-home &nbsp;


## Removing

rm ~/.local/bin/calculate-time-go-home &nbsp;
rm -rf ~/.local/bin/time-to-go-home &nbsp;
