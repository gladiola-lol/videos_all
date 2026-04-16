from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Servidor listo 🚀</h1>"

# Flask ya sirve automáticamente la carpeta /static
# Tu video estará en /static/videos/mivideo.mp4

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
