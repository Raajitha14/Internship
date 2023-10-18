from flask import Flask,render_template,url_for,request,jsonify
from Scrap4_domain import *
#from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route('/scrape',methods=["POST"])
def index():
    #return render_template('index.html') 
    input=request.get_json(force=True)
    print(input["url"])
    print(input)
    visited_links=set()
    visited_emails=set()
    visited_phones=set()
    crawl_website(input["url"],input["url"],visited_links,visited_emails,visited_phones)
    print("crawling completed")
    print(visited_links)
    print(visited_emails)
    print(visited_phones)
    response={"emaillist":list(visited_emails),
              "links":list(visited_links),
              "phonenolist":list(visited_phones)}
    return jsonify(response),200

if __name__=="__main__":
    app.run(debug=True)  
