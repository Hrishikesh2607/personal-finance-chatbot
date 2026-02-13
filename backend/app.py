from flask import Flask, request, jsonify
from budget_engine import get_monthly_spending, monthly_summary, remaining_budget, budget_advice

app = Flask(__name__)

@app.route("/summary", methods=["GET"])
def summary():
    return jsonify(monthly_summary())

@app.route("/advice", methods=["POST"])
def advice():
    data= request.json
    category= data.get("category")
    return jsonify({"advice": budget_advice(category)})

@app.route("/spending", methods=["POST"])
def spending():
    data = request.json

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    category = data.get("category")

    if not category:
        return jsonify({"error": "Category missing"}), 400

    total = get_monthly_spending(category)
    return jsonify({"total_spent": total})

if __name__ == "__main__":
    app.run(debug=True)




