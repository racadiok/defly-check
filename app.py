from flask import Flask, jsonify, request
import os

import worker

app = Flask(__name__)


@app.route("/api/check-team/<string:region>/", methods=["GET"])
def check_team(region):
    return jsonify(worker.check_server(region))

@app.route("/api/check-team-port/<string:region>/<int:port>", methods=["GET"])
def check_team_by_port(region, port):
    return jsonify(worker.check_server_by_port(region, port))

@app.route("/api/check-teams", methods=["GET"])
def checkTeams():
    return jsonify(worker.check_servers())


if __name__ == "__main__":
    app.run()
