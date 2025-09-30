from flask import Flask, request, render_template
import numpy as np
import joblib as jb

app = Flask(__name__)
model = jb.load(r"C:\Users\Tashfeen Subhani\OneDrive\Documents\GitHub\practisedatascientist\practising my projects\iris prediction\iris_model.pkl")
@app.route("/")

def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])
        
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(features)
        mapping = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}
        predicted_species = mapping[prediction[0]]
        
        return render_template("index.html", prediction_text=f"Predicted Iris Specie: {predicted_species}")
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
