
import sys,os
import vcs
import sys
import cdms2
import vtk
import os
import MV2
bg = not False
x=vcs.init()

x.setcolormap("rainbow")
gm = vcs.createisofill()


xtra = {}
f=cdms2.open(os.path.join(sys.prefix,'sample_data','clt.nc'))
s=f("clt",**xtra)
s-=s
x.plot(s,gm,bg=bg)



x.png('test_vcs_basic_isofill_zero.png')
