#将反切的台罗注音声部和韵部拼接
def fq2py(str1,str2):
    shengmu=["p","b","m","t","n","l","k","g","h","s","j"]
    shengmu2=["ph","th","kh","ng","ts","tsh"]
    len_str2=len(str2)
    for i in shengmu:
        if str1[0:1]==i:
            p1=i
            for j in shengmu2:
                if str1[0:2]==j:
                    p1=j
                    break
            break
                
        else:
            p1=str1
    
    for i in shengmu:
        if str2[0:1]==i:
            p2=str2[1:len_str2]
            for j in shengmu2:
                if str1[0:2]==j:
                    p2=str2[2:len_str2]
                    break
            break
               
        else:
            p2=str2
    pinyin=p1+p2
    return pinyin