from flask import Flask, abort
#from flask_rebar import errors
from covid import get_totals_by_state

application = Flask("Rad_Covid")

#@application.route("/state/<state>/cases", methods=["GET"])
#def total_cases_by_state(state):
#    return f"{get_totals_by_state(state, 'cases')}"

#@application.route("/state/<state>/deaths", methods=["GET"])
#def total_deaths_by_state(state):
#    return f"{get_totals_by_state(state, 'deaths')}"

@application.route("/state/<state>/<stat_type>", methods=["GET"])
def total_deaths_by_state(state, stat_type):
    try:
        return f"{get_totals_by_state(state, stat_type)}"
    except Exception as e:
        return abort(404, str(e))
