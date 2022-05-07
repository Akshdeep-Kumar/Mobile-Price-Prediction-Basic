from flask import Flask, render_template, request
import pickle
import numpy as np
model=pickle.load(open(r'C:\Users\hp\Desktop\ML_Project\flaskenv\model.pkl', 'rb'))

app=Flask(__name__)
@app.route("/")

def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    values=[int(x) for x in request.form.values()]
    final=np.array(values)
    prediction=model.predict(final.reshape(1,-1))
    output=prediction[0]
    return render_template('index.html', sent_value=f"expected mobile price {output}")

if __name__=="__main__":
    app.run(debug=True)
    