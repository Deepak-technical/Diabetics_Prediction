from flask import Flask ,request,render_template
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open('diabetics211.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])


        data=np.array([[preg,glucose,bp,st,insulin,bmi,dpf,age]])
        prediction=model.predict(data)

        if(prediction==1):
            prediction="Opps! It Seems That You Have Diabetics"
        else:
            prediction="Great! You Don't Have Diabetics"

        return render_template ("prediction.html",prediction_text="You have: {}".format(prediction))

    else:
        return render_template("prediction.html")

if __name__=="__main__":
    app.run(debug=True)                   