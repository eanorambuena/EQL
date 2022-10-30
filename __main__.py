from query import DataBase

if __name__ == '__main__':
    import codecs
    import csv
    import urllib.request
    
    url = 'http://winterolympicsmedals.com/medals.csv'
    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    csv_content = ""
    for line in csvfile:
        csv_content += ",".join([value.strip() for value in str(line)[1:-1].split(",")]) + "\n"

    db = DataBase()
    db.load_from_csv(csv_content)
        
    while True:
        db.query(input(">>> "))
