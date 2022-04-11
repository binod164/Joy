from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Event
from myapp.event_lists.forms import EventForm

event_lists = Blueprint('event_lists', __name__)

@event_lists.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = EventForm()
    if form.validate_on_submit():
        event_post = Event(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(event_post)
        db.session.commit()
        flash('Event Post Created')
        print('Event post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)