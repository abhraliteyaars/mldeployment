from flask import Flask,render_template,request
import pickle
import sklearn

app =Flask(__name__)

model =pickle.load(open("models/houseprice.pkl","rb"))

@app.route("/")
def basic_render():
    return render_template("index.html")

@app.route("/predict", methods=["GET"])
def model_data():
    price = ""
    area = ""
    bedrooms = ""
    bathrooms = ""
    stories = ""
    if request.method == "GET":
        area = request.args.get('area',type=int)
        bedrooms = request.args.get('bedrooms',type=int)
        bathrooms = request.args.get('bathrooms',type=int)
        stories = request.args.get('stories',type=int)
        inputs = [[area,bedrooms,bathrooms,stories]]
        price = model.predict(inputs)
    return render_template("index.html",price = price,area =area,bedrooms = bedrooms,stories = stories,bathrooms = bathrooms)

if __name__ == "__main__":
    app.run(debug=True)