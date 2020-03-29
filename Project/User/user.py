from flask import Blueprint, render_template, session, request, url_for, redirect, flash, jsonify
from flask_login import logout_user
from Project import app
from flask_user import roles_required, login_required, current_user
from ..checker import url_checker
from ..Models.models import *

user = Blueprint('user', __name__, template_folder='user_template', static_folder='user_static', url_prefix='/user')

@user.route('homepage')
# @login_required
def user_homepage():
    return render_template("user_homepage.html")

@user.route('test', methods=["POST", "GET"])
def url_check():
    if request.method == "POST":
        url = request.form.get("url")
        result = url_checker(url)
        print(result)
    return render_template("user_result.html")

