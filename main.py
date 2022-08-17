from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    """Landing page route."""
    nav = [
        {"name": "Home", "url": "https://example.com/1"},
        {"name": "About", "url": "https://example.com/2"},
        {"name": "Pics", "url": "https://example.com/3"},
    ]
    return render_template(
        "home.html",
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja.",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
