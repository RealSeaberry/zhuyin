#在说文解字中查找反切
import json


def match_shuowen(string,type0,shuowen_loc):
    ano=0
    if type0==0:
        for i in range(1,9833):
            with open(shuowen_loc+str(i)+".json") as json_data:
                temp_data=json.load(json_data)
            if temp_data["wordhead"]==string:
                fanqie=temp_data["pronunciation"]
                fanqie=fanqie[:2]
                ano=1
                break
            else:
                fanqie=[]
                ano=0
    #print(fanqie)
    return fanqie,ano