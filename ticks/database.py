import psycopg2
import datetime

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
    
    
def save_tick(content, project_id=None, task_id=None):
    if task_id:
        # update existing task
        pass
    else:
        query = """INSERT INTO ticks (task_content) VALUES (%s) RETURNING task_id;"""
    
        task_id = db.execute_query(query, (content,))
    
        if project_id:
            query = """INSERT INTO ticks_projects VALUES(%s,%s) RETURNING project_id;"""
            db.execute_query(query, (project, task_id))
        
    return task_id
    
    
def toggle_complete_tick(task_id):
    pass
    
    
def get_incomplete_ticks():
    query = """
            SELECT task_id, task_content
            FROM ticks 
            WHERE completed IS NULL
            OR completed > %s;"""
    
    twelve_hours_ago = datetime.datetime.now() - datetime.timedelta(hours=12)
    tasks = db.execute_query(query, (twelve_hours_ago,))
    
    return tasks
    
    
def get_projects():
    pass
    
    
def save_project(project_name):
    pass