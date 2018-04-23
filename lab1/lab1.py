import urllib.request
import json


def read_from_file(filename):
    with open(filename) as f:
        read_data = f.read()
    return read_data


def write_to_file(filename, data):
    with open(filename, 'w') as f2:
        f2.write(json.dumps(data, indent=4))


url = json.loads(read_from_file('in.json'))["url"]

response = json.loads(urllib.request.urlopen(url).read().decode('utf8'))
out = []
for i in range(len(response)):
    result = {}
    result["league_name"] = response[i]["league_name"]
    result["match_date"] = response[i]["match_date"]
    result["match_hometeam_name"] = response[i]["match_hometeam_name"]
    result["match_awayteam_name"] = response[i]["match_awayteam_name"]
    result["match_hometeam_score"] = response[i]["match_hometeam_score"]
    result["match_awayteam_score"] = response[i]["match_awayteam_score"]
    out.append(result)

write_to_file('out.json', out)
