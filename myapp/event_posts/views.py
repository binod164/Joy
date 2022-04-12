from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Event
from myapp.event_posts.forms import EventForm

event_posts = Blueprint('event_posts', __name__)

@event_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = EventForm()
    if form.validate_on_submit():
        event_post = Event(title=form.title.data, image_url=form.image_url.data, text=form.text.data, location=form.location.data, eventdate=form.eventdate.data, user_id=current_user.id)
        db.session.add(event_post)
        db.session.commit()
        flash('Event Post Created')
        print('Event post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)


@event_posts.route('/<int:event_post_id>')
def event_post(event_post_id):
    event_post = Event.query.get_or_404(event_post_id) 
    return render_template('event_post.html', title=event_post.title, date=event_post.date, post=event_post)    

@event_posts.route('/<int:event_post_id>/update',methods=['GET','POST'])
@login_required
def update(event_post_id):
    event_post = Event.query.get_or_404(event_post_id)

    if event_post.organizer != current_user:
        abort(403)

    form = EventForm()

    if form.validate_on_submit():
        event_post.title = form.title.data
        event_post.image_url = form.image_url.data
        event_post.text = form.text.data
        event_post.location = form.location.data
        event_post.eventdate = form.eventdate.data
        
        db.session.commit()
        flash('Event Post Updated')
        return redirect(url_for('event_posts.event_post',event_post_id=event_post.id))

    elif request.method == 'GET':
        form.title.data = event_post.title
        form.text.data = event_post.text
        form.image_url.data = event_post.image_url
        form.location.data = event_post.location
        form.eventdate.data = event_post.eventdate


    return render_template('create_post.html',title='Updating',form=form)    


@event_posts.route('/<int:event_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(event_post_id):

    event_post = Event.query.get_or_404(event_post_id)
    if event_post.organizer != current_user:
        abort(403)

    db.session.delete(event_post)
    db.session.commit()
    flash('Event Post Deleted')
    return redirect(url_for('core.index'))