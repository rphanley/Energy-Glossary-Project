import os
import re

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


load_dotenv(override=True)
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'energy_glossary'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'Env value not loaded')

mongo = PyMongo(app)

record_loaded = False
term_id = None
is_update = False

@app.route('/')
@app.route('/home')
def home():
    global record_loaded
    record_loaded = False
    home_msg = {'term':'Look up an energy term..','description':'Please search for a term, and press Enter.'}
    return render_template("read.html",
                                result_term=home_msg)




@app.route('/search_terms', methods=['POST'])
def search_terms():
    result = None
    global term_id,record_loaded
    record_loaded = False
    
    #Get the search text from the input box on the navbar (base.html)
    search_text = request.form['search_input']
    #Run a case-insensitive search for a record with term=search_text
    try:
        result = mongo.db.terms.find_one({'term': re.compile(search_text, re.IGNORECASE)})
       
    except:
        result = {'term':'Error accessing the database ','description':'Check your database access and try again.'}
        print("Error accessing the database")

    # Print an error if no result found, otherwise populate the read.html template with the result
    if not result:
        result = {'term':'No result found for: ' + search_text,'description':'Check your spelling and try again.'}
        print("Error! No result found.")
    else:
        print("Found a database entry for: " + search_text)
        term_id = result['_id']
        record_loaded = True

   
    return render_template("read.html",
                                result_term=result)


@app.route('/add_update/<mode>')
def add_update(mode):
    global term_id,record_loaded,is_update

    print('Mode is:' + mode)
    # If Update button was clicked, set up to update the loaded record
    if mode == 'update':
        is_update = True
        if record_loaded:
                term_to_update = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
                display_action_name = 'Update'
                display_term_name = term_to_update['term']
                display_term_desc = term_to_update['description']
        else:   # No record loaded yet, display an error message
                no_rec_msg = {'term':'No entry loaded yet','description':'Please search for an entry, then click Update.'}
                return render_template("read.html",
                                result_term=no_rec_msg)
    # Add mode, bring up form for record insertion.
    elif mode == 'add':
        is_update = False
        display_term_name =''
        display_term_desc =''
        display_action_name ='Add'
   
    return render_template('addupdate.html',
                                 form_action=display_action_name,
                                 form_term_name=display_term_name,
                                 form_term_description=display_term_desc)


#Perform the record update or insertion in the database
@app.route('/create_entry', methods=['POST'])
def create_entry():
    global term_id,is_update
    terms =  mongo.db.terms

    if is_update: #Update the record
        terms.update( {'_id': ObjectId(term_id)},
            {
            'term':request.form.get('term_name'),
            'description':request.form.get('term_description'),
            })
        print('Updated record..')
        is_update = False
    else:  # Add a new record
        terms.insert_one({
            'term':request.form.get('term_name'),
            'description':request.form.get('term_description'),
            })
        print('Added record..')

    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    global term_id,record_loaded

    if record_loaded:
            mongo.db.terms.delete_one({'_id': ObjectId(term_id)})
            # Notify the user
            msg = {'term':'Entry deleted!','description':''}
    else:
        # No record loaded yet, display an error message
        msg = {'term':'No entry loaded yet','description':'Please search for an entry, then click Delete.'}

    return render_template("read.html",
                                result_term=msg)
         
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','5000')),
            debug=True)
