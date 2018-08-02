import subprocess
import shutil
import os
import glob

DIR_INPUT = 'Source'
DIR_OUT = 'Result'

os.mkdir('Result')
for file in glob.glob('Source/*.jpg'):
    file_name_old = file.replace('Source\\', '')
    file_name_new = file_name_old[:-4] + '_new.jpg'
    subprocess.run(rf'convert {DIR_INPUT}/{file_name_old} -resize 200 {DIR_OUT}/{file_name_new}')


