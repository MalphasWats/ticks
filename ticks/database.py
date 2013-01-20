import psycopg2

import instruments.database as db

def create_tables():

    schema = """
    CREATE TABLE ticks
    (
        task_id SERIAL PRIMARY KEY,
        task_content TEXT NOT NULL,
        created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        completed timestamp DEFAULT NULL
    );

    CREATE TABLE ticks_projects
    (
        project_id SERIAL PRIMARY KEY,
        project_name TEXT NOT NULL
    );
    CREATE INDEX ticks_project_name on ticks_projects(project_name);

    CREATE TABLE project_ticks
    (
        project_id INTEGER NOT NULL,
        task_id INTEGER NOT NULL,
        PRIMARY KEY (project_id, task_id)
    );"""

    db.execute_query(schema)
    
    
def tables_created():
    
    query = """
    SELECT relname FROM pg_class 
    WHERE relname = 'ticks'
    OR relname = 'ticks_projects'
    OR relname = 'projects_ticks';
    """
    
    result = db.execute_query(query)
    
    if result:
        return True
        
    return False