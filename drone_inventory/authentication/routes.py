from flask import Blueprint, render_template, flash, redirect, request, url_for
from sqlalchemy import except_all

# project files imports
from drone_inventory.forms import UserLoginForm
from drone_inventory.models import User, db

auth = Blueprint('auth', __name__, template_folder='auths')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(email, password = password)
            db.session.add(user)
            db.session.commit()
            


            flash(f'You have successfully created a user account for {email}.', 'user-created')
            return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please check your form.')

    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    return render_template('signin.html', form=form)