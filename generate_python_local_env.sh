# Debian for base version 3.10 change accordingly

#insatll pip venv
sudo apt install python3-pip
sudo apt install python3.10-venv

#mkdir py3
#cd py3
python3.10 -m venv env
source env/bin/activate
pip list
#deactivate
# to remove env just remove the dir done
#rm -rf env