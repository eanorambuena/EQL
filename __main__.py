from engine.base import DataBase

if __name__ == '__main__':
    import codecs
    import csv
    import pickle
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
    db.create_table("medals")
    medals = db.use_table("medals")
    medals.load_from_csv(csv_content)
    medals.template(*template)
        
    while True:
        _input = input(">>> ")
        if _input.lower() == "exit":
            db.save("example_data/database.edb")
            break
        db.query(_input)

    print("End")

    with open("example_data/database.edb", "rb") as file:
        db: DataBase = pickle.load(file)
    while True:
        db.query(input(">>> "))
