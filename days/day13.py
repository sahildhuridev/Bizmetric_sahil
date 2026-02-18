'''
Docstring for days.day13
Working with ENV

Python -m venv .venv_name
( do you want to select only this folder - say yes)
'''

# command to make env active:
# env_name\Scripts\Activate 
# (in powershell) env_name\bin\Activate 

# pip install pyodbc pandas numpy

# to uninstall the package from enviroment:
#  


# pip list - tells us what all packages we have installed and their version







# debugging and logging 
# 
#  

# import logging
# # security level
# # debug
# # info
# # warning 
# # error - stopping the user to go ahead 
# # critical - when rules are violated and still user can do it

# logging.basicConfig(level = logging.ERROR) # get all this info as outcome from error onwards
# logging.log(logging.DEBUG , " log debug message this is sahil sadanand dhuri")
# logging.log(logging.INFO , " log INFO message")
# logging.log(logging.WARNING , " log WARNING message")
# logging.log(logging.ERROR , " log ERROR message")
# logging.log(logging.CRITICAL , " log CRITICAL message")


#-------------------- first method ------------------------------------------------------

import logging

logging.basicConfig( filename = 'day13_app.log' ,level = logging.DEBUG)

logging.debug('new log code: ')

logger = logging.getLogger('sahil')

logging.debug('this is generated from debug function')
logging.warning('this is generated from warning function')


logger.debug('this is generated from debug function')
logger.warning('this is generated from warning function')

logger2 = logging.getLogger('godspeed')

logging.error('this is generated from error function')
logging.critical('this is generated from critical function')


logger2.error('this is generated from error function')
logger2.critical('this is generated from critical function')

#logging.shutdown()


# ---------------- other method -----------------------------
import logging
logging.basicConfig(level = logging.DEBUG)
# create name for logger
logger = logging.getLogger('my logs')
gen_log_file = logging.FileHandler('other_log_file.txt')
gen_log_file.setLevel(logging.INFO)
logger.addHandler(gen_log_file)
print('login page')
logger.info('INFO: this is just inormation of the process')
logger.debug('DEBUG: this is just debug of the process')
