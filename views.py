from flask import Blueprint, render_template, request
from flask_login import current_user
import requests

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

            return render_template('index.html', hero_info=hero, user=current_user) 
        
        else:
            error = hero_info['error']
            return render_template('index.html', error=error, user=current_user)

    return render_template('index.html', user=current_user)


@views.route('/account')
def account():
    return render_template('account.html', user=current_user)


@views.route('/about')
def about():
    return render_template('about.html', user=current_user)


@views.route('/contact')
def contact():
    return render_template('contact.html', user=current_user)
