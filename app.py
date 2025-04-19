#ENTJ_task
#app.py

from flask import Flask, request, render_template
from s3_utils import load_history, save_history
from gpt_utils import chat_with_gpt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    user_id = request.args.get("user_id", "default_user")
    if request.method == "POST":
        msg = request.form["message"]
        history = load_history(user_id)
        response = chat_with_gpt(user_id, msg, history)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
