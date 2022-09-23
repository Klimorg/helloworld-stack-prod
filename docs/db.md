# Postgre & pgadmin

## SQLAlchemy

TO be able to discuss between the api and the database, we use SQLAlchemy, which is a widely used python libarary to do it. Whatever database you will use, you will almost always to create these 3 things in SQLAchemy :

1. The Engine,
2. the Metadata.
3. the Databse,

### The Engine

The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections.

```python
from sqlalchemy import create_engine
engine = create_engine(db_uri, echo=True, future=True)
```

```python
from sqlalchemy.ext.asyncio import create_async_engine
engine = create_async_engine(async_db_uri, future=True, echo=False)
```

### The Metadata

### The Database


## Set up Postgre

## Set up pgadmin

## Connect pgadmin to your postgre db


## Sources

* [SQLAclhemy tutorial](https://docs.sqlalchemy.org/en/14/tutorial/index.html)
