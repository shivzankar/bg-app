from flask import Flask
import os
app = Flask(__name__)

COLOR = os.getenv("APP_COLOR", "blue")

THEMES = {
    "blue": {
        "name": "Blue", "header": "#1a56db", "heading": "#2f3e8c",
        "bg": "linear-gradient(180deg, #93c5fd 0%, #3b82f6 100%)",
        "badge": "BLUE - STABLE VERSION", "version": "1.0",
    },
    "green": {
        "name": "Green", "header": "#16a34a", "heading": "#166534",
        "bg": "linear-gradient(180deg, #86efac 0%, #22c55e 100%)",
        "badge": "GREEN - NEW VERSION", "version": "2.0",
    },
}

@app.route("/")
def home():
    t = THEMES.get(COLOR, THEMES["blue"])
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>VLE 8 - {t['name']} Environment</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; min-height: 100vh; font-family: Arial, Helvetica, sans-serif; background: {t['bg']}; }}
  header {{ background: {t['header']}; color: #ffffff; text-align: center; padding: 30px 16px 34px; }}
  header h1 {{ margin: 0 0 14px; font-size: 34px; font-weight: bold; }}
  header p {{ margin: 0; font-size: 16px; }}
  .card {{ background: #f7f7f7; width: 560px; max-width: 92%; margin: 40px auto; padding: 26px 30px 34px;
           border-radius: 10px; box-shadow: 0 6px 22px rgba(0, 0, 0, 0.15); text-align: center; }}
  .card h2 {{ color: {t['heading']}; font-size: 30px; margin: 4px 0 18px; }}
  .badge {{ display: inline-block; background: {t['header']}; color: #ffffff; padding: 9px 22px;
            border-radius: 20px; font-size: 15px; }}
  .card h3 {{ color: {t['heading']}; font-size: 22px; margin: 22px 0 16px; }}
  .card p {{ color: #444444; font-size: 15px; margin: 0 0 12px; }}
</style>
</head>
<body>
  <header>
    <h1>VLE 8 - Blue-Green Deployment</h1>
    <p>Automated Deployment using Jenkins, Docker and Kubernetes</p>
  </header>
  <div class="card">
    <h2>{t['name']} Environment</h2>
    <span class="badge">{t['badge']}</span>
    <h3>Application Version {t['version']}</h3>
    <p>Currently serving traffic from the {t['name']} deployment.</p>
    <p>Deployment Strategy: Blue-Green</p>
    <p>Container Platform: Docker</p>
    <p>Orchestration: Kubernetes</p>
  </div>
</body>
</html>"""

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
