from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Event
from myapp.event_lists.forms import EventForm

event_lists = Blueprint('event_lists', __name__)