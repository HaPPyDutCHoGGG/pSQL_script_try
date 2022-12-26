import psycopg2;
import random as r;

_db = 'mtuci_db';
con = psycopg2.connect(
    database = _db,
    user = 'postgres',
    password = 'psqlmtuci',
    host = '127.0.0.1',
    port = '5432');

print('DB "{0}" connected'.format(_db));
cur = con.cursor();

#region group
cur.execute("CREATE TABLE groups(id SERIAL UNIQUE, name varchar NOT NULL UNIQUE PRIMARY KEY, department varchar NOT NULL, FOREIGN KEY(department) REFERENCES departments(deanery));");
con.commit();
_groups = ['bpm2101', 'bib2201', 'bon2110', 'bos2002']; deps = ['KiiB','SiSS']; 
for i in range(0,4):
    if(i < 2):
        cur.execute("INSERT INTO groups(name,department) VALUES(%s,%s);",(_groups[i],deps[0]));con.commit();
    else:
        cur.execute("INSERT INTO groups(name,department) VALUES(%s,%s);",(_groups[i],deps[1]));con.commit();
con.commit();
#end region



#region students
cur.execute("CREATE TABLE students(id SERIAL UNIQUE, group_name varchar NOT NULL, name varchar NOT NULL UNIQUE, passport varchar NOT NULL, FOREIGN KEY(group_name) REFERENCES groups(name));");
con.commit();
_names = ['Egor', 'Alex', 'Semion', 'Sasha', 'Gleb', 'Gregory', 'Artem', 'Max', 'Maria', 'Victory','unknown', 'Pavel', 'Lilia', 'Igor', 'Sofie', 'Andrew', 'Yuriy', 'Anna', 'Ivan', 'Kristy'];
for i in range(0,20):
    _name = _names[i]; _passp = r.randint(1,10**5); 
    if (i < 5): cur.execute("INSERT INTO students(group_name,name,passport) VALUES(%s,%s,%s);",(_groups[0],_name,_passp));con.commit();
    elif (i < 10): cur.execute("INSERT INTO students(group_name,name,passport) VALUES(%s,%s,%s);",(_groups[1],_name,_passp));con.commit();
    elif (i < 15): cur.execute("INSERT INTO students(group_name,name,passport) VALUES(%s,%s,%s);",(_groups[2],_name,_passp));con.commit();
    elif (i < 20): cur.execute("INSERT INTO students(group_name,name,passport) VALUES(%s,%s,%s);",(_groups[3],_name,_passp));con.commit();
    con.commit();
#end region



#region options
'''
menu = '(1)-create table,(2)-insert,(3)-select,(4)-delete,(5)-update,(6)-exit';
print(menu); option = input();

while (True):
    if (option == 1):
        print('choose a name 4 ur table print a number of fields');
        name = input(); number_of_fields = input(); fields = [];
        for i in range(0,number_of_fields-1):
            _field = str(input()); fields.append(_field);
        cur.execute("CREATE TABLE student_group (id SERIAL PRIMARY KEY)");
        for item in fields:
            cur.execute("ALTER TABLE (%)" %name);
            

    elif (option == 2):
    elif (option == 3):
    elif (option == 4):
    elif (option == 5):
    elif (option == 6): con.commit();break;
'''
#end region
con.close();
