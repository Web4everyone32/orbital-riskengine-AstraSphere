from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Orbital Risk Engine</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            input, button { padding: 8px; margin: 5px; }
            .result { margin-top: 20px; padding: 15px; border-radius: 5px; }
            .HIGH { background-color: #ffdddd; }
            .MEDIUM { background-color: #fff3cd; }
            .LOW { background-color: #ddffdd; }
        </style>
    </head>
    <body>
        <h2>Orbital Risk Engine</h2>
        <p>Analyze orbital congestion risk for LEO shells.</p>

        <input id="altitude" placeholder="Altitude (km)" value="550"/>
        <input id="inclination" placeholder="Inclination (deg)" value="97"/>
        <button onclick="analyze()">Analyze Risk</button>

        <div id="output"></div>

        <script>
            async function analyze() {
                const alt = document.getElementById("altitude").value;
                const inc = document.getElementById("inclination").value;

                const res = await fetch(`/orbit/risk?altitude_km=${alt}&inclination_deg=${inc}`);
                const data = await res.json();

                document.getElementById("output").innerHTML = `
                    <div class="result ${data.risk_level}">
                        <b>Orbit Shell:</b> ${data.orbit_shell}<br/>
                        <b>Object Density:</b> ${data.object_density}<br/>
                        <b>Congestion Index:</b> ${data.congestion_index}<br/>
                        <b>Collision Probability:</b> ${data.collision_probability}<br/>
                        <b>Risk Level:</b> ${data.risk_level}
                    </div>
                `;
            }
        </script>
    </body>
    </html>
    """
