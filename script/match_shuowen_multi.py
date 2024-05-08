import multiprocessing
from match_shuowen_part import match_shuowen_part

def match_shuowen_multi(string,type,shuowen_loc,number):
    
    # 将任务分配给number个线程
    pool = multiprocessing.Pool(number)
    results = []

    # 将json文件分成number个部分，每个部分分配给一个线程
    for i in range(number):
        start_index = i * 9833 // number + 1
        end_index = (i + 1) * 9833 // number
        results.append(pool.apply_async(match_shuowen_part, args=(start_index, end_index, string, shuowen_loc)))
    pool.close()
    pool.join()# 等待所有线程完成
    
    
    for result in results:
        fanqie = result.get()
        
        if fanqie[1] == 1:
             ans=fanqie
             break
        else:
            ans=[]

    if ans!=[]:
        return ans    
    else:
        return [],0
