from flask import Blueprint, render_template, session, request, url_for, redirect, flash, jsonify
from flask_login import login_required, current_user, logout_user
from ..Models.models import *
from Project import db, app, admin_flask
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
import pandas as pd
import numpy as np
from ..configuration import *
from ..utils.dataset_preprocessing import preprocessing

class DatapreprocessView(BaseView):
    @expose('/')
    def preprocess_dataset(self):
        urldata = pd.read_csv(DATASET_PATH)
        # print(urldata.head(10))

        preprocessed_df = preprocessing(urldata)
        # print(preprocessed_df.head())
        preprocessed_df.to_csv(PREPROCESSED_DATASET)
        print("Test Success")
        return self.render('admin/preprocess.html', endpoint='test')

admin = Blueprint('admin_blueprint', __name__, template_folder='ad_template', static_folder='ad_static', url_prefix='/admin')
admin_flask.add_view(ModelView(Whitelist_url,db.session, name='Whitelist URL'))
admin_flask.add_view(ModelView(Blacklist_url, db.session, name='Blacklist URL'))
admin_flask.add_view(DatapreprocessView(name='Dataset Preprocessing'))
