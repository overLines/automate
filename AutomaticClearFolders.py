# Author:       Benjamin Busch
# created:      2023-02-15
# Version:      1.0
# Description:
#   This program clearing automatic the Download Directory 'Downloads'
#   under Windows every day at 18:00 pm o Clock.

import logging
import os

from setuptools.command.dist_info import dist_info

downloadPath = 'C:\\Users\\bbusch\\Downloads\\'
not_delete = ['C:\\Users\\bbusch\\Downloads\\desktop.ini']
logname = 'automaticClearFolder.log'

logging.basicConfig(filename=logname,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logging.info('Started TASK...  ')
for file_ame in os.listdir(downloadPath):
    file = downloadPath + file_ame
    curFile = str(file)

    if os.path.isfile(file):
        if not_delete[0] != curFile:
            print(curFile)
            logging.info('Delete file:'+curFile)
            os.remove(file)
logging.info('-- Finished TASK -- ')
