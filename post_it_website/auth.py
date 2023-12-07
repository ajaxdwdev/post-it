from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Welcome back ' + user.firstName + '!', category = 'success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect credentials', category='invalid_entry')
        else:
            flash('User does not exist', category ='invalid_entry')

    return render_template("login.html", boolean=True)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        data = request.form.to_dict()

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Account already exists!', category='invalid_entry')
        elif len(email) < 4 :
            flash('Email is too short!', category='invalid_entry')
        elif len(firstName) < 2:
            flash('Please enter a valid name!', category='invalid_entry')
        elif len(lastName) < 2:
            flash('Please enter a valid last name!', category='invalid_entry')
        elif password != confirmPassword:
            flash('Passwords do not match!', category='invalid_entry')
        elif len(password) < 6:
            flash('Please enter a password longer than 6 characters!', category='invalid_entry')
        else:
            newUser = User(email=email, firstName=firstName, lastName=lastName, password=generate_password_hash(password, method='scrypt'))
            db.session.add(newUser)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))


    return render_template("sign_up.html")