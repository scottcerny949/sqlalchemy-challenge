from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/<start></br>"
        f"/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return "precip placeholder"

@app.route("/api/v1.0/stations")
def stations():
    return "stations placeholder"

@app.route("/api/v1.0/tobs")
def tobs():
    return "tobs placeholder"

@app.route("/api/v1.0/<start>")
def temps(start):
    return "placeholder"

@app.route("/api/v1.0/<start>/<end>")
def temps2(startend):
    return "placeholder2"


if __name__ == "__main__":
    app.run(debug=True)


