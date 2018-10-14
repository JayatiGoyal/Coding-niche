

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder="./", static_folder='./', static_url_path='')

@app.route('/sendEmail')
def data():
    # url in the browser should be http://127.0.0.1:8000/sendEmail?name=vibhanshimodi
    user = request.args.get('name')
	if (user == "vibhanshimodi"):
	  send_email(codingniche1@gmail.com","coders1234","vibhanshimodi@gmail.com","Luggage update","your luggage has been loaded")
	elif (user == "abhinitmodi"):
	  send_email(codingniche1@gmail.com","coders1234","vibhanshimodi@gmail.com","Luggage update","your luggage has been loaded")
	
if __name__ == '__main__':
  app.debug=True
  app.run(host='0.0.0.0')