#在教育部闽南语字典中查找文读和多音注音
def match_dic(string,hokin_dic):
        ano=0
        pinyin0=''
        temp=hokin_dic.loc[hokin_dic['text'] == string]
      
        lenth_temp=len(temp)
        if lenth_temp==1:
            pinyin0=temp.iloc[0].at['pinyin']
            ano=1
            
        elif lenth_temp>1:

            for j in range(0,lenth_temp):
                if temp.iloc[j].at['wenbai']==1:
                    pinyin0=temp.iloc[j].at['pinyin']+'/'+pinyin0
                    ano=1
                    
                    
            if ano==0:
                    for j in range(0,lenth_temp):
                        if temp.iloc[j].at['wenbai']==0:
                            pinyin0=temp.iloc[j].at['pinyin']+'/'+pinyin0
                            ano=1
                            
            
            if ano==0:
             pinyin0=''            
        elif lenth_temp==0:
            pinyin0=''
            ano=0
            
        return pinyin0,lenth_temp,ano