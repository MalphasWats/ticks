from flask import request, session, g, redirect, url_for, abort, render_template, flash, jsonify, Response, make_response, current_app

#un-comment if public_endpoints needed.
#from instruments.core import public_endpoint

from ticks import blueprint
import database

from markdown import markdown
                   

@blueprint.route('/')
def index():
    ticks = database.get_incomplete_ticks()
    
    current_app.jinja_env.filters['markdown'] = markdown
    return render_template('ticks.html', ticks=ticks)
    
    
@blueprint.route('/save', methods=['POST'])
def save_todo_item():
    task_id = request.form.get('task_id')
    project_id = request.form.get('project_id')
    text = request.form.get('text')
    
    database.save_tick(text, project_id, task_id)
    
    return redirect(url_for('ticks.index'))
    
    
@blueprint.route('/create_tables')
def create_tables():
    if not database.tables_created():
        database.create_tables()
        flash("Tables were created", category='info')
    else:
        flash("Tables already exist!", category='error')
    return redirect(url_for('ticks.index'))
    
    
@blueprint.route('/toggle_complete/<int:task_id>')
def toggle_complete(task_id):
    database.toggle_complete_tick(task_id)
    
    return redirect(url_for('ticks.index', _anchor="tick_%s" % (task_id,)))
    
    
@blueprint.route('/promote/<int:task_id>')
def promote_tick(task_id):
    database.promote_tick(task_id)
    
    return redirect(url_for('ticks.index', _anchor="tick_%s" % (task_id,)))
    
    
@blueprint.route('/demote/<int:task_id>')
def demote_tick(task_id):
    database.demote_tick(task_id)
    
    return redirect(url_for('ticks.index', _anchor="tick_%s" % (task_id,)))
    
    
@blueprint.route('/delete/<int:task_id>')
def delete_tick(task_id):
    database.delete_tick(task_id)
    
    return redirect(url_for('ticks.index'))
    
    
@blueprint.route('/edit/<int:task_id>')
def edit_tick(task_id):
    tick = database.get_tick(task_id)
    ticks = database.get_incomplete_ticks()
    
    current_app.jinja_env.filters['markdown'] = markdown
    return render_template('ticks.html', ticks=ticks, tick=tick[0])
    
    
def get_content_widget():
    return render_template('ticks_widgets/content_widget.html')
    
    
def get_admin_panel():
    return render_template('ticks_widgets/admin_panel.html', tables_created=database.tables_created())