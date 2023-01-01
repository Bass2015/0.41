# 0.41

## Accesing the database
In the `data` folder, there's a module named `database`, which will contain all the methods needed to get information from the data base. There will be methods to retrieve specific data using SQL. 

To use it in a notebook or script in your personal folder, first you have to execute the following code:

``` Python
import sys
sys.path.append('..')
import data.database as db
```

That piece of code will import the database module. At this moment, the only method is `get_connection`, which returns a connection to the remote database where all the data is. 

The username, password, database, host and port needed to get the connection are written in the file `config.ini`. Here below there's the method to get that information, but everything is already coded in `get_connection`, so that's the only method you need to get the connection if you want to do your own queries. 

```Python
from configparser import ConfigParser

config = ConfigParser()
config.read('../config.ini')  # <- that in case you're in your personal folder
db_info = config['DATABASE']
conn = db.get_connection(db_info) # This is the connection with the database
```

> Obviously, in a normal project I should have not pushed that config file, with the password to access a database. But as this is just a practice project, and the data is not sensitive, we can leave it as it is and everybody can create the connection to the database

I will write methods to retrieve specific data from the database, and return it as pandas Dataframes. If you need a specific method just write it here in pseudocode. (in suggested methods)

### Suggested methods.
