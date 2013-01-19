from flask import Blueprint, render_template

blueprint = Blueprint('ticks', __name__, template_folder='templates', static_folder='static')

LABEL = 'Ticks'
ADMIN_LABEL = 'ticks'
ICON = 'check'

import ticks.core

def get_admin_panel():
    return render_template('ticks_widgets/admin_panel.html')
    
    
from ticks.core import get_content_widget