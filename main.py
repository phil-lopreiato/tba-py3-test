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


@app.route("/team/list")
def team_list() -> str:
    page = 1
    client = ndb.Client()
    with client.context():
        page_labels = ['1-999']
        cur_page_label = page_labels[0]

        teams_1 = Team.query(Team.team_number >= 0, Team.team_number <= 500).fetch_async()
        teams_2 = Team.query(Team.team_number >= 501, Team.team_number <= 1000).fetch_async()
        teams = teams_1.get_result() + teams_2.get_result()

        num_teams = len(teams)
        middle_value = num_teams // 2
        if num_teams % 2 != 0:
            middle_value += 1
        teams_a, teams_b = teams[:middle_value], teams[middle_value:]

        template_values = {
            "teams_a": teams_a,
            "teams_b": teams_b,
            "num_teams": num_teams,
            "page_labels": page_labels,
            "cur_page_label": cur_page_label,
            "current_page": page
        }
        return render_template("team_list.html", **template_values)


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
