import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'energy_glossary'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_term')
def get_term():
    # retdoc=""
    # count=0
    #doc=mongo.db.terms.find_one()
    #doc=mongo.db.terms.find({"term": "x-ray"})
    #if doc:
        #print("")
        #for k, v in doc.items():
        #    print(k + " " + v)
        #         if k != "_id":
        #             count+=1
                
        #             retdoc+= '"'+k+'": '+v
        #             if count < 2:
        #                 retdoc+=","
        
        # print(retdoc)    
         
    return render_template("read.html",
                                found_term=mongo.db.terms.find_one({'term': 'x-ray'},{'_id':0}))


@app.route('/search_terms', methods=['POST'])
def search_terms():
    search_text = request.form['search_input']
    return render_template("read.html",
                                found_term=mongo.db.terms.find_one({"term": search_text.lower()},{'_id':0}))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','5000')),
            debug=True)
