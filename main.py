import os
import pathlib

from flask import Flask, render_template
from google.cloud import ndb

from models.team import Team

app = Flask(__name__)


@app.route("/")
def root() -> str:
    return render_template("main.html")


@app.route("/team/<team_key>")
def team_info(team_key: str) -> str:
    client = ndb.Client()
    with client.context():
        team = Team.get_by_id(team_key)
        return render_template("team.html", team=team)


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.

    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"
    ] = f"{pathlib.Path(__file__).parent.absolute()}/tba-dev-phil-key.json"

    app.run(host="127.0.0.1", port=8080, debug=True)
