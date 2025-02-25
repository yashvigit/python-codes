def differ():
    boys=0
    girls=0
    l1= [ ('b1','b2','b3'),'g1' ,'g2' , 'g3', ('b4',) ]
    for i in l1:
        if isinstance(i,tuple):
                boys +=len(i)
        else:
                girls+=1
    print(boys)
    print(girls)
    
            
            
differ()
