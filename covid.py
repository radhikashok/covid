import requests
import pandas
import io

response = requests.get("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
#print(response.text)

frame = pandas.read_csv(io.StringIO(response.text), sep = ",")
#state = frame.groupby("state")
#print(state.get_group("Washington")["deaths"].sum())

def get_total_cases_by_state(state):
    # return frame.groupby("state").get_group(state)["cases"].sum()
    group_states = frame.groupby("state")
    df = group_states.get_group(state)
    cases = df["cases"].sum()
    return cases

def get_total_cases_by_state2(state):
    return frame.groupby("state").sum()["cases"].loc[state]

#print(get_total_cases_by_state("New York"))
print(get_total_cases_by_state2("New York"))
