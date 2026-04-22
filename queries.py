import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()
#this is query A
print("query A")
rows = cursor.execute("select * from products").fetchall()
for row in rows:
    print(row)
print()

#this is query B
print("query B")
rows = cursor.execute("select name, price from products").fetchall()
for row in rows:
    print(row)
print()

#this is query C
print("query C")
rows = cursor.execute("select * from products where id = 3").fetchall()
for row in rows:
    print(row)
print()

#this is query D
print("query D")
rows = cursor.execute("select * from products where name like '%sheet%'").fetchall()
for row in rows:
    print(row)
print()

#this is query E
print("query E")
rows = cursor.execute("select * from products order by price desc").fetchall()
for row in rows:
    print(row)
print()

#this is query F
print("query F")
rows = cursor.execute("select * from products  order by price desc limit 2").fetchall()
for row in rows:
    print(row)
print()

#this is query G
print("query G")
cursor.execute("update products set price = 38000 where id = 1")
conn.commit()
rows = cursor.execute("select * from products where id = 1").fetchall()
for row in rows:
    print(row)
print()



