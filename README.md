##闽南语注音1.01beta
这段代码可以为繁体的txt文档闽南语文读的台罗拼音注音。默认闽南语读音字典是台湾教育部的闽南语字典，也可以使用说文解字的唐韵进行注音。
当使用默认的闽南语字典时，会优先选择文读音，而无文读音时会将所有读音都注释进文本中。由于此字典尚未包括所有的汉字，故一些字的读音无法查询，若说文解字中也查不到这个字，则会留空不注音。目前正在努力完善闽南语读音字典，以求减少这种情况的发生。
当使用说文解字中唐韵的反切注音时，会将字带入默认的字典搜索读音，然后进行拼接。若搜索不到对应字的读音，会直接将反切注释进文本。
本代码仅供研究学习使用。



##使用方法
1/将需要注音的文本粘贴进主目录下的text.txt，然后运行main.py。
2/按照提示选择是否在教育部字典无结果时查找说文解字库，是否使用多线程(平行遍历说文解字库，不一定会更快)。
3/输入目标文件名。



##支持
dic来源:教育部闽南语字典 https://sutian.moe.edu.tw/zh-hant/siongkuantsuguan/
说文解字来源:https://github.com/shuowenjiezi/shuowen/blob/master



##required package
tqdm                latest version
pandas              latest version
multiprocessing     latest version
