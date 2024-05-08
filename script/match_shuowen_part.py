#在说文解字中查找反切
import json


def match_shuowen_part(start_index, end_index, string, shuowen_loc):
    ano = 0
    fanqie = []
    for i in range(start_index, end_index + 1):
        with open(shuowen_loc + str(i) + ".json") as json_data:
            temp_data = json.load(json_data)
        if temp_data["wordhead"] == string:
            fanqie = temp_data["pronunciation"]
            fanqie = fanqie[:2]
            ano = 1
            break
        else:
            fanqie = []
            ano = 0
    return fanqie, ano