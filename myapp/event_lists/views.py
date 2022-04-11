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


@event_lists.route('/<int:event_list_id>')
def event_list(event_list_id):
    event_list = Event.query.get_or_404(event_list_id) 
    return render_template('event_list.html', title=event_list.title, date=event_list.date, list=event_list)    

@event_lists.route('/<int:event_list_id>/update',methods=['GET','POST'])
@login_required
def update(event_list_id):
    event_list = EventForm.query.get_or_404(event_list_id)

    if event_list.author != current_user:
        abort(403)

    form = EventForm()

    if form.validate_on_submit():
        event_list.title = form.title.data
        event_list.text = form.text.data
        db.session.commit()
        flash('Event Post Updated')
        return redirect(url_for('event_lists.event_list',event_list_id=event_list.id))

    elif request.method == 'GET':
        form.title.data = event_list.title
        form.text.data = event_list.text

    return render_template('create_post.html',title='Updating',form=form)    


@event_lists.route('/<int:event_list_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(event_list_id):

    blog_post = Event.query.get_or_404(event_list_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(event_list)
    db.session.commit()
    flash('Event Post Deleted')
    return redirect(url_for('core.index'))