from query import DataBase

if __name__ == '__main__':
    db = DataBase()
    csv = """
'12344567-8','Miguel',45,3000,'03-24-1977'
'20575479-3','Estefania',22,1200,'07-15-2000'
'10005633-1','Carlos',57,2000,'01-01-1965'
'22487682-4','Dominga',18,234,'12-12-2004'"""

    for line in csv.splitlines():
        line = line.strip()
        if line == '':
            continue
        raw_row = line.split(",")
        row = [value.strip() for value in raw_row]
        db.insert(*row)
        
    while True:
        db.query(input(">>> "))
