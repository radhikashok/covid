import base64
import requests
import pandas
import io
from matplotlib import pyplot, ticker
pyplot.switch_backend('Agg')

response = requests.get("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
frame = pandas.read_csv(io.StringIO(response.text), sep = ",")

def get_totals_img(stat_type):
    if stat_type not in ["cases", "deaths"]:
        raise RuntimeError(f"Invalid stat type passed: {stat_type}")

    dict_table = frame.groupby("state").sum()[stat_type].to_dict()
    dict_states = list(dict_table.keys())
    dict_types = list(dict_table.values())

    rects = pyplot.bar(dict_states, dict_types)
    pyplot.gcf().subplots_adjust(bottom=0.15)
    pyplot.title("COVID-19 " + stat_type.upper())
    pyplot.ticklabel_format(style="plain", axis="y")
    pyplot.xticks(fontsize=6, rotation=90)
    pyplot.xlabel("States")
    pyplot.ylabel(stat_type)

    for rect in rects:
        height = rect.get_height()
        pyplot.text(rect.get_x() + rect.get_width()/2.,
                    height + 10,
                    f"{height}",
                    ha="center",
                    va="bottom",
                    rotation=90,
                    fontsize=4)
    
    bio = io.BytesIO()
    pyplot.savefig(bio, format="PNG")
    return base64.b64encode(bio.getvalue())


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
