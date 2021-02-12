from flask import Flask, render_template, request, flash, redirect, session

import os
import requests
import crud
from model import connect_to_db

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """non post method of homepage """

    return render_template ('homepage.html')

@app.route('/', methods=['POST'])
def log_in():
    """displays homepage and log in"""

    form_email = request.form.get("login_email")
    form_password = request.form.get("login_password")

    user = crud.get_user_by_email(form_email)
    print("*******", user)

    if user != None:
        flash(f"no user with the {form_email} found! try making an account!")
        

    else:
        flash(f"logging in!")
        print(user)
        return render_template('account.html',
                         user=user)
    
    return redirect('/')   


@app.route('/create_account', methods=['POST'])
def create_user():
    """page to create a new account"""

    #if statement to check if you have an account

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")
    over_21 = request.form.get("over_21")
    user_zipcode = request.form.get("user_zipcode")

    render_template ('create_account.html',
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    over_21=over_21,
                    user_zipcode=user_zipcode)

@app.route('/account')
def user_account_page():
    """lists info about the users account
        including preferences and fav restaurants"""
    
    # request.args.get("")

    render_template ('account.html')

# @app.route('/account', methods=['POST'])
# def 

@app.route('/search')
def search():
    """takes in info about what to search yelp for """

    render_template ('search.html')

@app.route('/search_results')
def rando_results():
    """shows the chosen results from the search"""

    render_template ('search_results.html')



@app.route('/all_results')
def search_results():
    """shows a list of all the results from the search"""

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)