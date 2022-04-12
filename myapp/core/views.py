from flask import render_template, request, Blueprint
from myapp.models import Event

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    event_posts = Event.query.order_by(Event.date.desc()).paginate(page=page, per_page=6)
    return render_template('index.html', event_posts=event_posts)

@core.route('/info')
def info():
    return render_template('info.html')