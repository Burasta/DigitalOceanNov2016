from . import app
from flask import render_template, redirect, url_for, flash, session
from util.forms import ChatRegistration, ChatLogin, Search, AddItem
from util.models import db, User, Item
import json
import hashlib


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/chat/')
def chat():
    return redirect('http://www.appletarsenal.com/chat/')


@app.route('/user/<int:profileid>')
def user(profileid):
    return redirect('http://imythess.com/profile/%d' % profileid)


@app.route('/login/', methods=["GET", "POST"])
def login():
    form = ChatLogin()
    if form.validate_on_submit():
        users = User.query
        hash = hashlib.sha256()
        hash.update(form.userPassword.data.encode('utf-8'))
        password = hash.hexdigest()
        for each in users:
            if form.userName.data == each.userName and password == each.userPassword:
                flash('Successfully logged in!')
                session['user'] = each.userName
                session['userid'] = each.userID
                return redirect(url_for('home'))
            elif form.userName.data == each.userName:
                flash('Incorrect username or password.')
                return render_template('login.html', form=form, user=user)
            else:
                flash('You need to register before signing in!')
                return render_template('login.html', form=form, user=user)
    return render_template('login.html', form=form, user=user)


@app.route('/register/', methods=["GET", "POST"])
def registration():
    user = None
    form = ChatRegistration()
    if form.validate_on_submit():
        users = get_users()
        if form.userName.data in users:
            flash('A user with that name is already registered.')
            return render_template('register.html', form=form, user=user)
        hash = hashlib.sha256()
        user = User()
        user.userName = form.userName.data
        hash.update(form.userPasswordConfirm.data.encode('utf-8'))
        user.userPassword = hash.hexdigest()
        user.userRole = 'AJAX_CHAT_USER'
        db.session.add(user)
        db.session.commit()
        flash('Submitted!')
        return redirect(url_for('registration'))
    return render_template('register.html', form=form, user=user)


@app.route('/search/', methods=["GET", "POST"])
def shopsearch():
    item = None
    form = Search()
    if form.validate_on_submit():
        item = form.search.data
    return render_template('search.html', form=form, item=item)


@app.route('/additems/', methods=["GET", "POST"])
def additems():
    item = None
    form = AddItem()
    if form.validate_on_submit():
        item = Item()
        item.itemName = form.itemName.data
        item.itemDescription = form.itemDescription.data
        item.itemImage = form.itemImage.data
        item.itemShop = form.itemShop.data
        db.session.add(item)
        db.session.commit()
        flash('Submitted!')
        return redirect(url_for('additems'))
    return render_template('additems.html', form=form, item=item)


@app.route('/get_items')
def get_items():
    item_query = Item.query.order_by(Item.itemName.asc())
    result = []
    for each in item_query:
        result.append(each)
    return json.dumps(result)


@app.route('/get_users')
def get_users():
    user_query = User.query.order_by(User.userID.asc())
    result = []
    for each in user_query:
        result.append(each.userName)
    return json.dumps(result)


@app.route('/ozan/')
def ozan_home():
    return render_template('ozan/home.html')


# @app.route('/setupdb')
# def setupdb():
#     db.engine.execute('CREATE TABLE users(userID INTEGER PRIMARY KEY AUTOINCREMENT,\
#                       userName VARCHAR(22),\
#                       userPassword CHAR(64),\
#                       userRole VARCHAR(30))')
#     return json.dumps()
