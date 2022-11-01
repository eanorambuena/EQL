import sys

from engine.base import open_database

if len(sys.argv) < 2:
    print("No database file specified")
    sys.exit(1)
path = sys.argv[1]

with open_database(path) as db:
    listening = True
    while listening:
        _input = input(">>> ")
        if _input.lower() == "exit":
            listening = False
        else:
            db.query(_input)
