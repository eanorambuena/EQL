from query import DataBase

if __name__ == '__main__':
    import codecs
    import csv
    import urllib.request
    
    url = 'http://winterolympicsmedals.com/medals.csv'
    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    csv_content = ""
    count = 0
    for line in csvfile:
        if count == 0:
            template = [
                value.strip().replace(" ", "_") for value in str(line)[1:-1].split(",")
                ]
        else:
            csv_content += ",".join([value.strip() for value in str(line)[1:-1].split(",")]) + "\n"
        count += 1

    db = DataBase()
    db.load_from_csv(csv_content)
    db.template(*template)
        
    while True:
        db.query(input(">>> "))
