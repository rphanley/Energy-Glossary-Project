"""App to handle CRUD operations for the energy_glossary terms database"""
import os
import re

from dotenv import load_dotenv
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from utils import created_today

load_dotenv(override=True)
APP = Flask(__name__)
APP.config['MONGO_DBNAME'] = 'energy_glossary'
APP.config['MONGO_URI'] = os.getenv('MONGO_URI', 'Env value not loaded')
APP.secret_key = os.getenv('SECRET_KEY')

MONGO = PyMongo(APP)

@APP.route('/')
def home():
    """Home page with search input and display of the most recent database entries."""
    latest = MONGO.db.terms.find().sort('_id', -1).limit(10)
    return render_template("index.html", records=latest)


@APP.route('/search_terms', methods=['POST'])
def search_terms():
    """Posts the search for the requested term and handles the single returned record, or any errors"""
    result = None
    #Get the search text from the input box
    search_text = request.form['search_input']
    #Run a case-insensitive search for a record with term=search_text
    try:
        result = MONGO.db.terms.find_one({'term': re.compile(search_text, re.IGNORECASE)})
    except:
        # Notify the user
        flash('Error accessing the database! Check your database access and try again.')
        return redirect(url_for('home'))
    # Print an error if no result found, otherwise get the result record.
    if not result:
        flash('No result found for: ' + '"' + search_text + '"' + ' .Check your spelling and try again.')
        return redirect(url_for('home'))
    else:
        print("Found a database entry for: " + search_text)
        term_id = result['_id']
        return redirect(url_for('get_record', record_id=term_id))


@APP.route('/terms/<record_id>')
def get_record(record_id):
    """Gets the single found record from the database, checks if it was created today, and passes it for display"""
    badge = ''
    record = MONGO.db.terms.find_one({'_id': ObjectId(record_id)})
    if created_today(record_id):
        badge = 'new badge'
    return render_template("read.html", result_term=record, badge_class=badge)

@APP.route('/terms/new', methods=['GET', 'POST'])
def add():
    """Gets or posts the add term form to insert a new entry in the database."""
    if request.method == 'POST':
        terms = MONGO.db.terms
        # Add a new record
        new_term = request.form.get('term_name')
        terms.insert_one({
            'term':new_term,
            'description':request.form.get('term_description'),
            })
        result = terms.find_one({'term': re.compile(new_term, re.IGNORECASE)})
        flash('Entry for ' + '"' + new_term + '"' + ' created!')
        return render_template("read.html", result_term=result, badge_class='new badge')
    else:
        return render_template('add.html')

#Perform the record update in the database
@APP.route('/terms/<term_id>/edit', methods=['GET', 'POST'])
def update(term_id):
    """Gets or posts the update term form to update an existing entry in the database."""
    if request.method == 'POST':
        terms = MONGO.db.terms
        badge = ''
        #Update the record
        terms.update({'_id': ObjectId(term_id)},
                     {'term':request.form.get('term_name'),
                      'description':request.form.get('term_description'),})
        record = terms.find_one({'_id': ObjectId(term_id)})
        if created_today(term_id):
            badge = 'new badge'
        flash('Entry for ' + '"' + record['term'] + '"' + ' updated!')
        return render_template("read.html", result_term=record, badge_class=badge)
    else:
        term = MONGO.db.terms.find_one({"_id": ObjectId(term_id)})
        return render_template('update.html', term_to_update=term)


@APP.route('/terms/<term_id>/')
def delete(term_id):
    """Deletes the given record from the database."""
    entry = MONGO.db.terms.find_one({"_id": ObjectId(term_id)})
    name = entry['term']
    MONGO.db.terms.delete_one({'_id': ObjectId(term_id)})
    # Notify the user
    flash('Entry for ' + '"' + name + '"' + ' deleted!')
    return redirect(url_for('home'))

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=False)
