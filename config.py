from Fernet import FernetEncrdecr

# """"""""""""""""""""""""""""""""PUBLIC CONFIGURATION"""""""""""""""""""""""""""""""""""""""""""
project_id = ''
dataset_name = "SYSDBA"

# """"""""""""""""""""""""""""""""ATM CONFIGURATION""""""""""""""""""""""""""""""""""""
DATA_FILENAME = "credit_card_info.xlsx"

# dm DB Info
DBtype = '3'
db_key = b'OTBQDg8NDtSNtGGw35IKevckBrigRBR6a4qpn5WWq6s='
db_host = 'LOCALHOST'
db_port = '8809'
db_user = 'SYSDBA'
db_pwd = b'gAAAAABkoQivlcGCG0y573jGwHmpTp-t5O7dIHEoc8lFmisvZb5vbS3FyuVVpZpsI324ZmDROgFCfpRLE5DY59KUVlh8wudQkg=='
database = 'SYSDBA'
db_password = FernetEncrdecr().decrdecr(db_key,db_pwd)[0]

# 截图路径相关配置
import os
currentPath = os.path.dirname(os.path.abspath(__file__))
logPath = os.path.join(currentPath,'logs')



