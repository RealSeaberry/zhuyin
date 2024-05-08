#将注音写入txt中

from tqdm import tqdm
from match_dic import match_dic
from match_shuowen import match_shuowen
from fq2py import fq2py
from match_shuowen_multi import match_shuowen_multi


def txtzy(file_name,destname,hokin_dic,shuowen_loc,file_loc,mode,num,fq):
 
 with open(file_name,encoding='UTF-8') as text:
     content = text.read()
     lenth = len(content)
     zhuyin=content

 pos=0
 sum_lenth=0

 for i in tqdm(range(0,lenth-1)):
   pos=sum_lenth+i
   
  
   if content[i] == '。' or content[i] == "，" or content[i] == "、" or content[i]=='?' or content[i]=='!' or content[i]=="《" or content[i]== "》" or content [i]=="" or content[i]=="\n" or content[i]=="：" or content[i]=="「" or content[i]=="」":
       continue
   else:
      pinyin=match_dic(content[i],hokin_dic)

      if content[i]=="" or content[i]=="\n":
            continue
      elif pinyin[2]==1:
          zhuyin=zhuyin[:pos+1]+pinyin[0]+zhuyin[pos+1:]
          sum_lenth=len(pinyin[0])+sum_lenth  
          continue   
      elif pinyin[2]==0:
         
         if fq=="1" :
          
          if mode==1:
            fanqie=match_shuowen(content[i],pinyin[2],shuowen_loc)
          if mode==2:
            fanqie = match_shuowen_multi(content[i],pinyin[2],shuowen_loc,num)
    
          fanqie_tp=fanqie[0]
          
          if fanqie[1]==1:
             fanqie1=fanqie_tp[0:1]
             fanqie2=fanqie_tp[1:2]
             pinyin1=match_dic(fanqie1,hokin_dic)
             pinyin2=match_dic(fanqie2,hokin_dic)
             try:
                 tmp_py1=pinyin1[0].split("/")
             except:
                 tmp_py1=pinyin1[0]
             try:
                 tmp_py2=pinyin2[0].split("/")
             except:
                 tmp_py2=pinyin2[0]
                 
             if pinyin1[2]==1 and pinyin2[2]==1:
                pinyin=fq2py(tmp_py1[0],tmp_py2[0])    
                zhuyin=zhuyin[:pos+1]+pinyin+zhuyin[pos+1:]
                sum_lenth=len(pinyin)+sum_lenth
             else:
                zhuyin=zhuyin[:pos+1]+"("+fanqie[0]+"切"+")"+zhuyin[pos+1:]
                sum_lenth=len(fanqie[0])+sum_lenth+3
          elif fanqie[1]==0:
             continue
         else:
            continue
             
          
 with open(file_loc+destname+'.txt','w',encoding='UTF-8') as hokin:
     hokin.write(zhuyin) 
         