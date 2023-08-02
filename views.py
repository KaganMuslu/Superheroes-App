from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
import requests
from models import SUP_User_Heroes, SUP_Heroes
from app import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        hero_name = request.form.get('input_hero')
        hero_info = requests.get(f'https://superheroapi.com/api/2689056404570124/search/{hero_name}').json()


        if hero_info['response'] != 'error':
            results = hero_info['results']
            hero = {}

            for result in results:            
                hero_id = result["id"]
                hero[hero_id] = {}

                hero[result["id"]]['hero_name'] = result["name"]
                hero[result["id"]]['hero_powerstats'] = result["powerstats"]
                hero[result["id"]]['hero_full_name'] = result["biography"]['full-name']
                hero[result["id"]]['hero_image'] = result["image"]
                print(hero)

            return render_template('index.html', hero_info=hero, user=current_user) 
        
        else:
            error = hero_info['error']
            return render_template('index.html', error=error, user=current_user)

    return render_template('index.html', user=current_user)


@views.route('/heroes')
def heroes():
    heroes_query = SUP_User_Heroes.query.filter_by(user_id=current_user.id).all()
    print(heroes_query)

    return render_template('heroes.html', user=current_user)


@views.route('/hero_add/<hero_id>')
def hero_add(hero_id):
    req = requests.get(f'https://superheroapi.com/api/2689056404570124/{hero_id}').json()
    new_hero_db = SUP_Heroes(hero_id=hero_id, name = req['name'],
                                full_name = req['biography']['full-name'],
                                image_url = req['image']['url'],
                                intelligence = req['powerstats']['intelligence'],
                                strength = req['powerstats']['strength'],
                                speed = req['powerstats']['speed'],
                                durability = req['powerstats']['durability'],
                                power = req['powerstats']['power'],
                                combat = req['powerstats']['combat'])
    db.session.add(new_hero_db)

    new_hero_user = SUP_User_Heroes(user_id=current_user.id, hero_id=hero_id)
    db.session.add(new_hero_user)

    db.session.commit()
    
    return redirect(url_for('views.heroes'))


@views.route('/account')
def account():
    return render_template('account.html', user=current_user)


@views.route('/about')
def about():
    return render_template('about.html', user=current_user)


@views.route('/contact')
def contact():
    return render_template('contact.html', user=current_user)
