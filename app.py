import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'energy_glossary'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'Env value not loaded')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_term')
def get_term():
    return render_template("read.html",
                                result_term=mongo.db.terms.find_one({'term': 'x-ray'},{'_id':0}))



@app.route('/search_terms', methods=['POST'])
def search_terms():
    result = None
    
    #Get the search text from the input box on the navbar (base.html)
    search_text = request.form['search_input']
    #Search the MongoDB database using the search text (exclude the record id from the result)
    try:
        result = mongo.db.terms.find_one({'term': search_text.lower()},{'_id':0})
    except:
        result = {'term':'Error accessing the database ','description':'Check your database access and try again.'}
        print("Error accessing the database")

    # Print an error if no result found, otherwise populate the read.html template with the result
    if not result:
        result = {'term':'No result found for: ' + search_text,'description':'Check your spelling and try again.'}
        print("Error! No result found.")
    else:
        print("Found a database entry for: " + search_text)


    return render_template("read.html",
                                result_term=result)


@app.route('/create_entry', methods=['POST'])
def create_entry():
    terms =  mongo.db.terms
    terms.insert_one(request.form.to_dict())
    return redirect(url_for('get_term'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','5000')),
            debug=True)
