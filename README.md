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
### Creating a database
In this quick start, we will import a database from a CSV file. You can just run the following command:
```bash
python3 example.py
```
This will create a database called `MainDatabase` and will import the data from the CSV file `http://winterolympicsmedals.com/medals.csv`
You will see the following output:
```bash
'Year' | 'City' | 'Sport' | 'Discipline' | 'NOC' | 'Event' | 'Event_gender' | 'Medal'
Database MainDataBase saved to example_data\database.edb
```

### Querying the database
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
Oh! It seems that we have an error, we can not see anything. This is because we are actually selecting the data but not printing it. To print the data, we will use the `;` clause. The `;` clause is used to print the data. 
Try to run the following query:
```javascript
SELECT *;
```
Now we receive the following output:
```bash
----------------
0 results shown
```
That´s okay, `MainTable` is an empty table. Let's try to query the `medals` table.
```javascript
CHECKOUT medals
SELECT *;
```
Now we receive the following output:
```bash
0: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'M'               | 'Silver'
1: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'W'               | 'Gold'
2: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'pairs'           | 'X'               | 'Gold'  
3: '1924'            | 'Chamonix'        | 'Bobsleigh'       | 'Bobsleigh'       | 'BEL'             | 'four-man'        | 'M'               | 'Bronze'
4: '1924'            | 'Chamonix'        | 'Ice Hockey'      | 'Ice Hockey'      | 'CAN'             | 'ice hockey'      | 'M'               | 'Gold'  
5: '1924'            | 'Chamonix'        | 'Biathlon'        | 'Biathlon'        | 'FIN'             | 'military patrol' | 'M'               | 'Silver'
6: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'FIN'             | 'pairs'           | 'X'               | 'Silver'
7: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '10000m'          | 'M'               | 'Gold'
8: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '10000m'          | 'M'               | 'Silver'
9: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '1500m'           | 'M'               | 'Gold'
-------------------
10 results shown
2301 results hidden
```
Now we can see the data from the `medals` table. We can see that we have 2311 results, but we can only see 10. This is because we have a limit of 10 results. We will see how to change this limit later.

### Printing the last selection
As we have seen, we can print the data from a selection using the `;` clause. But what if we want to print the data from the last selection?
In every case, we can use `;` to print the data from the last selection.
We can also use it as a complete statement, doubling the `;` character.
```javascript
;;
```
In this case, we will print the data from the selection of the last section:
```bash
0: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'M'               | 'Silver'
1: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'W'               | 'Gold'
2: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'pairs'           | 'X'               | 'Gold'  
3: '1924'            | 'Chamonix'        | 'Bobsleigh'       | 'Bobsleigh'       | 'BEL'             | 'four-man'        | 'M'               | 'Bronze'
4: '1924'            | 'Chamonix'        | 'Ice Hockey'      | 'Ice Hockey'      | 'CAN'             | 'ice hockey'      | 'M'               | 'Gold'  
5: '1924'            | 'Chamonix'        | 'Biathlon'        | 'Biathlon'        | 'FIN'             | 'military patrol' | 'M'               | 'Silver'
6: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'FIN'             | 'pairs'           | 'X'               | 'Silver'
7: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '10000m'          | 'M'               | 'Gold'
8: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '10000m'          | 'M'               | 'Silver'
9: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '1500m'           | 'M'               | 'Gold'
-------------------
10 results shown
2301 results hidden
```
The `;;` clause will be useful when we want to print the data from the last selection when we can not simply add the `;` clause to the end of the selection.
#### Global clauses and Env clauses
There are two types of clauses: Global clauses and Env clauses. Global clauses are used to modify the behavior of the database. Env clauses are used to modify the behavior of the current table. We will see the global clauses first.

When we use a global clause, adding a `;` clause at the end of the statement will not print the data from the last selection. This is because the global clause is not at the environment level, but at the database level. The `;` clause is at the environment level, so it will not print the data from the last selection.
Even though, we can use the `;;` clause to print the data from the last selection, as we have seen before.

For example, `CHECKOUT` is a global clause. Then, if we use `CHECKOUT` and then the complete clause `;;`, we will be printing the data from the last selection.
```javascript
CHECKOUT MainTable ;;
```
We will receive the following output:
```bash
0: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'M'               | 'Silver'
1: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'W'               | 'Gold'
2: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'pairs'           | 'X'               | 'Gold'  
3: '1924'            | 'Chamonix'        | 'Bobsleigh'       | 'Bobsleigh'       | 'BEL'             | 'four-man'        | 'M'               | 'Bronze'
4: '1924'            | 'Chamonix'        | 'Ice Hockey'      | 'Ice Hockey'      | 'CAN'             | 'ice hockey'      | 'M'               | 'Gold'  
5: '1924'            | 'Chamonix'        | 'Biathlon'        | 'Biathlon'        | 'FIN'             | 'military patrol' | 'M'               | 'Silver'
6: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'FIN'             | 'pairs'           | 'X'               | 'Silver'
7: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '10000m'          | 'M'               | 'Gold'
8: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '10000m'          | 'M'               | 'Silver'
9: '1924'            | 'Chamonix'        | 'Skating'         | 'Speed skating'   | 'FIN'             | '1500m'           | 'M'               | 'Gold'
-------------------
10 results shown
2301 results hidden
```
### Selecting specific rows
We can select specific rows from a table using the `WHERE` clause. The `WHERE` clause is used to filter the data from the table. We can use the `WHERE` clause to select specific rows from the table.
The syntax of the `WHERE` clause is:
```javascript
WHERE value_1 operator value_2
```
Note that we can use the `WHERE` clause only after the `SELECT` clause, and we can use it only once in a selection.
For example, if we want to select the rows from the `medals` table where the `Year` column is equal to `1928`, we can use the following selection:
```javascript
WHERE Year = 1928;
```
We will receive the following output:
```bash
0: '1928'            | 'St. Moritz'      | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'M'               | 'Silver'
1: '1928'            | 'St. Moritz'      | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'W'               | 'Silver'
2: '1928'            | 'St. Moritz'      | 'Skating'         | 'Figure skating'  | 'AUT'             | 'pairs'           | 'X'               | 'Bronze'
3: '1928'            | 'St. Moritz'      | 'Skating'         | 'Figure skating'  | 'AUT'             | 'pairs'           | 'X'               | 'Silver'
4: '1928'            | 'St. Moritz'      | 'Skating'         | 'Figure skating'  | 'BEL'             | 'individual'      | 'M'               | 'Bronze'
5: '1928'            | 'St. Moritz'      | 'Ice Hockey'      | 'Ice Hockey'      | 'CAN'             | 'ice hockey'      | 'M'               | 'Gold'
6: '1928'            | 'St. Moritz'      | 'Skating'         | 'Speed skating'   | 'FIN'             | '1500m'           | 'M'               | 'Gold'
7: '1928'            | 'St. Moritz'      | 'Skating'         | 'Speed skating'   | 'FIN'             | '5000m'           | 'M'               | 'Silver'
8: '1928'            | 'St. Moritz'      | 'Skating'         | 'Speed skating'   | 'FIN'             | '500m'            | 'M'               | 'Bronze'
9: '1928'            | 'St. Moritz'      | 'Skating'         | 'Speed skating'   | 'FIN'             | '500m'            | 'M'               | 'Gold'
-----------------
10 results shown
31 results hidden
```
We can also concatenate multiple conditions using the `AND` operator. For example, if we want to select the rows where the `Year` is greater than `1950`, the `Sport` is equal to `Skating`, and the `Medal` is equal to `Gold`, we can use the following selection:
```javascript
WHERE Year > 1950 AND Sport = 'Skating' AND Medal = 'Gold';
```
We will receive the following output:
```bash
----------------
0 results shown
```
That is because there are no rows that satisfy the conditions. The `WHERE` clause acts as a filter of the *last selection*, then, the engine is concatenating the conditions as follows:
```javascript
Year = 1928 AND Year > 1950 AND Sport = 'Skating' AND Medal = 'Gold';
```
We can see that the first condition and the second condition are not compatible, so the engine will return an empty table. If we want to get the rows where the `Year` is greater than `1950`, the `Sport` is equal to `Skating`, and the `Medal` is equal to `Gold`, we can use the following selection:
```javascript
SELECT *
WHERE Year > 1950 AND Sport = 'Skating' AND Medal = 'Gold';
```
Now, we will receive the following output:
```bash
0: '1952'            | 'Oslo'            | 'Skating'         | 'Figure skating'  | 'GBR'             | 'individual'      | 'W'               | 'Gold'
1: '1952'            | 'Oslo'            | 'Skating'         | 'Figure skating'  | 'GER'             | 'pairs'           | 'X'               | 'Gold'
2: '1952'            | 'Oslo'            | 'Skating'         | 'Speed skating'   | 'NOR'             | '10000m'          | 'M'               | 'Gold'
3: '1952'            | 'Oslo'            | 'Skating'         | 'Speed skating'   | 'NOR'             | '1500m'           | 'M'               | 'Gold'  
4: '1952'            | 'Oslo'            | 'Skating'         | 'Speed skating'   | 'NOR'             | '5000m'           | 'M'               | 'Gold'  
5: '1952'            | 'Oslo'            | 'Skating'         | 'Figure skating'  | 'USA'             | 'individual'      | 'M'               | 'Gold'  
6: '1952'            | 'Oslo'            | 'Skating'         | 'Speed skating'   | 'USA'             | '500m'            | 'M'               | 'Gold'  
7: '1956'            | 'Cortina dAmpezzo' | 'Skating'         | 'Figure skating'  | 'AUT'             | 'pairs'           | 'X'               | 'Gold' 
8: '1956'            | 'Cortina dAmpezzo' | 'Skating'         | 'Speed skating'   | 'SWE'             | '10000m'          | 'M'               | 'Gold'
9: '1956'            | 'Cortina dAmpezzo' | 'Skating'         | 'Speed skating'   | 'URS'             | '1500m'           | 'M'               | 'Gold'
------------------
10 results shown
208 results hidden
```

### Managing tables
We can manage tables using the `CREATE`, `DROP` and `TEMPLATE` statements. The `CREATE` statement is used to create a new table. The `DROP` statement is used to delete a table. The `TEMPLATE` statement is used to modify the headers of the columns of a table.

#### Creating a table
We can create a new table using the `CREATE` statement. The syntax of the `CREATE` statement is:
```javascript
CREATE table_name
```
For example, if we want to create a new table called `income_table`, we can use the following statement:
```javascript
CREATE income_table
```

#### Managing columns
We can name or rename the columns of a table using the `TEMPLATE` statement. The syntax of the `TEMPLATE` statement is:
```javascript
TEMPLATE "column_name_1" "column_name_2" "column_name_3" ...
```
For example, if we want to rename the columns of the `income_table` table, we can use the following statement:
```javascript
TEMPLATE "Name" "Age" "Income"
```
Note that we do not need to specify the data type of the columns. The EQL engine will automatically detect the data type of the columns while filtering the data.

#### Deleting a table
We can delete a table using the `DROP` statement. The syntax of the `DROP` statement is:
```javascript
DROP table_name
```
For example, if we want to delete the `income_table` table, we can use the following statement:
```javascript
DROP income_table
```

### Inserting data
We can insert data into a table using the `INSERT` and `VALUES` statements. The `INSERT` statement is used to insert data into a table. The `VALUES` statement is used to specify the values of the columns of the table.
The syntax of the `INSERT VALUES` statement is:
```javascript
INSERT
VALUES "value_1" "value_2" "value_3" ...
```
If we are inserting strings, we need to use quotation marks. If we are inserting numbers, we must not use quotation marks. For example, let's insert some data into the `MainTable` table:
```javascript
CHECKOUT MainTable
INSERT VALUES "John" 25 10000
INSERT VALUES "Mary" 30 20000
INSERT VALUES "Peter" 35 30000
```
We can see that the `MainTable` table has been updated. If we select all the rows of the `MainTable` table using:
```javascript
SELECT *;
```
we will receive the following output:
```bash
0: 'John'            | 25                | 10000
1: 'Mary'            | 30                | 20000
2: 'Peter'           | 35                | 30000
----------------
3 results shown
```

### Listing useful commands
We can list many useful things using the `LIST` statement. The `LIST` statement is used to list the names, defined clauses and the name of variables. For example, if we want to list the names of the tables, we can use the following statement, as we have seen in a previous section:
```javascript
LIST TABLES
```
Output:
```bash
MainTable
medals
```
If we want to list all the defined clauses, we can use the following statement:
```javascript
LIST CLAUSES
```
At the time of writing this tutorial, the output of the `LIST CLAUSES` statement is:
```bash
;;
AND
CHECKOUT
CLAUSES
CREATE
DROP
ENV
EXIT
GET
GLOBAL
INSERT
LET
LIST
SELECT
SET
TABLES
TEMPLATE
VALUES
WHERE
```
If we want to list the names of the global variables, we can use the following statement:
```javascript
LIST GLOBAL
```
Output:
```bash
NAME
```
If we want to list the names of the env variables, we can use the following statement:
```javascript
LIST ENV
```
Output:
```bash
MAX_RESULTS_SHOWN
MIN_VALUE_LENGTH_SHOWN
```
We can list the env variables only if we are in a table. If we are not in a table, we will receive the following error:
```bash
No table selected
```
We will talk about EQL variables in the next section.

### Using variables
In EQL, we can use variables to store data. We can use the `LET` statement to define a global variable. We can use the `SET` statement to define an env variable. 

Global variables are defined for the whole database. Env variables are defined for the current table. We can use the `GET` statement to get the value of a variable. When we use the `GET` statement, the engine first tries to get the value of the variable from the env variables. If the variable is not defined in the env variables, the engine will try to get the value of the variable from the global variables. If the variable is not defined in the global variables, the engine will return nothing. The result of the `GET` statement is often stored as the last selection of the current table.

#### Defining or modifying global variables
```javascript
CHECKOUT medals
LET MAX_RESULTS_SHOWN 5
```
We will see the following output:
```bash
GLOBAL MAX_RESULTS_SHOWN <- 5
```
We can see that the `MAX_RESULTS_SHOWN` variable has been defined or modified. If we want to get the value of the `MAX_RESULTS_SHOWN` variable, we can use the following statement:
```javascript
GET MAX_RESULTS_SHOWN
```
Output:
```bash
ENV MAX_RESULTS_SHOWN -> 10
```
Note that the result is different because we are using the `LET` statement, the value of the `MAX_RESULTS_SHOWN` is stored in the global variables, but we are getting the value of the `MAX_RESULTS_SHOWN` variable from the env variables. 

#### Defining or modifying env variables
We can modify the value of the `MAX_RESULTS_SHOWN` env variable using the `SET` statement as follows:
```javascript
SET MAX_RESULTS_SHOWN 5
```
We will see the following output:
```bash
ENV MAX_RESULTS_SHOWN <- 5
```
We can see that the `MAX_RESULTS_SHOWN` variable has been defined or modified. If we want to get the value of the `MAX_RESULTS_SHOWN` variable, we can use the following statement:
```javascript
GET MAX_RESULTS_SHOWN
```
Output:
```bash
ENV MAX_RESULTS_SHOWN -> 5
```
Now we can see we have successfully modified the value of the `MAX_RESULTS_SHOWN` env variable!

#### Assigning the last selection to a variable
We can assign the last selection to a variable using the `LET` or `SET` statement, followed by the name of the variable and the clause `*`. For example, if we want to assign the last selection to the `last_selection` global variable, we can use the following statement:
```javascript
SELECT *
LET last_selection *
```
Output:
```bash
LAST_SELECTION <- (
    0: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'M'               | 'Silver'
    1: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'W'               | 'Gold'
    2: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'pairs'           | 'X'               | 'Gold'
    3: '1924'            | 'Chamonix'        | 'Bobsleigh'       | 'Bobsleigh'       | 'BEL'             | 'four-man'        | 'M'               | 'Bronze'
    4: '1924'            | 'Chamonix'        | 'Ice Hockey'      | 'Ice Hockey'      | 'CAN'             | 'ice hockey'      | 'M'               | 'Gold'
    -------------------
    5 results shown
    2306 results hidden
)
```
Note that variable names are not case-sensitive.
We can see the value stored in `last_selection` as we saw in the previous subsections.
```javascript
GET last_selection
```
Output:
```bash
GLOBAL LAST_SELECTION -> (
    0: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'M'               | 'Silver'
    1: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'individual'      | 'W'               | 'Gold'
    2: '1924'            | 'Chamonix'        | 'Skating'         | 'Figure skating'  | 'AUT'             | 'pairs'           | 'X'               | 'Gold'
    3: '1924'            | 'Chamonix'        | 'Bobsleigh'       | 'Bobsleigh'       | 'BEL'             | 'four-man'        | 'M'               | 'Bronze'
    4: '1924'            | 'Chamonix'        | 'Ice Hockey'      | 'Ice Hockey'      | 'CAN'             | 'ice hockey'      | 'M'               | 'Gold'
    -------------------
    5 results shown
    2306 results hidden
)
```

### Exitting and saving the database
We can use the `EXIT` statement to exit the EQL shell. If we are running a database in a `with` python context, the database will be saved automatically.

If we are running the database with the EQL engine, it saves the database automatically when we use the `EXIT` statement, because it uses the python context manager inside.

```javascript
EXIT
```
In this example, we will see the following output:
```bash
Database MainDataBase saved to example_data\database.edb
```