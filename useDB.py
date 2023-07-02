# -*- coding: utf-8 -*-

from flask_bootstrap import Bootstrap
import dmPython
import config
import logger
import pytz
from datetime import datetime, timedelta

target_date_time = pytz.timezone('Asia/Shanghai')
target_date_time_M = datetime.now(target_date_time).strftime('%Y-%m-%d')
logger = logger.MyLogging().get_log("insert_data_" + target_date_time_M)

class sqliteDB(object):

    def __init__(self):
        return

    def connect(self):
        import sqlite3, os, platform
        path = os.getcwd()
        if platform.system() == 'Windows':
            path += '\\'
        else:
            path += '/'

        # change root password to yours:
        conn = sqlite3.connect(path + config.sqliteFile)
        return conn

    def search(self, sql):
        logger.info(sql)
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()
        # logger.info('values:',values)
        cursor.close()
        conn.close()
        return values

    def insert(self, sql):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        logger.info(sql)
        cursor.close()
        try:
            conn.commit()
        except :
            logger.info('commit error')
        conn.close()


class mysqlDB(object):

    def __init__(self):
        return

    def connect(self):
        # change root password to yours:

        # import mysql.connector
        # conn = mysql.connector.connect(host=config.db_host, port=config.db_port, user=config.db_user, password=config.db_password, database=config.database,
        #                       auth_plugin='mysql_native_password')

        import pymysql
        conn = pymysql.connect(host=config.db_host, port=config.db_port, user=config.db_user, password=config.db_password, database=config.database)

        return conn

    def search(self, sql):
        conn = self.connect()
        cursor = conn.cursor()
        # logger.info(sql)
        cursor.execute(sql)
        values = cursor.fetchall()
        # logger.info('values1 :', values)
        cursor.close()
        conn.close()
        return values

    def insert(self, sql):
        logger.debug(sql)
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        try:
            conn.commit()
        except :
            logger.error('commit error')
        conn.close()

    def excutesql(self, sql):
        logger.debug(sql)
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        try:
            conn.commit()
        except:
            logger.error('commit error')
        conn.close()

    # 测试查询，防止sql注入
    def searchsql(self, sql, args):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        values = cursor.fetchall()
        cursor.close()
        return values

class DmsqlDb(object):

    def __init__(self):
        return

    def connect(self):
        # change root password to yours:

        import dmPython
        conn = dmPython.connect(user=config.db_user, password=config.db_password, server=config.db_host, port=config.db_port)
        return conn

    def search(self, sql):
        conn = self.connect()
        cursor = conn.cursor()
        # logger.info(sql)
        cursor.execute(sql)
        values = cursor.fetchall()
        # logger.info('values1 :', values)
        cursor.close()
        conn.close()
        return values

    def insert(self, sql):
        logger.debug(sql)
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        try:
            conn.commit()
        except :
            logger.error('commit error')
        conn.close()

    def excutesql(self, sql):
        logger.debug(sql)
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        try:
            conn.commit()
        except:
            logger.error('commit error')
        conn.close()

    # 测试查询，防止sql注入
    def searchsql(self, sql, args):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        values = cursor.fetchall()
        cursor.close()
        return values

class useDB(object):

    def __init__(self):
        self.DBtype = config.DBtype
        return

    def insert(self,sql):
        if self.DBtype == '1':
            sqliteDB().insert(sql)
        else:
            DmsqlDb().insert(sql)

    def search(self,sql):
        if self.DBtype == '1':
            return sqliteDB().search(sql)
        else:
            return DmsqlDb().search(sql)

    def searchsql(self, sql,args):
        if self.DBtype == '1':
            return sqliteDB().search(sql)
        else:
            return DmsqlDb().searchsql(sql,args)