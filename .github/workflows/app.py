from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num_legs = int(request.form["num_legs"])
        num_wings = int(request.form["num_wings"])
        num_flesh = int(request.form["num_flesh"])
        total_weight = (num_legs * 0.25) + (num_wings * 0.25) + (num_flesh * 1)
        chickens_needed = (num_legs + num_wings + num_flesh) // 5 + 1  # Each chicken has 2 legs, 2 wings, and 1 flesh
        remaining_legs = max(0, (2 * chickens_needed) - num_legs)
        remaining_wings = max(0, (2 * chickens_needed) - num_wings)
        remaining_flesh = max(0, chickens_needed - num_flesh)
        return render_template("index.html", total_weight=total_weight,
                               chickens_needed=chickens_needed,
                               remaining_legs=remaining_legs,
                               remaining_wings=remaining_wings,
                               remaining_flesh=remaining_flesh)
    
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
