from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    '''
    if request.method == 'POST':
        ##note = request.form.get('note')
        data = request.get_json()
        note_Heading = data.get('noteHeading')
        note_Content = data.get('noteContent')
        if len(note_Heading or note_Content) < 1:
            flash('Cannot post an empty note!', category='invalid_entry')
        else:
            ##new_note = Note(data=note, userId=current_user.id)
            new_note= Note(noteHeading=note_Heading, noteContent=note_Content, userId=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    ##return render_template("home.html", user=current_user)
    '''
    return render_template("dashboard.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.userId == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})

@views.route('/add-note', methods=['POST'])
@login_required
def add_note():
    data = request.get_json()

    note_heading = data.get('noteHeading')
    note_content = data.get('noteContent')

    if len(note_heading or note_content) < 1:
        flash('Cannot post an empty note!', category='invalid_entry')
        return jsonify({'error': 'Cannot add an empty note!'}), 400
    else: 
        new_note = Note(noteHeading=note_heading, noteContent=note_content, userId=current_user.id)

        db.session.add(new_note)
        db.session.commit()

        print('Note added successfully!')
        flash('Note added!', category='success')

    return jsonify({'message': 'Note added successfully!'})
    ##return render_template("dashboard.html", user=current_user)

