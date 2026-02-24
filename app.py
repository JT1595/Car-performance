from flask import Flask, render_template

app = Flask(__name__)

# ====================== CAR DATA ======================
cars = [
    {
        "brand": "Koenigsegg",
        "model": "Jesko Absolut",
        "zero_to_100": "2.5 s",
        "torque": "1500 Nm",
        "hp": "1600 hp",
        "top_speed": "530+ km/h",
        "image": "/static/images/koenigsegg.jpg"  # Updated path for subfolder
    },
    {
        "brand": "Lamborghini",
        "model": "Revuelto",
        "zero_to_100": "2.4 s",
        "torque": "725 Nm + electric",
        "hp": "1015 hp",
        "top_speed": "350 km/h",
        "image": "/static/images/lamborghini.jpg"  # Updated path for subfolder
    },
    {
        "brand": "Aston Martin",
        "model": "Valkyrie",
        "zero_to_100": "2.5 s",
        "torque": "900+ Nm",
        "hp": "1160 hp",
        "top_speed": "400+ km/h",
        "image": "/static/images/astonmartin.jpg"  # Updated path for subfolder
    },
    {
        "brand": "Ferrari",
        "model": "SF90 XX",
        "zero_to_100": "2.3 s",
        "torque": "1065 Nm",
        "hp": "1030 hp",
        "top_speed": "340 km/h",
        "image": "/static/images/ferrari.jpg"  # Updated path for subfolder
    },
    {
        "brand": "Bugatti",
        "model": "Chiron Super Sport",
        "zero_to_100": "2.4 s",
        "torque": "1600 Nm",
        "hp": "1600 hp",
        "top_speed": "440 km/h",
        "image": "/static/images/bugatti.jpg"  # Updated path for subfolder
    }
]

@app.route("/")
def home():
    return render_template("index.html", cars=cars)

if __name__ == "__main__":
    app.run(debug=True)