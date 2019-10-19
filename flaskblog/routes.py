from flaskblog.models import User,Post
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationFrom, LoginForm
from flaskblog import app,db,bcrypt
posts = [
    {
        'author':'abc',
        'title':'blog post 1',
        'content':'bla bla',
        'date_posted':'Oct xx, 20xx'
    }
    ]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About page")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! you are now able to log in', 'success')
        return redirect(url_for("login"))

    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@blog.com" and form.password.data=="password":
            flash("You've been looged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")

    return render_template('login.html',title='Login', form=form)


