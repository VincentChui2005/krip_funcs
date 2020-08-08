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
  
  table.add(1234567890123456, "07/21", 051)
  table.addmany((2345678901234567, "08/31", 028), (3456789012345678, "10/01", 777))
  
  print(table.check())
```
