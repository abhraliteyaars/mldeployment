from flask import Flask,render_template,request,jsonify
import pickle
import sklearn
from db import write_data_db
import datetime

app =Flask(__name__)

model =pickle.load(open("models/houseprice.pkl","rb"))


#base_df = pd.read_csv('sample_file.csv')

@app.route("/") 
def basic_render():
    return render_template("index.html")


#in case we want to pass data in the url
@app.route("/predict", methods=["GET"])
def model_data():
    price = ""
    area = ""
    bedrooms = ""
    bathrooms = ""
    stories = ""
    area = request.args.get('area',type=int)
    bedrooms = request.args.get('bedrooms',type=int)
    bathrooms = request.args.get('bathrooms',type=int)
    stories = request.args.get('stories',type=int)
    inputs = [[area,bedrooms,bathrooms,stories]]
    price = model.predict(inputs)
    price_int = int(price[0])
    price_usd = "$ {:,}".format(price_int)
    timestamp = datetime.datetime.now()
    write_data_db(price_int, area, bedrooms, bathrooms, stories,timestamp)
    # print(price_int, area, bedrooms, bathrooms, stories,timestamp)
    return render_template("index.html",price = price_usd,area =area,bedrooms = bedrooms,stories = stories,bathrooms = bathrooms)


    
#in case we want to pass case sensitive data
# @app.route("/predict", methods=["POST"])
# def post_method():
#     price = ""
#     area = ""
#     bedrooms = ""
#     bathrooms = ""
#     stories = ""
#     area = request.form.get('area',type=int)
#     bedrooms = request.form.get('bedrooms',type=int)
#     bathrooms = request.form.get('bathrooms',type=int)
#     stories = request.form.get('stories',type=int)
#     inputs = [[area,bedrooms,bathrooms,stories]]
#     price = model.predict(inputs)
#     price_int = price.astype(int)
#     return render_template("index.html",price = price_int,area =area,bedrooms = bedrooms,stories = stories,bathrooms = bathrooms)

#api response
@app.route("/api/predict", methods=["POST"])
def model_data_api():
    data = request.get_json()
    area = int(data.get('area'))
    bedrooms = int(data.get('bedrooms'))
    bathrooms = int(data.get('bathrooms'))
    stories = int(data.get('stories'))
    inputs = [[area,bedrooms,bathrooms,stories]]
    price = model.predict(inputs)
    return jsonify({"predicted_price": float(price[0])})

if __name__ == "__main__":
    app.run(debug=True)