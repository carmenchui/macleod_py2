macleod (Python2 Version - working on mac os x 10.10+)
======================================================

backup version of @thahmann's macleod scripts that run on Python2 (unsure if this copy is older than the following commit: <https://github.com/thahmann/macleod/tree/fa5c900afdb46b34be85865b07ad68b0a520d09b>)

the following scripts are **unmodified** from the original source; this repo is meant as a **backup** of a working version prior to the python3 change, along with any associated instructions to help users get this running on their macs

Installation:
-------------
the scripts appear to run on python 2.7 on mac os x 10.10+ (yosemite or higher)
1. clone repo or download zip from github
2. change file paths in macleod\_mac.conf (see conf/ folder)
3. create provers/ folder with the **mac** ladr and vampire binaries - send me a msg if you need them but the vampire\_mac binaries i have are very old and am unsure if they work
4. give macleod\_py2 folder executable permission (just in case os-level permission errors show up)
```bash
chmod +x macleod_py2
```
5. check your python version (should be python 2.7)
```bash
python --version
```
6. install pip and texttable if you haven't already
```bash
sudo easy_install pip
sudo pip install texttable
```
7. add src/ and task/ folders to PYTHONPATH variable on your machine
```bash
echo $PYTHONPATH
export PYTHONPATH=/path/to/macleod_py2/src:/path/to/macleod_py2/tasks:$PYTHONPATH
```
if you want to add this to the PYTHONPATH **permanently**, you will need to modify ~/.bash\_profile by appending this at the end of the file (located in home directory; e.g., /Users/cchui/ - this is a hidden file, make sure you enabled viewing hidden files in Finder)
```bash
export PYTHONPATH=/path/to/macleod_py2/src:/path/to/macleod_py2/tasks:$PYTHONPATH
```
8. navigate to gui folder and run the gui script
```bash
ls
cd macleod_py2
python gui/gui_alpha.py
```
9. open a clif file and see if it parses the imports correctly - if doing nested imports, your file directory in macleod\_mac.conf must be accurate otherwise you will get errors
![gui](/doc/img/2018-04-04_11-25-39.jpg?raw=true)
10. click buttons to do desired translations or run consistency check

Consistency Check:
------------------
* ladr consistency check appears to work
![consistency](/doc/img/2018-04-04_12-15-30.jpg?raw=true)
* **vampire has been disabled** in the provers section of macleod\_mac.conf because it throws an OS-level error with python and it causes macleod to hang (will look at this later but it might also be because the vampire_mac binaries are too old)

Translations:
-------------
tested and confirmed to work for:
* clif to ladr translation
* clif to tptp translation

translations will go into the /generated and /conversions file of wherever you store your ontologies (in this case, mine go to the [colore](http://colore.oor.net) repository)

![tptp](/doc/img/2018-04-04_12-09-52.jpg?raw=true)


Noted Errors:
-------------
gui does hang for a little bit if working with big files (be patient?? make a cuppa)