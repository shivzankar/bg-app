from flask import Flask
import os
app = Flask(__name__)

COLOR = os.getenv("APP_COLOR", "blue")
BUILD = os.getenv("BUILD", "dev")
SHADES = {"blue": "#1565c0", "green": "#2e7d32"}

@app.route("/")
def home():
    bg = SHADES.get(COLOR, "#555555")
    return f"""<!DOCTYPE html>
<html><head><title>{COLOR.upper()} environment</title></head>
<body style="margin:0;height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;background:{bg};color:white;font-family:Arial,sans-serif;text-align:center">
  <h1 style="font-size:72px;margin:0">{COLOR.upper()} ENVIRONMENT</h1>
  <h2 style="font-weight:normal">Build #{BUILD}</h2>
  <p style="font-size:20px">Blue-Green Deployment | Jenkins + Docker + Kubernetes</p>
</body></html>"""

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
