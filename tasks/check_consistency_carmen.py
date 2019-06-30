from src import filemgt
from tasks import *
import os, sys
from src.ClifModuleSet import ClifModuleSet
from tasks import check_consistency
import logging

#global variables
filemgt.start_logging()
tempfolder = filemgt.read_config('converters', 'tempfolder')
ignores = [tempfolder,"theorems", "generated", "output", "archive", "mappings", "experiments", "interprets"]
ending = filemgt.read_config('cl','ending')
licence.print_terms()

if __name__ == '__main__':
    options = sys.argv
    options.reverse()
    options.pop()
    folder = options.pop()
    ladr_all(folder, options)

def consistent_all(folder, options=[]):
    good = 0
    bad = 0
    neutral = 0
    good_files = []
    bad_files = []
    neutral_files = []
    for directory, subdirs, files in os.walk(folder):
        if any(ignore in directory for ignore in ignores):
            pass
        else:
            for single_file in files:
                if single_file.endswith(ending):
                    filename = os.path.join(directory, single_file)
                    print filename
                    m = ClifModuleSet(filename)
                    (result, _)=check_consistency.consistent(filename, m, options)
                    if result is True:
                        good += 1
                        good_files.append(filename)
                    elif result is False:
                        bad += 1
                        bad_files.append(filename)
                    else:
                        neutral += 1
                        neutral_files.append(filename)
    print "\n------------ CONSISTENCY CHECK (ALL) RESULTS ------------\n"
    logging.getLogger(__name__).info("------------ CONSISTENCY CHECK (ALL) RESULTS ------------\n")
    print str(good+bad+neutral) + " files in total"
    logging.getLogger(__name__).info(str(good+bad+neutral) + " files in total \n")
    print str(good) + " consistent theories:"
    logging.getLogger(__name__).info(str(good) + " consistent:\n")
    for line in good_files:
    	logging.getLogger(__name__).info(" - "+line)
    	print " - " + line
    print str(neutral) + " unknown theories: "
    logging.getLogger(__name__).info(str(neutral) + " unknown:\n")
    for line in neutral_files:
    	logging.getLogger(__name__).info(" - "+line)
    	print " - " + line
    print str(bad) + " inconsistent theories:"
    logging.getLogger(__name__).info(str(bad) + " inconsistent: \n")
    for line in bad_files:
    	logging.getLogger(__name__).info(" - "+line)
    	print " - " + line