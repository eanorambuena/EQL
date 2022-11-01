# EQL
Eanorambuena's Query Language, just for learning

## What is EQL?
EQL is a query language that I'm developing for learning purposes. It's not intended to be used in production.
It's a simple language that allows you to query data from a database.

## How to use it?
You can use it in two ways:
- Using it as a package
- Using the EQL interpreter

### Using the EQL interpreter
1. Clone the repository
```bash
git clone https://github.com/eanorambuena/EQL.git
```
2. Install the dependencies
Currently this project does not have any dependencies, but it is possible that in the future it will have some.
3. Run the interpreter
```bash
python3 EQL
```
4. Write your query
```javascript
>>> CHECKOUT MainTable;
>>> SELECT *;
```

## Quick start
#### Creating a database
In this quick start we will import a database from a CSV file. You can just run the following command:
```bash
python3 example.py
```
This will create a database called `MainDatabase` and will import the data from the CSV file `http://winterolympicsmedals.com/medals.csv`
You will see the following output:
```bash
'Year' | 'City' | 'Sport' | 'Discipline' | 'NOC' | 'Event' | 'Event_gender' | 'Medal'
Database MainDataBase saved to example_data\database.edb
```

#### Querying the database
Now that we have a database, we can query it. To do this, we will use the EQL interpreter. To start the interpreter, just run the following command:
```bash
python3 EQL example_data/example.edb
```
This will start the interpreter and will load the database `example_data/example.edb`. Now we can start querying the database. To do this, we will use the `SELECT` statement. The `SELECT` statement is used to query data from a table. The syntax of the `SELECT` statement is the following:
```javascript
SELECT number_of_columns
```
Where `number_of_columns` is the number of columns that you want to query. If you want to query all the columns, you can use the `*` character.
Try to run the following query:
```javascript
SELECT *
```
You will see the following output:
```bash
No table selected
```
This is because we haven't selected a table. To select a table, we will use the `CHECKOUT` statement. The `CHECKOUT` statement is used to select a table. The syntax of the `CHECKOUT` statement is the following:
```javascript
CHECKOUT table_name
```
Where `table_name` is the name of the table that you want to select.
We can see the tables that are in the database by using the `LIST TABLES` statement.
```javascript
LIST TABLES
```
You will see the following output:
```bash
MainTable
medals
```
Let's select the `MainTable` table.
```javascript
CHECKOUT MainTable
```
Now, we can query the data from the table.
```javascript
SELECT *
```
Oh! It seems that we have an error, we can not see anythig. This is because we are actually selecting the data but not printing it. To print the data, we will use the `;` clause. The `;` clause is used to print the data. 
Try to run the following query:
```javascript
SELECT *;
```
Now we receive the following output:
```bash
----------------
0 results shown
```



