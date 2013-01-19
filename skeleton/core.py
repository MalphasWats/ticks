from flask import request, session, g, redirect, url_for, abort, render_template, flash, jsonify, Response, make_response

#un-comment if public_endpoints needed.
#from instruments.core import public_endpoint

from skeleton import blueprint
import database
                   

@blueprint.route('/')
def index():
    return render_template('skeleton.html')
    
    
def get_content_widget():
    return render_template('skeleton_widgets/content_widget.html')