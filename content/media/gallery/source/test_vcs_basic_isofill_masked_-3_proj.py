
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

p = vcs.createprojection()

ptype = int('-3')
p.type = ptype
gm.projection = p

xtra = {}
f=cdms2.open(os.path.join(sys.prefix,'sample_data','clt.nc'))
s=f("clt",**xtra)
s=MV2.masked_greater(s,78.)
x.plot(s,gm,bg=bg)




x.png('test_vcs_basic_isofill_masked_-3_proj.png')
