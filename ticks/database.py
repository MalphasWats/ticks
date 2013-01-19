import psycopg2

import instruments.database as db

def create_tables():

    schema = """
        
    """

    db.execute_query(schema)