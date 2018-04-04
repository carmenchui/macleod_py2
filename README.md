Macleod (Python2 Version)
======================================================

backup version of @thahmann's macleod scripts that run on Python2 (unsure if this copy is older than the following commit: <https://github.com/thahmann/macleod/tree/fa5c900afdb46b34be85865b07ad68b0a520d09b>)

Installation:
-------------
mostly for mac since the scripts appear to run on python 2.7 on mac os x 10.10 (yosemite)
* clone repo or download zip
* change file paths in the conf/ folder
* create provers/ folder with the ladr and vampire binaries
* install texttable
--
sudo pip install texttable
--
* add src/ and task/ folders to PYTHONPATH variable on machine
--
echo $PYTHONPATH
export PYTHONPATH=/path/to/macleod_py2/src:/path/to/macleod_py2/tasks:$PYTHONPATH
--
* navigate to gui folder and run the gui script
--
ls
cd macleod_py2
python gui/gui_alpha.py
--
