# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:10:53 2018

@author: Loka Rupesh Reddy
"""
import pymysql as db
from pandas import DataFrame
import pandas as pd
import numpy as np

local_conn=db.connect(host="localhost", port=3306, user='root', passwd='root', db='unison')
local_cur=local_conn.cursor()

for col in columns:
    col_name = col
    avg = (data[col]).replace(0,np.nan).dropna().mean()
    sd=(data[col]).replace(0,np.nan).dropna().std()
    median=(data[col]).replace(0,np.nan).dropna().median()
    count=(data[col]).replace(0,np.nan).dropna().count()
    local_cur.execute("insert into statistics values ('%s', '%f', '%f', '%f', '%d', now())" % 
                (col_name,avg,sd,median,count))

    local_conn.commit()