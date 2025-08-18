from flask import Flask, render_template, request
from dotenv import load_dotenv
from ai.cards import parse_card
load_dotenv()
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def scan_documents():
    # requirements - 
    # 1. should accept multiple images (max 10)
    # 2. should send images to chatGPT in a proper manner
    # 3. should take the json response and add in a local .xlsx sheet
    # 4. should return a response, telling how many images were successfully processed, their name and the ones who werent
    
    if request.method == "POST":
        try:
            res = parse_card()
            return res
        except Exception as e:
            return {"error": str(e)}
    return render_template("index.html")