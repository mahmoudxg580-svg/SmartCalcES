from flask import Flask,request,jsonify
app=Flask(__name__)
scores=[]

@app.route("/submit",methods=["POST"])
def submit(): scores.append(request.json); return jsonify(ok=True)

@app.route("/top")
def top(): return jsonify(sorted(scores,key=lambda x:-x["score"])[:10])

app.run(host="0.0.0.0",port=10000)