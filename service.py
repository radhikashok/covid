from flask import Flask, abort, render_template
from covid import get_totals_for_state
from backup import get_totals_img

application = Flask("Rad_COVID")

#@application.route("/state/<state>/cases", methods=["GET"])
#def total_cases_by_state(state):
#    return f"{get_totals_by_state(state, 'cases')}"

#@application.route("/state/<state>/deaths", methods=["GET"])
#def total_deaths_by_state(state):
#    return f"{get_totals_by_state(state, 'deaths')}"

@application.route("/state/<state>/<stat_type>", methods=["GET"])
def total_deaths_by_state(state, stat_type):
    try:
        return f"{get_totals_for_state(state, stat_type)}"
    except Exception as e:
        return abort(404, str(e))

@application.route("/images/<stat_type>.png", methods=["GET"])
def totals_image(stat_type):
    try:
        return render_template("index.html", img_data=get_totals_img(stat_type).decode("utf-8"))
    except Exception as e:
        return abort(404, str(e))
