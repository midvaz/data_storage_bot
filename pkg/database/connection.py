
import asyncpg

import logging
from pkg.config import config

def get_connection(cnf: config.Config): 
    try:
        with asyncpg.connect(
            user=cnf.db.user,  
            password=cnf.db.password,
            database=cnf.db.database, 
            host=cnf.db.host, 
            port=cnf.db.port )as conn:

            return conn
        
    except Exception as e:
        logging.error("can't connect to database: ", e)
        exit(1)
