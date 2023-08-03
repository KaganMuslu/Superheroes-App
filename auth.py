from flask import render_template, url_for, redirect, Blueprint, request, flash
from flask_login import current_user, login_user, logout_user
from models import SUP_User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('inputUsername')
        password = request.form.get('inputPassword')

        user = SUP_User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                login_user(user, remember=True)
                flash('Giriş Yapıldı!', category='success')
                return redirect(url_for('views.home'))
            
            else:
                flash('Şifreniz Yanlış!', category='error')
                return redirect(url_for('views.account'))
            
        else:
            flash('Kullanıcı Bulunamadı!', category='error')
            return redirect(url_for('views.account'))


@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('inputUsernameNew')
        password = request.form.get('inputPasswordNew')
        user = SUP_User.query.filter_by(username=username).first()

        if user:
            flash('Bu Kullanıcı Adı Mevcut!', category='error')
            return redirect(url_for('views.account'))
    
        elif len(username) > 20 or len(username) < 3:
            flash('Kullanıcı adı 3 ile 20 karakter uzunluğunda olmalıdır!', category='error')
            return redirect(url_for('views.account'))

        elif len(password) > 20 or len(password) < 3:
            flash('Şifreniz 3 ile 20 karakter uzunluğunda olmalıdır!', category='error')
            return redirect(url_for('views.account'))
        
        else:
            new_user = SUP_User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Kayıt Olundu!', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))


@auth.route('/logout')
def logout():
    
    logout_user()
    return redirect(url_for('views.home'))
