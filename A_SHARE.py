import os, platform
os.system('git pull')
try:
    import requests
except:
    os.system('pip2 install requests')

import a_share
a_share.login()
