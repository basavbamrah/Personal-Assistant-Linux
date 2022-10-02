from lib2to3.pgen2.token import tok_name
from random import random
from cryptography.fernet import Fernet
import mysql.connector

import random
import secrets


class Encrypt:
    def __init__(self):
        self.conn2 = mysql.connector.connect(user='root',
                                            host='localhost',
                                            port=3306,
                                            password='')
        self.cur = self.conn2.cursor()
        self.cur.execute('use assistant')
        try:
            self.cur.execute(
                "create table tkeys(id varchar(20) primary key,tkey varchar(200));")
            print('yes')
        except Exception as e:
            print(e)
            pass

    def gen_key(self):
        key=Fernet.generate_key().decode()
        return key

    def hash_fun(self, token):
        dig = '123456789'
        
        token = bin(token)
        return ("".join(random.choices(dig, k=3)) + token+"".join(random.choices(dig, k=3))).replace('0b', "")

    def save_key(self, key, token_table):
        print('key: ',key)
        valid_token = [i for i in range(50, 101)]  # 50-100
        rand_key = secrets.token_urlsafe(64)
        if token_table in valid_token:
            token_table = self.hash_fun(token_table)
        else:
            return
        # process key
        print(token_table)
        self.cur.execute(f'insert into tkeys values("{token_table}", "{key}");')
        # rand_token = self.hash_fun(random.randint(650, 750))
        # rand_key = base64.b85encode(rand_key).decode()
        # self.cur.execute(
        #     f'insert into tkeys values("{rand_token}", "{rand_key}");')
        self.conn2.commit()

    def get_key(self, table_token):
        table_token = self.hash_fun(table_token)
        table_token=table_token[3:-3]
        self.cur.execute(f'select tkey from tkeys where id LIKE "___{table_token}___";')
        key = self.cur.fetchall()[0][0]
        # key = base64.b85decode(key.encode()).decode()
        print(key)
        return key

    def enc(self,data,key):
        obj=Fernet(key)
        data=obj.encrypt(data.encode()).decode()
        return data

    def dcrpt(self, data,key):
        obj=Fernet(key.encode())
        data=obj.decrypt(data.encode()).decode()
        return data


# print(Encrypt().hash_fun(12))
# print(Encrypt().hash_fun("9621100179", False))
