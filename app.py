from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
  dtnow = datetime.now()
  res = jsonify({"date": int(dtnow.strftime("%d")), "month": int(dtnow.strftime("%m")),
      "year": int(dtnow.strftime("%Y")), "hour": int(dtnow.strftime("%H")),
      "minute": int(dtnow.strftime("%M")), "second": int(dtnow.strftime("%S")),
      "formatted": dtnow.strftime("%d/%m/%Y, %H:%M:%S %Z")})

  return res

if __name__ == '__main__':
  app.run()
