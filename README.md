macleod (Python2 Version - working on mac os x 10.10+)
======================================================

backup version of @thahmann's macleod scripts that run on Python2 (unsure if this copy is older than the following commit: <https://github.com/thahmann/macleod/tree/fa5c900afdb46b34be85865b07ad68b0a520d09b>)

the following scripts are **unmodified** from the original source; this repo is meant as a backup of a working version prior to the python3 change

Installation:
-------------
mostly for mac since the scripts appear to run on python 2.7 on mac os x 10.10+ (yosemite or higher)
* clone repo or download zip from github
* change file paths in macleod\_mac.conf and logging.conf (see conf/ folder)
* create provers/ folder with the **mac** ladr and vampire binaries - send me a msg if you need them but the vampire\_mac binaries i have are very old
* install texttable
```bash
sudo pip install texttable
```
* add src/ and task/ folders to PYTHONPATH variable on machine
```bash
echo $PYTHONPATH
export PYTHONPATH=/path/to/macleod_py2/src:/path/to/macleod_py2/tasks:$PYTHONPATH
```
* navigate to gui folder and run the gui script
```bash
ls
cd macleod_py2
python gui/gui_alpha.py
```
* open a clif file and see if it parses the imports correctly
![gui](/doc/img/2018-04-04_11-25-39.jpg?raw=true)
* click buttons to do desired translations

Consistency Check:
------------------
* ladr consistency check appears to work... unsure about vampire at the moment?? system hangs

Translations:
-------------
tested and confirmed to work for:
* clif to ladr translation
* clif to tptp translation

translations will go into the /generated and /conversions file of wherever you store your ontologies (in this case, mine go to the [colore](http://colore.oor.net) repository)

Noted Errors:
-------------
there is a logging error in line 406 of src/clif.py when the script tries to open a clif file but it does not appear to affect any functionality
![406error](/doc/img/2018-04-04_11-25-16.jpg?raw=true)

gui does hang for a little bit if working with big files (be patient??)