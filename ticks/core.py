from flask import request, session, g, redirect, url_for, abort, render_template, flash, jsonify, Response, make_response

#un-comment if public_endpoints needed.
#from instruments.core import public_endpoint

from ticks import blueprint
import database
                   

@blueprint.route('/')
def index():
    return render_template('ticks.html')
    
    
@blueprint.route('/save')
def save_todo_item():
    pass
    
    
@blueprint.route('/create_tables')
def create_tables():
    if not database.tables_created():
        database.create_tables()
        flash("Tables were created", category='info')
    else:
        flash("Tables already exist!", category='error')
    return redirect(url_for('ticks.index'))
    
    
def get_content_widget():
    return render_template('ticks_widgets/content_widget.html')
    
    
def get_admin_panel():
    return render_template('ticks_widgets/admin_panel.html', tables_created=database.tables_created())