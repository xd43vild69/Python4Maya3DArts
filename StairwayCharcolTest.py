#Stairway Charcol Test

import maya.cmds as mc

for x in range(0,10):
	stepName = 'cubex'+ str(x)
	
	cubeStep = mc.polyCube(w=50, h=2, d=5, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1, name=stepName)

	grp = mc.group(name=stepName + "NUL", em=True)
	mc.parent(cubeStep,grp)
	
	mc.setAttr(cubeStep[0] + ".translateY", x * 2)

mc.setAttr(grp + ".ry", x * 15)	