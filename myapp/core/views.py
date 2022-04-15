from flask import render_template, request, Blueprint
from myapp.models import Event
from flask import request

core = Blueprint('core', __name__)

@core.route('/')
def info():
    return render_template('info.html')

@core.route('/index')
def index():
    term = request.args.get('term')
    if term:
        page = request.args.get('page', 1, type=int)
        event_posts = Event.query.filter(Event.location.contains(term) | Event.title.contains(term)).paginate(page=page, per_page=6)
    else:    
        page = request.args.get('page', 1, type=int)
        event_posts = Event.query.order_by(Event.date.desc()).paginate(page=page, per_page=6)
    return render_template('index.html', event_posts=event_posts)
