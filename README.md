# krip_funcs
Custom functions created by kripaar (krip_V)
___
# sqlite.py
* The `database` and `table` objects are inside for now  
### Quick Example
```py
from kripfunc.sqlite import database

db = database()  # Leave parameter blank => storing everything in ram, not opening any file

table = db.create_table("credit_card", {"card_number": "INT NON NULL", "expire": "TEXT", "CVC": "CHAR(3)"})

table.append(1234567890123456, "07/21", "051")
table.append_many((2345678901234567, "08/31", "028"), (3456789012345678, "10/01", "777"))

print(table.get())   # (1234567890123456, '07/21', '051')
print(table.get(0))  # [(1234567890123456, '07/21', '051'), (2345678901234567, '08/31', '028'), (3456789012345678, '10/01', '777')]
print(table.get(2))  # [(1234567890123456, '07/21', '051'), (2345678901234567, '08/31', '028')]
```

# commander.py
* Convert a command-line form of string into running your commands
### Quick Example
```py
from kripfunc.commander import Commander

c = Commander("/")

@c.command(name="money")
def bank():
    print("You have no balance in your bank account")

@c.command(parent="money")
def top():
    print("The top is Li Ka Shing")

@c.command(name="give", parent="money")
def i_had_loan_from(account_payable, amount_to_give):
    print(f"You've given ${amount_to_give} to {account_payable}")


c("/money")                               # You have no balance in your bank account
c("/money top")                           # The top is Li Ka Shing
c("/money give \"Kripaar Bank\" 1000")    # You've given $1000 to Kripaar Bank
```

```py
from kripfunc.commander import Commander

c = Commander("Hey, ")

@c.command(name="what")
def a():
    print("What?")


@c.command(name="is", parent="what")
def b():
    print("Hello?")


@c.command(parent="what:is")
def going():
    print("Are you saying?")


@c.command(name="on?", parent="what:is:going")
def on():
    print("You meant \"What's going on?\"? There's nothing weird going on!")


c("Hey, what")                  # What?
c("Hey, what is going on?")     # You meant "What's going on?"? There's nothing weird going on!
```
