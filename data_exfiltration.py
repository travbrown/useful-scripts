import shutil
import os, fnmatch
import glob
from pathlib import Path
import sys

def exfiltrate(source_dir, target_dir, file_type):
    filter_string = source_dir + '**/*.' + file_type
    print('Copying: \n\n')
    for file_name in glob.iglob(filter_string):
        print(file_name)
        shutil.copy(os.path.join(source_dir, file_name), target_dir)
    print('\n Files Copied')

source_dir = sys.argv[1]
target_dir = sys.argv[2]
file_type = sys.argv[3]
exfiltrate(source_dir, target_dir, file_type)

'''
Run script:
    navigate to the folder the script is in terminal
    Run command --> python3 data_exfiltration.py "<absolute_path_of_source>" "<absolute path of destination>" "<insert file type (eg. html)>"
'''