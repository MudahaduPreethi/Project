from flask import Flask, send_from_directory, request, jsonify, session, redirect

app = Flask(__name__)
app.secret_key = "27a253b9bed035d4da86efca5d0b1e70"  # Replace with a secure secret key


# Serve HTML files
@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "123":
            session["user"] = username
            return send_from_directory(".", "hp.html")  # Redirect to home page
        else:
            return "Invalid username or password"
    return send_from_directory(".", "login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


@app.route("/hp")
def hp():
    if "user" not in session:
        return redirect("/login")
    return send_from_directory(".", "hp.html")


@app.route("/about")
def about():
    return send_from_directory(".", "About.html")


@app.route("/ccl")
def ccl():
    return send_from_directory(".", "ccl.html")


@app.route("/faq")
def faq():
    return send_from_directory(".", "FAQ.html")


# Serve CSS, JS, and other static files
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)


# API route for crop recommendations
@app.route("/recommendation", methods=["POST"])
def recommendation():
    data = request.json
    try:
        soil_ph = float(data.get("soilPH"))
        soil_moisture = float(data.get("soilMoisture"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Provide valid soilPH and soilMoisture values."}), 400

    recommendation = (
        "Neutral soil. Grow Wheat, Rice, or Corn."
        if 5.5 <= soil_ph <= 7.5
        else "Acidic soil. Grow Coffee or Sweet Potato."
        if soil_ph < 5.5
        else "Alkaline soil. Grow Barley or Cotton."
    )
    notes = (
        "Ensure adequate irrigation as soil moisture is low."
        if soil_moisture < 20
        else "Be cautious of waterlogging as soil moisture is very high."
        if soil_moisture > 80
        else "Soil moisture is optimal."
    )
    return jsonify({"recommendation": recommendation, "notes": notes})


if __name__ == "__main__":
    app.run(debug=True)
