import subprocess
import shutil
import os
import glob

DIR_INPUT = 'Source'
DIR_OUT = 'Result'

os.mkdir('Result')
for file in glob.glob('Source/*.jpg'):
    file_name_old = os.path.basename(file)
    file_name_new = os.path.splitext(file_name_old)[0] + '_new.jpg'
    subprocess.run(rf'convert {DIR_INPUT}/{file_name_old} -resize 200 {DIR_OUT}/{file_name_new}')
