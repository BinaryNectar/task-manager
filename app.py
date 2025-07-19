from flask import Flask, send_from_directory
from routes import bp

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="")

    # serve index.html for the root URL
    @app.route("/")
    def serve_ui():
        return send_from_directory(app.static_folder, "index.html")
    
    app.register_blueprint(bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

