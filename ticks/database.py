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
        priority INTEGER DEFAULT 0,
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
        query = """UPDATE ticks SET task_content=%s WHERE task_id=%s"""
        db.execute_query(query, (content,task_id))
        
    else:
        query = """INSERT INTO ticks (task_content) VALUES (%s) RETURNING task_id;"""
        task_id = db.execute_query(query, (content,))
    
    if project_id:
        query = """INSERT INTO ticks_projects VALUES(%s,%s) RETURNING project_id;"""
        db.execute_query(query, (project, task_id))
        
    return task_id
    
    
def toggle_complete_tick(task_id):
    query = """
            UPDATE ticks
            SET completed = CASE
                              WHEN completed IS NULL THEN CURRENT_TIMESTAMP
                              ELSE NULL
                            END
            WHERE task_id=%s;
    """
    db.execute_query(query, (task_id,))
    
    return task_id
    
    
def promote_tick(task_id):
    query = """
            UPDATE ticks
            SET priority = priority + 1
            WHERE task_id=%s;
    """
    db.execute_query(query, (task_id,))
    
    return task_id
    
    
def demote_tick(task_id):
    query = """
            UPDATE ticks
            SET priority = priority - 1
            WHERE task_id=%s;
    """
    db.execute_query(query, (task_id,))
    
    return task_id
    
    
def delete_tick(task_id):
    query = """
            DELETE FROM ticks WHERE task_id=%(tid)s;
            DELETE FROM project_ticks WHERE task_id=%(tid)s;
    """
    db.execute_query(query, {'tid': task_id})
    
    return task_id
    
    
def get_incomplete_ticks():
    query = """
            SELECT task_id, task_content, completed
            FROM ticks 
            WHERE completed IS NULL
            OR completed > %s
            ORDER BY priority DESC, created;"""
    
    eight_hours_ago = datetime.datetime.now() - datetime.timedelta(hours=8)
    tasks = db.execute_query(query, (eight_hours_ago,))
    
    return tasks
    
    
def get_tick(task_id):
    query = """SELECT task_id, task_content FROM ticks WHERE task_id=%s;"""
    return db.execute_query(query, (task_id,))
    
    
def get_projects():
    pass
    
    
def save_project(project_name):
    pass