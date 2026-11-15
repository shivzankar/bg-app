from flask import Flask
import os
app = Flask(__name__)

COLOR = os.getenv("APP_COLOR", "blue")
BUILD = os.getenv("BUILD", "dev")

THEMES = {
    "blue":  {"main": "#1a56db", "light": "#e8effc", "badge": "BLUE - STABLE VERSION",
              "version": "1.0", "note": "Currently serving traffic from the Blue deployment."},
    "green": {"main": "#15803d", "light": "#e7f6ec", "badge": "GREEN - NEW VERSION",
              "version": "2.0", "note": "New release deployed and verified in the Green deployment."},
}

@app.route("/")
def home():
    t = THEMES.get(COLOR, THEMES["blue"])
    name = COLOR.capitalize()
    return f"""<!DOCTYPE html>
<html><head><title>VLE 8 - {name} Environment</title>
<style>
  body {{ margin:0; font-family:Arial,sans-serif; background:{t['light']}; }}
  header {{ background:{t['main']}; color:white; text-align:center; padding:28px 16px; }}
  header h1 {{ margin:0 0 10px; font-size:34px; }}
  header p {{ margin:0; font-size:16px; }}
  .card {{ background:white; max-width:520px; margin:60px auto; padding:32px 40px; border-radius:12px;
           box-shadow:0 4px 18px rgba(0,0,0,0.12); text-align:center; }}
  .card h2 {{ color:{t['main']}; font-size:30px; margin:0 0 18px; }}
  .badge {{ display:inline-block; background:{t['main']}; color:white; padding:10px 22px;
            border-radius:22px; font-weight:bold; font-size:15px; }}
  .card h3 {{ color:#1f2937; font-size:24px; margin:22px 0 14px; }}
  .card p {{ color:#4b5563; margin:8px 0; font-size:16px; }}
</style></head>
<body>
  <header>
    <h1>VLE 8 - Blue-Green Deployment</h1>
    <p>Automated Deployment using Jenkins, Docker and Kubernetes</p>
  </header>
  <div class="card">
    <h2>{name} Environment</h2>
    <span class="badge">{t['badge']}</span>
    <h3>Application Version {t['version']}</h3>
    <p>{t['note']}</p>
    <p>Deployment Strategy: Blue-Green</p>
    <p>Container Platform: Docker</p>
    <p>Orchestration: Kubernetes</p>
    <p>Jenkins Build: #{BUILD}</p>
  </div>
</body></html>"""

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
