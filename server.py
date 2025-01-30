import csv

from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import os
from datetime import datetime

app = Flask(__name__)
print(__name__)

def write_to_db(data):
        with open('./database.txt', mode='a') as db_file:
            db_file.seek(0, os.SEEK_END)
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            za_datetime = datetime.now()
            db_file.write(f'\n{za_datetime},{email},{subject},{message}')
        db_file.close()

def write_to_csv(data):
    with open('./database.csv', mode='a', newline='') as db_2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        za_datetime = datetime.now()
        csv_writer = csv.writer(db_2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([za_datetime,email,subject,message])
    db_2.close()

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_index(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Error saving to database: did not save to database.'
    else:
        return 'something went wrong, try again!'

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')