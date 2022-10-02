from concurrent.futures import thread
from mimetypes import init
# import threading
import mysql.connector
import encrypt
# contacts
# key hash fuction
# group id
#


class HandleDatabase:
    def __init__(self):
        print('Yes database')
        self.conn = mysql.connector.connect(user='root',
                                            host='localhost',
                                            port=3306,
                                            password='')
        self.cur = self.conn.cursor()
        self.key = ""
        self.encp = encrypt.Encrypt()
        self.token_dic = {'contact': 50, }
        self.create()

    def create(self):
        print('yes')
        try:
            self.cur.execute('create database assistant')
        except:
            pass
        self.cur.execute('use assistant')
        try:
            self.cur.execute(
                "create table contact(name varchar(50) unique key, p_phone_no varchar(200),s_phone_no varchar(200));")
            # self.cur.execute("create table contact(name varchar(50) unique key, p_phone_no varchar(20),s_phone_no varchar(20));")
            self.key = self.encp.gen_key()
            self.encp.save_key(
                key=self.key, token_table=self.token_dic['contact'])
        except Exception as e:
            print(e)
            pass
        # self.cur.execute(f"insert into contact values(1,'m','m','a');")

    def insert_values(self, s):
        self.cur.execute(s)

    def fetch_number(self, name):
        self.get_key(self.token_dic['contact'])
        print('yes fetch')
        try:
            self.cur.execute(
                f'select p_phone_no,s_phone_no from contact where name = "{name}"')
            num = self.cur.fetchall()[0]
            n=[]
            for i in num:
                if i:
                    n.append(self.encp.dcrpt(i,self.key))
            print(n)
            return n


        except Exception as e:
            print(e)
            pass

    def get_key(self, token):
        self.key = self.encp.get_key(token)

    def load_vcf(self, path='./test_contact.vcf'):
        a = 1
        self.get_key(self.token_dic['contact'])
        num_dict = self.extract(path)
        print(num_dict['mom'])
        print('yes')
        for i in list(num_dict.keys()):
            # print(type(num_dict[i][0]))
            # print(f"{i}:{num_dict[i]}")
            # try:
            if len(num_dict[i]) == 1:
                num = num_dict[i][0]
                num = self.encp.enc(num, self.key)
                self.cur.execute(
                    f"insert into  contact values('{i}','{num}',NULL);")

            else:
                num1 = num_dict[i][0]
                num1 = self.encp.enc(num1, self.key)
                num2 = self.encp.enc(num_dict[i][1], self.key)

                self.cur.execute(
                    f"insert into  contact values('{i}','{num1}','{num2}');")
            # except Exception as e:
            # print(e)
            self.conn.commit()

    def extract(self, path='./test_contact.vcf'):
        d = {}
        n = ""
        pn = ""
        with open(path, 'r') as contact:
            # whitelist = ['FN', 'TEL', 'CELL']
            for line in contact:
                blacklist = ['BEGIN', 'VERSION', 'PHOTO', 'CHARSET']
                if [ele for ele in blacklist if ele in line]:
                    continue
                elif 'FN:' in line:

                    n = line
                    n = n.replace('FN:', "")
                    # n = list(n)
                    n = [i if (i.isalpha() or i.isspace()) else "" for i in n]
                    # print(n)

                    n = "".join(n).strip().lower()
                    # print(n)

                    if n.replace(" ", "").isalpha():
                        # print('yes')
                        if n not in d:
                            # print(n)
                            d[n] = []

                elif 'CELL' in line or 'TEL' in line or 'PREF' in line:
                    pn = line

                    pn = pn.split(':')[1]
                    pn = pn.split(';')
                    if len(pn) > 1:
                        pn = pn[1]
                    pn = ''.join(pn).strip()

                    if pn[0] != '+' and len(pn) == 10:
                        pn = "+91"+pn

                    if n:
                        if len(d[n]) < 2:
                            d[n].append(pn)
                        # with open('./temp.txt', 'a')as temp:
                        #     temp.write(f'{n} : {pn}\n')
                else:
                    continue
            for i in list(d.keys()):
                d[i] = list(set(d[i]))
            return d


# HandleDatabase()
# HandleDatabase().load_vcf()
# print(HandleDatabase().fetch_number('mom'))

# extract()
