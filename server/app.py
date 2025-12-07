import os
from flask import Flask, send_from_directory

# Defines the location of the build folder
# In production (Docker), we might adjust this path.
# We will assume the structure /app/client/dist for static files
# or relative paths during dev.

CLIENT_DIST_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../client/dist'))

app = Flask(__name__, static_folder=CLIENT_DIST_FOLDER)

# Security Headers
try:
    from flask_talisman import Talisman
    csp = {
        'default-src': '\'self\'',
        'img-src': ['\'self\'', 'data:', 'https:'],
        'style-src': ['\'self\'', '\'unsafe-inline\'', 'https://fonts.googleapis.com'],
        'font-src': ['\'self\'', 'https://fonts.gstatic.com'],
        'script-src': ['\'self\'', '\'unsafe-inline\''] # 'unsafe-inline' might be needed for some Vue setups or initial hydration if not strict. 
        # Ideally avoid unsafe-inline but for a simple template it reduces friction.
    }
    Talisman(app, content_security_policy=csp, force_https=False) # force_https=False because logic might handle SSL termination (e.g. AWS Lightsail Load Balancer) or local dev
except ImportError:
    pass

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # Check if the file exists in the dist folder
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    
    # Otherwise fallback to index.html (SPA)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
