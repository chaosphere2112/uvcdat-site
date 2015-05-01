import cdms2,sys,vcs

x=vcs.init()
f=cdms2.open(sys.prefix+"/sample_data/clt.nc")
s=f("clt",slice(0,1),squeeze=1)
b=x.createboxfill()
b.level_1=20
b.level_2=80
b.ext_1="y"
b.ext_2="y"
x.plot(s,b,bg=1)

fnm= "test_boxfill_lev1_lev2_ext1_ext2.png"

x.png(fnm)
