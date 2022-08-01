#run the flask app 

export FLASK_APP=myproject/
export FLASK_DEBUG=1
flask run

#kill port if already running
sudo fuser -k 5000/tcp

#database creation(execute the below code in python)

from FlaskApp.models import <tables>
from FlaskApp import db, create_app
db.create_all(app=create_app())
