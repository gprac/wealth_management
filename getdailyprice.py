#!/usr/bin/python

import sqlite3
import requests
from bs4 import BeautifulSoup

def get_url(url, params=None, proxies=None):
    rsp = requests.get(url, params=params, proxies=proxies)
    rsp.raise_for_status()
    return rsp.text


def get_fund_data(code, start='', end=''):
    record = {'Code': code}
    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx'
    params = {'type': 'lsjz', 'code': code, 'page': 1, 'per': 65535, 'sdate': start, 'edate': end}
    html = get_url(url, params)
    soup = BeautifulSoup(html, 'html.parser')
    records = []
    tab = soup.findAll('tbody')[0]
    for tr in tab.findAll('tr'):
        if tr.findAll('td') and len((tr.findAll('td'))) == 7:
            record['Date'] = str(tr.select('td:nth-of-type(1)')[0].getText().strip())
            record['NetAssetValue'] = str(tr.select('td:nth-of-type(2)')[0].getText().strip())
            record['ChangePercent'] = str(tr.select('td:nth-of-type(4)')[0].getText().strip())
            records.append(record.copy())
    return records



conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
tablenames = cursor.execute("select name from sqlite_master where type = 'table' order by name").fetchall()
print(tablenames)
products = cursor.execute("select id, code, type from product_product").fetchall()

yfdvalue = get_fund_data('000968', '2019-03-18', '2019-03-18')
#for row in products:
#	if row[2] == 'F':
#		print(row[1])
mysqlstr = 'replace into product_dailyprice(product_id, price, date ) values(5,'+str(yfdvalue[0]['NetAssetValue'])+',datetime(\''+ str(yfdvalue[0]['Date'])+'\'))' 
print(mysqlstr)
cursor.execute(mysqlstr)
#tablestruct = cursor.execute('PRAGMA table_info(product_dailyprice)').fetchall()
#print(tablestruct)
conn.commit()
products = cursor.execute("select * from product_dailyprice where product_id=5").fetchall()
print(products)






def demo(code, start, end):
    table = PrettyTable()
    table.field_names = ['Code', 'Date', 'NAV', 'Change']
    table.align['Change'] = 'r'
    records = get_fund_data(code, start, end)
    for record in records:
        table.add_row([record['Code'], record['Date'], record['NetAssetValue'], record['ChangePercent']])
    return table


#if __name__ == "__main__":
#    print(get_fund_data('110022', '2018-02-22', '2018-03-02'))