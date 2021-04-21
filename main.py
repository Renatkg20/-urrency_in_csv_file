import sqlite3
import requests
from bs4 import BeautifulSoup
from beautifultable import BeautifulTable
import re
import pandas as pd

connection = sqlite3.connect('state_numb_cars_kg.db')
c = connection.cursor()
#c.execute("CREATE TABLE cars (ID int, Brand text, Model text);")

for i in c.execute("SELECT * FROM cars;"):
    print(i)


def valuta_kg():
  url = "https://valuta.kg/"
  user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
  source = requests.get(url, headers=user_agent, timeout= 2.50)
  html_doc = source.text
  soup = BeautifulSoup (html_doc,'html.parser')
  soup = soup.find("div", {"class": "container"})
  t = re.sub(r'\s+', ' ', soup.get_text())
  fin4 = t.split(" ")
  tes = " ".join(fin4[7:17])
  # h0=["Валюта"]
  # h1=[fin4[1],fin4[17], fin4[18]]
  # h2=[fin4[2],fin4[19], fin4[20]]
  # h3=[fin4[3],fin4[21], fin4[22]]
  # h4=[fin4[4],fin4[23], fin4[24]]
  # h5=[fin4[5],fin4[25], fin4[26]]
  # h6=[fin4[6],fin4[27], fin4[28]]
 
  # h0.append("Покупка")
  # h0.append("Продажа")

  # table = BeautifulTable()
  # table.column_headers = h0
  # table.column_headers = h0
  # table.append_row(h1)
  # table.append_row(h2)
  # table.append_row(h3)
  # table.append_row(h4)
  # table.append_row(h5)
  # table.append_row(h6)

  df = pd.DataFrame (
    {'USD': [fin4[17], fin4[18]],
     'EURO': [fin4[19], fin4[20]],
     'RUB': [fin4[21], fin4[22]],
     'KZT': [fin4[23], fin4[24]],
     'CNY': [fin4[25], fin4[26]],
     'GBP': [fin4[27], fin4[28]]},
     index = ["Buy", "Sell"])
  #return f"{tes} \n {table}", df
  return  df

print(valuta_kg())

with open("currency.csv", "a") as f: 
     f.write(str(valuta_kg()))



 



















# #c.execute("CREATE TABLE cars_base (ID text, Brand text);")
# # c.execute("CREATE TABLE persons (ID text, Brand text);")
# # def add_numb(str1):
# #     connection = sqlite3.connect("state_numb_cars_kg.db")
# #     c = connection.cursor()
# #     res = str1.split(" ")
# #     a, b, c, d, f = res[0], res[1], res[2],  res[3], res[4]

# #     c.execute(f"INSERT INTO cars_base VALUES ({a}, {b}, {c}, {d}, {f})")
# #     connection.commit()

# # def add_numb():
# #      c.execute("""INSERT INTO cars_base VALUES (1, Honda, 8951BC, White);""")
# #      connection.commit()



# # print(add_numb())

# # c.execute("INSERT INTO cars_base VALUES (1, Honda);")c.execute("INSERT INTO cars_base VALUES (1, Honda);")
# c.execute("INSERT INTO persons VALUES ('John', 'Doe')")
# # a = input('Name ')
# # b = input('Last Name ')
# # c.execute(f"INSERT INTO persons VALUES ('{a}', '{b}')")
# connection.commit()

# # fname = ["Gofaslf", "kfjaksfja", "sfkjaqrwf"]
# # lname = ["Gofasdlf", "kfjaksadffja", "sffafkjaqrwf"]
# # for i, a in zip(fname, lname):
# #     c.execute("INSERT INTO persons VALUES (?, ?)", (i, a))
# #     connection.commit()

# # for row in c.execute("SELECT * FROM cars_base;"):
# #     print(row)
# for row in c.execute("SELECT * FROM persons;"):         print(row)
# # #name = input("Namn: ")
# # #for row in c.execute("SELECT * FROM persons WHERE fname=?", (name,)):
# # #    print(row)

# # connection.close()