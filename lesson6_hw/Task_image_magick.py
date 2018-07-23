import subprocess
import shutil
import os


os.mkdir('Result')
for file in os.listdir(r'Source'):
    subprocess.run(r'convert Source/{0} -resize 200 {1}_new.jpg'.format(file, file[:-4]))
    shutil.move(src='{}'.format(file[:-4] + '_new.jpg'), dst='Result')
