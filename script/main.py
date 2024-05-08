import pandas as pd
from txtzy import txtzy
from ifmulti import ifmulti
from isfq import isfq
import os

#字典与文件保存位置

path=os.path.abspath('.')+'\\'
file = 'text.txt' #将待注音文本放入text.txt中
dic_loc=path
dic='dic.csv'
file_name = path+file
hokin_dic=pd.read_csv(dic_loc+dic,encoding='utf-8')
shuowen_loc=path+'\\shuowen\\shuowen-master\\data\\'


if __name__=="__main__":
  
  fq=isfq()
  mode,num=ifmulti(fq)
  destname=input("Enter a name for the result:")
  txtzy(file_name,destname,hokin_dic,shuowen_loc,path,mode,num,fq)
  print('done!')





