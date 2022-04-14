from crypt import methods
from operator import methodcaller
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from myapp import db
from myapp.models import User
from myapp.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from myapp.models import User, Event
from myapp.event_posts.forms import EventForm


users = Blueprint('users', __name__) # dont forget to register this in __init__.py 

event_posts = Blueprint('event_posts', __name__)

# register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for Registration!')
        return redirect(url_for('users.login'))
    
    return render_template('register.html', form=form)

# login
@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')

            if next ==None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html',form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.info')) 

@users.route('/account')
@login_required
def account():
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(id =current_user.id).first_or_404()
    event_posts = Event.query.filter_by(organizer=user).order_by(Event.date.desc()).paginate(page=page, per_page=6) 
    return render_template('account.html', event_posts=event_posts, user=user)

@users.route('/<username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    event_posts = Event.query.filter_by(organizer=user).order_by(Event.date.desc()).paginate(page=page, per_page=6) 
    return render_template('user_event_posts.html', event_posts=event_posts, user=user)

@event_posts.route('/<int:event_post_id>')
def event_post(event_post_id):
    event_post = Event.query.get_or_404(event_post_id) 
    return render_template('user_event_posts.html', title=event_post.title, date=event_post.date, post=event_post)    
