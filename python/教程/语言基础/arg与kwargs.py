def foo(*args,**kwargs):
    print ('args is',args)
    print ('kwargs is',kwargs)
foo(1,2)
foo(k=1,w=2,a=3,r=4,g=5,s=6)
foo(1,2,a=1,b=2,c=2)
foo('a',1,None,a=1,b='2',c=3)