
from flask import Flask, request, jsonify
from datetime import datetime, date

app = Flask(__name__)


@app.route("/calculate", methods=["POST"])
def calculate_deadline():
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or "deadline" not in data:
        return jsonify({"error": "Missing required field: deadline"}), 400

    try:
        deadline = datetime.strptime(data["deadline"], "%Y-%m-%d").date()

        days_remaining = (deadline - date.today()).days
        ####################################################################################
        #### PLACEHOLDER: Determine if a deadline is upcoming, overdue, or today here ######
        ####################################################################################
   

        return jsonify({
            "deadline": deadline.isoformat(),
            "days_remaining": days_remaining,
        })

    except (ValueError, TypeError):
        return jsonify({
            "error": "Invalid deadline. Use YYYY-MM-DD format."
        }), 400


if __name__ == "__main__":
    app.run(port=5000, debug=True)
