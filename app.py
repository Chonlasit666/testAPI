from flask import Flask, request
app = Flask(__name__)

@app.route("/test", methods=['GET'])
def hello():
  q = request.args.get('q')
  print(q)
  return { "message": 1 }, 201

if __name__ == "__main__":
    app.run()
