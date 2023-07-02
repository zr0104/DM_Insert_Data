import psycopg2
from apscheduler.schedulers.blocking import BlockingScheduler
import ddt

import useDB
import config
from datetime import datetime, timedelta
import pytz
import timezone_change
import logger
import openpyxl
import xlsxwriter
import xlrd
from handle_excel import excel_data
import os
import sys
import csv
from parameterized import parameterized
import unittest
basePath = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# with open(basePath + "/Config/credit_card_info.csv","r",encoding="utf-8") as rf:
#     myread = csv.reader(rf)
#     keylist = list(myread)
#     print(keylist)


# @ddt.ddt
class DmDBHandle():

    def __init__(self):
        self.useDB = useDB
        self.config = config

        # change mexico time
        self.target_date_time_M = pytz.timezone('Asia/Shanghai')
        self.target_date_time_MEX = datetime.now(self.target_date_time_M)
        self.target_date_time = self.target_date_time_MEX.strftime('%Y-%m-%d')
        self.logger = logger.MyLogging().get_log("insert_data_" + self.target_date_time)

    def search_MAX_NBR(self):
        search_max_sql= f"""select MAX(EMPLOYEEID) FROM SYSDBA.EMPLOYEES;"""
        search_max = useDB.useDB().search(search_max_sql)
        # self.logger.info("search_max:{}".format(search_max))
        return search_max

    # @parameterized.expand(keylist)
    # @ddt.data(*data)
    def Insert_Dm_DB(self):
        data = excel_data.get_excel_data(config.DATA_FILENAME)
        print(data)

        # Ident_card, Credit_card_nbr, Amount
        data_len = len(data)
        for i in range(0, data_len):
            Keys = DmDBHandle().search_MAX_NBR()
            Keys = Keys[0][0]
            Keys += 1
            Ident_card = data[i][0]
            Credit_card = data[i][1]
            Amount = data[i][2]
            insert_emp = f"""insert into EMPLOYEES (EMPLOYEEID,NATIONALNO,PERSONID,LOGINID,TITLE,BIRTHDATE,MARITALSTATUS,HAIRDATE,SALARY) 
                                    values ('{Keys}','{Ident_card}','{Credit_card}','1102','Master','1997-09-07','S','2008/5/30','{Amount}');"""
            # self.logger.info("insert_emp:{}".format(insert_emp))
            insert_result = useDB.useDB().insert(insert_emp)
            # self.logger.info("replenishment:{}".format(insert_result))
        return insert_result

    def Search_Dm_DB(self):
        insert_emp = f"""SELECT * FROM SYSDBA.EMPLOYEES;"""
        # self.logger.info(insert_emp)
        emp_result = useDB.useDB().search(insert_emp)
        # self.logger.info("emp_result:{}".format(emp_result))
        return emp_result


if __name__ == '__main__':
    exehandle = DmDBHandle()
    print(exehandle.search_MAX_NBR())
    print(exehandle.Insert_Dm_DB())
    print(exehandle.Search_Dm_DB())