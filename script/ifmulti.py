def ifmulti(fq):
    if fq=="1":
     key = input("Enter 2 if you'd like to use multiprocessing (not suggested):  ")
    else:
        key=[]
    if key=='2':
         mode=2
         num=int(input("number of processor used: "))
    else:
         mode=1
         num=[]
    return mode,num