# Author:       Benjamin Busch
# created:      2023-02-15
# Version:      1.1
# Description:
#   This program clearing automatic the Download Directory 'Downloads'
#   under Windows every day at 18:00 pm  o'clock.
# History-Fixes:
# Forgot to delete extraction folders.

import logging
import os
import shutil

not_delete = ['C:\\Users\\bbusch\\Downloads\\desktop.ini']
downloadPath = 'C:\\Users\\bbusch\\Downloads\\'
logname = 'automaticClearFolder.log'

logging.basicConfig(filename=logname,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logging.info('Started TASK...  ')
for file_ame in os.listdir(downloadPath):
    targetObject = downloadPath + file_ame
    if os.path.isfile(targetObject):
        if not_delete[0] != targetObject:
            logging.info('Delete file:' + targetObject)
            os.remove(targetObject)
    if os.path.isdir(targetObject):
        shutil.rmtree(targetObject)
        logging.info("Delete Folder: " + targetObject)
logging.info('-- Finished TASK -- ')