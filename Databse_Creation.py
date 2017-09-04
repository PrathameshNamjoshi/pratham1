import csv, sqlite3
from pprint import pprint
sql_file="Mumbai_india.db"
con = sqlite3.connect(sql_file)
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS nodes;''')
con.commit()


cur.execute("CREATE TABLE nodes(id INTEGER, lat REAL, lon REAL, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp DATE);") # use your column names here
con.commit()
with open('nodes.csv','rb') as thr: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(thr) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"),i['lat'].decode("utf-8"),i['lon'].decode("utf-8"),i['user'].decode("utf-8"),i['uid'].decode("utf-8"),i['version'].decode("utf-8"),i['changeset'].decode("utf-8"),i['timestamp'].decode("utf-8")) for i in dr]

cur.executemany("INSERT INTO nodes (id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?,?,?);", to_db)
con.commit()
#con.close()


cur.execute('''DROP TABLE IF EXISTS nodes_tags;''')
con.commit()

cur.execute("CREATE TABLE Nodes_tags (id INTEGER, key TEXT, value TEXT, type TEXT);") # use your column names here
con.commit()
with open('nodes_tags.csv','rb') as thr: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(thr) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"),i['key'].decode("utf-8"),i['value'].decode("utf-8"),i['type'].decode("utf-8")) for i in dr]

cur.executemany("INSERT INTO Nodes_tags (id, key, value, type) VALUES (?,?,?,?);", to_db)
con.commit()

cur.execute('''DROP TABLE IF EXISTS ways;''')
con.commit()


cur.execute("CREATE TABLE ways (id INTEGER, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp DATE);") # use your column names here
con.commit()
with open('ways.csv','rb') as thr: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(thr) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"),i['user'].decode("utf-8"),i['uid'].decode("utf-8"),i['version'].decode("utf-8"),i['changeset'].decode("utf-8"),i['timestamp'].decode("utf-8")) for i in dr]

cur.executemany("INSERT INTO ways (id , user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?);", to_db)
con.commit()


cur.execute('''DROP TABLE IF EXISTS ways_tags;''')
con.commit()


cur.execute("CREATE TABLE ways_tags (id INTEGER, key TEXT, value TEXT, type TEXT);") # use your column names here
con.commit()
with open('ways_tags.csv','rb') as thr: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(thr) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"),i['key'].decode("utf-8"),i['value'].decode("utf-8"),i['type'].decode("utf-8")) for i in dr]


cur.executemany("INSERT INTO ways_tags (id, key, value, type) VALUES (?,?,?,?);", to_db)
con.commit()



cur.execute('''DROP TABLE IF EXISTS ways_nodes;''')
con.commit()

cur.execute("CREATE TABLE ways_nodes (id INTEGER, node_id INTEGER, position INTEGER);") # use your column names here
con.commit()
with open('ways_nodes.csv','rb') as thr: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(thr) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"),i['node_id'].decode("utf-8"),i['position'].decode("utf-8")) for i in dr]

cur.executemany("INSERT INTO ways_nodes (id, node_id, position) VALUES (?,?,?);", to_db)
con.commit()
