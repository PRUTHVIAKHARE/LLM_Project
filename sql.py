import sqlite3

# connect to sqlite
connection = sqlite3.connect("Employee.db")

# Create a curosr object to insert record, create tables, retrieve
cursor = connection.cursor()

# create table
table_info='''
CREATE TABLE Employee (
    Employeeid int,
    Name varchar(255),
    Department varchar(255),
    Salary int,
    City varchar(255)
);

'''

cursor.execute(table_info)

# insert records
cursor.execute('''INSERT INTO Employee values(1001,"Priya","R&D",900000,"Bangalore")''')
cursor.execute('''INSERT INTO Employee values(1001,"Ansh","Data Science",700000,"Bangalore")''')
cursor.execute('''INSERT INTO Employee values(1001,"Dev","R&D",700000,"Chennai")''')
cursor.execute('''INSERT INTO Employee values(1001,"Rohan","Accounting",560000,"Chennai")''')
cursor.execute('''INSERT INTO Employee values(1001,"Harry","Operations",100000,"Bangalore")''')
cursor.execute('''INSERT INTO Employee values(1001,"Shudha","Sales",700000,"Bangalore")''')
cursor.execute('''INSERT INTO Employee values(1001,"Krish","Accounting",800000,"Hydrabad")''')
cursor.execute('''INSERT INTO Employee values(1001,"Amit","Data Science",600000,"Bangalore")''')
cursor.execute('''INSERT INTO Employee values(1001,"Raj","R&D",900000,"Bangalore")''')
cursor.execute('''INSERT INTO Employee values(1001,"Neha","Machine Learning",500000,"Bangalore")''')
cursor.execute('''INSERT INTO Employee values(1001,"Shiv","Finance",500000,"Hydrabad")''')

# display all records
print("Inserted records")

data = cursor.execute('''SELECT * FROM Employee''')

for row in data:
    print(row)

# always close the connection
cursor.commit()
cursor.close()