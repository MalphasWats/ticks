from flask import Blueprint, render_template

blueprint = Blueprint('skeleton', __name__, template_folder='templates', static_folder='static')

LABEL = 'skeleton'
ADMIN_LABEL = 'Skeleton Admin'
ICON = 'asterisk'

import skeleton.core

def get_admin_panel():
    return render_template('skeleton_widgets/admin_panel.html')
    
    
from skeleton.core import get_content_widget