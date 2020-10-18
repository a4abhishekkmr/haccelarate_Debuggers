from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import pyttsx3
import webbrowser

x= pyttsx3.speak("Welcome to Snooz...")
webbrowser.open("http://127.0.0.1:5000/")
app = Flask(__name__)

model=pickle.load(open('mode2.pkl','rb'))


@app.route('/')
def hello_world():
    pyttsx3.speak("Let's get started")
    return render_template("index.html")
    # x= pyttsx3.speak("Welcome to Snooz...")

database={'nachi':'123','james':'aac','karthik':'asdsf'}
@app.route('/Quick_sleep_checkup',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('index.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('index.html',info='Invalid Password')
        else:
	         return render_template('predict.php',name=name1)

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    # print(int_features)
    # print(final)
    prediction=model.predict(final)
    # print(prediction)
    # output='{0:.{1}f}'.format(prediction[0][1], 2)
    return render_template('predict.php',output =prediction )

    if prediction>6.0:
        return render_template('predict.php',pred='You have healthy sleep schedule')
    else:
        return render_template('predict.php',pred='Your need to work hard')


if __name__ == '__main__':
    app.run(debug=True)

#
# "
