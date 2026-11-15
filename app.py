from flask import Flask
import os
app = Flask(__name__)

COLOR = os.getenv("APP_COLOR", "blue")

THEMES = {
    "blue": {
        "name": "Blue", "badge": "BLUE - STABLE VERSION", "version": "1.0",
        "dark": "#0a1a4f", "mid": "#1a56db", "light": "#60a5fa", "glow": "rgba(96,165,250,0.55)",
    },
    "green": {
        "name": "Green", "badge": "GREEN - NEW VERSION", "version": "2.0",
        "dark": "#052e16", "mid": "#15803d", "light": "#4ade80", "glow": "rgba(74,222,128,0.55)",
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
  body {{
    margin: 0; min-height: 100vh; overflow-x: hidden; color: #ffffff;
    font-family: 'Segoe UI', Arial, sans-serif;
    background: radial-gradient(circle at 20% 20%, {t['light']} 0%, transparent 35%),
                radial-gradient(circle at 80% 80%, {t['mid']} 0%, transparent 40%),
                linear-gradient(135deg, {t['dark']} 0%, {t['mid']} 55%, {t['dark']} 100%);
  }}
  .orb {{ position: fixed; border-radius: 50%; filter: blur(40px); opacity: 0.45; animation: float 9s ease-in-out infinite; z-index: 0; }}
  .o1 {{ width: 260px; height: 260px; background: {t['light']}; top: 12%; left: 6%; }}
  .o2 {{ width: 340px; height: 340px; background: {t['mid']}; bottom: 4%; right: 6%; animation-delay: 3s; }}
  .o3 {{ width: 180px; height: 180px; background: {t['light']}; bottom: 18%; left: 38%; animation-delay: 6s; }}
  @keyframes float {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-30px); }} }}

  header {{
    position: relative; z-index: 1; text-align: center; padding: 34px 16px 38px;
    background: linear-gradient(90deg, {t['dark']}, {t['mid']}, {t['dark']});
    border-bottom: 2px solid {t['light']}; box-shadow: 0 8px 30px rgba(0,0,0,0.35);
  }}
  header h1 {{ margin: 0 0 12px; font-size: 38px; letter-spacing: 1px; text-shadow: 0 0 18px {t['glow']}; }}
  header p {{ margin: 0; font-size: 17px; opacity: 0.9; }}

  .card {{
    position: relative; z-index: 1; width: 620px; max-width: 92%; margin: 46px auto; padding: 34px 38px 30px;
    text-align: center; border-radius: 20px;
    background: rgba(255,255,255,0.10); backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.28);
    box-shadow: 0 20px 50px rgba(0,0,0,0.40), 0 0 40px {t['glow']};
  }}
  .card h2 {{ font-size: 40px; margin: 0 0 18px; text-shadow: 0 0 20px {t['glow']}; }}
  .badge {{
    display: inline-flex; align-items: center; gap: 10px; padding: 11px 26px; border-radius: 30px;
    font-weight: bold; font-size: 15px; letter-spacing: 1px;
    background: linear-gradient(90deg, {t['mid']}, {t['light']}); box-shadow: 0 0 22px {t['glow']};
  }}
  .dot {{ width: 10px; height: 10px; border-radius: 50%; background: #ffffff; animation: pulse 1.6s infinite; }}
  @keyframes pulse {{ 0% {{ box-shadow: 0 0 0 0 rgba(255,255,255,0.8); }} 100% {{ box-shadow: 0 0 0 12px rgba(255,255,255,0); }} }}
  .card h3 {{ font-size: 26px; margin: 26px 0 8px; }}
  .note {{ font-size: 16px; opacity: 0.9; margin: 0 0 26px; }}

  .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }}
  .tile {{
    background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.22); border-radius: 14px;
    padding: 16px 10px; transition: transform 0.25s, box-shadow 0.25s;
  }}
  .tile:hover {{ transform: translateY(-6px); box-shadow: 0 0 24px {t['glow']}; }}
  .icon {{ font-size: 30px; margin-bottom: 8px; }}
  .label {{ font-size: 12px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.75; }}
  .value {{ font-size: 16px; font-weight: bold; margin-top: 4px; }}

  .status {{
    margin-top: 24px; display: flex; justify-content: center; align-items: center; gap: 10px;
    font-size: 14px; opacity: 0.9;
  }}
  .live {{ width: 9px; height: 9px; border-radius: 50%; background: {t['light']}; animation: pulse 1.6s infinite; }}
</style>
</head>
<body>
  <div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>

  <header>
    <h1>VLE 8 - Blue-Green Deployment</h1>
    <p>Automated Deployment using Jenkins, Docker and Kubernetes</p>
  </header>

  <div class="card">
    <h2>{t['name']} Environment</h2>
    <span class="badge"><span class="dot"></span>{t['badge']}</span>
    <h3>Application Version {t['version']}</h3>
    <p class="note">Currently serving traffic from the {t['name']} deployment.</p>

    <div class="grid">
      <div class="tile"><div class="icon">&#8644;</div><div class="label">Deployment Strategy</div><div class="value">Blue-Green</div></div>
      <div class="tile"><div class="icon">&#128051;</div><div class="label">Container Platform</div><div class="value">Docker</div></div>
      <div class="tile"><div class="icon">&#9784;</div><div class="label">Orchestration</div><div class="value">Kubernetes</div></div>
    </div>

    <div class="status"><span class="live"></span>{t['name']} environment is live and healthy</div>
  </div>
</body>
</html>"""

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
