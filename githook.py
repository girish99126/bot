from flask import Flask
from flask import json
from flask import request


app = Flask(__name__)

@app.route("/")
def api_root():
    return "welcome bro"

@app.route('/github',methods=["POST"])
def api_git_message():
    if(request.headers['Content-Type']=="application/json"):
        return json.dumps(request.json)



if __name__ == "__main__":
    app.run(debug=True)

