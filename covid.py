import base64
import requests
import pandas
import io
from matplotlib import pyplot, ticker

response = requests.get("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
#print(response.text)

frame = pandas.read_csv(io.StringIO(response.text), sep = ",")
#state = frame.groupby("state")
#print(state.get_group("Washington")["deaths"].sum())
#print(frame["state"].unique())
def get_total_cases_by_state(state):
    # return frame.groupby("state").get_group(state)["cases"].sum()
    group_states = frame.groupby("state")
    df = group_states.get_group(state)
    cases = df["cases"].sum()
    return cases

def get_totals_for_state(state, stat_type):
    if stat_type not in ["cases", "deaths"]:
        raise RuntimeError(f"Invalid stat type passed: {stat_type}")
    return frame.groupby("state").get_group(state)[stat_type].sum()

def get_totals_by_state(stat_type):
    if stat_type not in ["cases", "deaths"]:
        raise RuntimeError(f"Invalid stat type passed: {stat_type}")
    return frame.groupby("state").sum()[stat_type].to_dict()


def get_total_cases_by_state2(state):
    return frame.groupby("state").sum()["cases"].loc[state]

#dict_table = get_totals_by_state("cases")
#dict_states = list(dict_table.keys())
#dict_cases = list(dict_table.values())

#pyplot.bar(dict_states,dict_cases)
#pyplot.title("COVID-19 CASES")
#pyplot.ticklabel_format(style="plain", axis="y")
#pyplot.xticks(rotation=90)
#pyplot.xlabel("States")
#pyplot.ylabel("Cases")

#bio = io.BytesIO()
#pyplot.savefig(bio, format="PNG")
#enc_img = base64.b64encode(bio.getvalue())

#print(get_total_cases_by_state("New York"))
#print(get_total_cases_by_state2("New York"))
