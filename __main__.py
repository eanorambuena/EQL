import sys

from engine.base import open_database

source_path = None

if len(sys.argv) < 2:
    print("No database file specified")
    sys.exit(1)
path = sys.argv[1]

if len(sys.argv) > 2:
    source_path = sys.argv[2]

source = []
if source_path:
    with open(source_path, "r", encoding="utf-8") as f:
        source = f.readlines()

with open_database(path) as db:
    listening = True
    while listening:
        if source_path and len(source) > 0:
            _input = source.pop(0)
        elif source_path:
            _input = "EXIT"
        else:
            _input = input(">>> ")
            
        if _input.lower() == "exit":
            listening = False
        else:
            db.query(_input)
