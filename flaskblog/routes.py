from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/Introduction", methods=['GET', 'POST'])
@login_required
def Introduction():
    return render_template('Introduction.html', title='Introduction')

@app.route("/BalanceSheet", methods=['GET', 'POST'])
@login_required
def BalanceSheet():
    
    if request.method == 'POST':
        id = request.form['id']
        date = request.form['date']

        bs01 = request.form['bs01']
        bs02 = request.form['bs02']
        bs03 = request.form['bs03']
        bs04 = request.form['bs04']
        bs05 = request.form['bs05']
        bs06 = request.form['bs06']
        bs07 = request.form['bs07']
        bs08 = request.form['bs08']
        bs09 = request.form['bs09']
        bs10 = request.form['bs10']
        bs11 = request.form['bs11']
        bs12 = request.form['bs12']
        bs13 = request.form['bs13']
        bs14 = request.form['bs14']
        bs15 = request.form['bs15']
        bs16 = request.form['bs16']
        bs17 = request.form['bs17']
        bs18 = request.form['bs18']
        bs19 = request.form['bs19']
        bs20 = request.form['bs20']
        bs21 = request.form['bs21']
        bs22 = request.form['bs22']
        bs23 = request.form['bs23']
        form = BalanceSheet(id=id,
                            date=date,
                            bs01=bs01,
                            bs02=bs02,
                            bs03=bs03,
                            bs04=bs04,
                            bs05=bs05,
                            bs06=bs06,
                            bs07=bs07,
                            bs08=bs08,
                            bs09=bs09,
                            bs10=bs10,
                            bs11=bs11,
                            bs12=bs12,
                            bs13=bs13,
                            bs14=bs14,
                            bs15=bs15,
                            bs16=bs16,
                            bs17=bs17,
                            bs18=bs18,
                            bs19=bs19,
                            bs20=bs20,
                            bs21=bs21,
                            bs22=bs22,
                            bs23=bs23,)
        db.session.add(form)
        db.session.commit(form)
    return render_template('BalanceSheet.html', title='BalanceSheet')

@app.route("/IncomeStatement", methods=['GET', 'POST'])
@login_required
def IncomeStatement():
    return render_template('IncomeStatement.html', title='IncomeStatement')

@app.route("/CashFlow", methods=['GET', 'POST'])
@login_required
def CashFlow():
    return render_template('CashFlow.html', title='CashFlow')

@app.route("/ConsolidatedBalanceSheet", methods=['GET', 'POST'])
@login_required
def ConsolidatedBalanceSheet():
    return render_template('ConsolidatedBalanceSheet.html', title='ConsolidatedBalanceSheet')

@app.route("/ConsolidatedIncomeStatement", methods=['GET', 'POST'])
@login_required
def ConsolidatedIncomeStatement():
    return render_template('ConsolidatedIncomeStatement.html', title='ConsolidatedIncomeStatement')

@app.route("/ConsolidatedCashFlow", methods=['GET', 'POST'])
@login_required
def ConsolidatedCashFlow():
    return render_template('ConsolidatedCashFlow.html', title='ConsolidatedCashFlow')

@app.route("/Buildings", methods=['GET', 'POST'])
@login_required
def Buildings():
    return render_template('Buildings.html', title='Buildings')

@app.route("/Shareholders", methods=['GET', 'POST'])
@login_required
def Shareholders():
    return render_template('Shareholders.html', title='Shareholders')

@app.route("/BoardMembers", methods=['GET', 'POST'])
@login_required
def BoardMembers():
    return render_template('BoardMembers.html', title='BoardMembers')

@app.route("/HumanResources", methods=['GET', 'POST'])
@login_required
def HumanResources():
    return render_template('HumanResources.html', title='HumanResources')
