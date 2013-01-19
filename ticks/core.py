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
    
    
def get_content_widget():
    return render_template('ticks_widgets/content_widget.html')
    
    
def get_admin_panel():
    return render_template('ticks_widgets/admin_panel.html')