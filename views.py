from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
import requests, random
from models import SUP_User_Heroes, SUP_Heroes
from app import db
from datetime import datetime, timedelta, timezone

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
    hero_list = []

    for hero in heroes_query:
        hero_info = SUP_Heroes.query.filter_by(hero_id=hero.hero_id).first()
        hero_list.append(hero_info)


    return render_template('heroes.html', user=current_user, heroes=hero_list)


@views.route('/hero_add/<hero_id>') #Yıldız Puanı ile Alma Sistemi Eklenecek!
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


@views.route('/random_heroes/<int:random_int>')
def random_heroes(random_int):

    heroes_query = SUP_User_Heroes.query.filter_by(user_id=current_user.id).all()
    hero_id_list = []

    for hero in heroes_query:
        hero_info = SUP_Heroes.query.filter_by(hero_id=hero.hero_id).first()
        hero_id_list.append(hero_info.hero_id)

    x = 0
    while x < random_int:
        random_id = random.randint(1,731)
        if random_id not in hero_id_list:
            req = requests.get(f'https://superheroapi.com/api/2689056404570124/{random_id}').json()
            if req['powerstats']['intelligence'] != 'null' and req['powerstats']['strength'] != 'null' and req['powerstats']['speed'] != 'null' and req['powerstats']['durability'] != 'null' and req['powerstats']['power'] != 'null' and req['powerstats']['combat'] != 'null':
                new_hero_db = SUP_Heroes(hero_id=random_id, name = req['name'],
                                            full_name = req['biography']['full-name'],
                                            image_url = req['image']['url'],
                                            intelligence = req['powerstats']['intelligence'],
                                            strength = req['powerstats']['strength'],
                                            speed = req['powerstats']['speed'],
                                            durability = req['powerstats']['durability'],
                                            power = req['powerstats']['power'],
                                            combat = req['powerstats']['combat'])
                db.session.add(new_hero_db)
                new_hero_user = SUP_User_Heroes(user_id=current_user.id, hero_id=random_id)
                db.session.add(new_hero_user)
                x += 1
                hero_id_list.append(random_id)
        else:
            print(random_id)
            print('Var lan bu hero!')

    db.session.commit()

    return redirect(url_for('views.heroes'))



@views.route('/new_hero', methods=['GET','POST'])
def new_hero():

    last_get_date = SUP_User_Heroes.query.filter_by(user_id=current_user.id).order_by(SUP_User_Heroes.hero_get_date.desc()).first()

    hero_get_date = last_get_date.hero_get_date
    veri_utc = hero_get_date.replace(tzinfo=timezone.utc)

    suanki_zaman_utc = datetime.now(timezone.utc)

    # Veri ile şu anki zaman arasındaki farkı hesaplama
    fark = suanki_zaman_utc - veri_utc

    # 2 saat çıkarma ve geriye kalan zamanı al
    kalan_zaman = timedelta(minutes=15) - fark
    kalan_saatler = kalan_zaman.seconds // 3600
    kalan_dakikalar = (kalan_zaman.seconds // 60) % 60

    # Eğer fark 2 saatten az ise mesaj yazdırma
    if fark <= timedelta(minutes=15):
        if kalan_saatler != 0:
            flash(f'Yeni karakter almaya {kalan_saatler} saat {kalan_dakikalar} dakika kaldı!', category='error')
        else:
            flash(f'Yeni karakter almaya {kalan_dakikalar} dakika kaldı!', category='error')

        return redirect(url_for('views.heroes'))

    else:
        flash(f'2 Yeni Karakter Hazır!', category='success') # yeni karakterlere badge new göster
        
        return redirect(url_for('views.random_heroes', random_int=2))


@views.route('/first_five')
def first_five():
    return redirect(url_for('views.random_heroes', random_int=5))


@views.route('/account')
def account():
    return render_template('account.html', user=current_user)


@views.route('/about')
def about():
    return render_template('about.html', user=current_user)


@views.route('/contact')
def contact():
    return render_template('contact.html', user=current_user)
