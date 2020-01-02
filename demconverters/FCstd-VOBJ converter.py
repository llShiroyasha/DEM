import os
from PySide import QtGui, QtCore

dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
os.chdir(dir_)

def converter():
	if App.ActiveDocument.Name == "Unnamed":
		ap = App.ActiveDocument.Name
		exec("""a1 = App.getDocument("{}").getObject("Extrude")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap = App.ActiveDocument.Name
		exec("""a1 = App.getDocument("{}").getObject("Extrude")""".format(ap),globals())
        
	if a1 == None:
		pass
	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Extrude")) == True:
		a=0
		b=len(App.ActiveDocument.Extrude.Shape.Vertexes)
		list1=[]
		for a in range (0,b):
			xp=App.ActiveDocument.Extrude.Shape.Vertexes[a].Point.x
			xp=xp*0.001
			xp=str(xp)
			list1.append(xp)
			yp=App.ActiveDocument.Extrude.Shape.Vertexes[a].Point.y
			yp=yp*0.001
			yp=str(yp)
			list1.append(yp)
			zp=App.ActiveDocument.Extrude.Shape.Vertexes[a].Point.z
			zp=zp*0.001
			zp=str(zp)
			list1.append(zp)
			a=a+1

		b=str(b)
		tell = """Ver: 1.1
Title: """+FreeCAD.getDocument(ap).getObject("Extrude").Label+"""
 
Bound_Type: 1 AXIS: 0.0 0.0 1.0
NUM_VERTEX: """+b+"""

"""
		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Extrude").Label+".VOBJ")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Extrude").Label+".VOBJ")
		VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude").Label+".txt", "w")
		VOBJ.write(tell)
		VOBJ.close()
        
		file = open(FreeCAD.getDocument(ap).getObject("Extrude").Label+".txt" , 'a') 
		n=0
		b=int(b)
		for n in range (0,b):
			a4=3*n
			a2=3*n+1
			a3=3*n+2
			a4=str(a4)
			a2=str(a2)
			a3=str(a3)
			exec("""file.write(list1[{}]+"  "+list1[{}]+"  "+list1[{}]+"\\n")""".format(a4,a2,a3))
			n+=1
		file.close()
        
		nbf=(b-2)/2
		nbe=nbf-1
		nbf=str(nbf)
		nbf=nbf.replace('.0','')
		nbe=str(nbe)
		nbe=nbe.replace('.0','')
		n=1
		c1=3
		c2=4
		c3=6
		c4=5

		next="""
NUM_FACES: """+nbf+"""
  
4 
1 3 4 2
  
"""
		VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude").Label+".txt", "a")
		VOBJ.write(next)
		VOBJ.close()

		file2 = open(FreeCAD.getDocument(ap).getObject("Extrude").Label+".txt", "a")
		nbf=int(nbf)
		for n in range (1,nbf):
			c1=str(c1)
			c2=str(c2)
			c3=str(c3)
			c4=str(c4)
			file2.write("""4 
"""+c1+""" """+c2+""" """+c3+""" """+c4+"""

""")
			c1=int(c1)
			c2=int(c2)
			c3=int(c3)
			c4=int(c4)
			c1=c1+2
			c2=c2+2
			c3=c3+2
			c4=c4+2
			n+=1
		file2.close()

		onext="""
NUM_Edges: """+nbe+"""

"""

		VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude").Label+".txt", "a")
		VOBJ.write(onext)
		VOBJ.close()

		file3 = open(FreeCAD.getDocument(ap).getObject("Extrude").Label+".txt", "a")
		nbe=int(nbe)
		c1=5
		c2=6
		for n in range (0,nbe):
			c1=str(c1)
			c2=str(c2)
			file3.write(c1+""" """+c2+"""
""")
			c1=int(c1)
			c2=int(c2)
			c1=c1+1
			c2=c2+1
			n+=1
		file3.close()

		oonext="""
_CohesionParamaters(Optional)_
"""

		VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude").Label+".txt", "a")
		VOBJ.write(oonext)
		VOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Extrude").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Extrude").Label+".VOBJ")

	j=1
	for j in range (1,100):
		n=str(j)
		a=App.getDocument(ap).getObject("Extrude00"+n)
		if j<10 and a==None:
			pass
		elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Extrude00"+n)) == True:
			a=0
			ldic=locals()
			exec("b=len(App.ActiveDocument.Extrude00{}.Shape.Vertexes)".format(n),globals(),ldic)
			b=ldic["b"]
			print(b)
			list1=[]
			for a in range (0,b):
				exec("xp=App.ActiveDocument.Extrude00{}.Shape.Vertexes[{}].Point.x".format(n,a),globals(),ldic)
				xp=ldic["xp"]
				xp=str(xp)
				xp=xp.replace('.0','')
				xp=int(xp)
				xp=xp*0.001
				xp=str(xp)
				list1.append(xp)
				exec("yp=App.ActiveDocument.Extrude00{}.Shape.Vertexes[{}].Point.y".format(n,a),globals(),ldic)
				yp=ldic["yp"]
				yp=str(yp)
				yp=yp.replace('.0','')
				yp=int(yp)
				yp=yp*0.001
				yp=str(yp)
				list1.append(yp)
				exec("zp=App.ActiveDocument.Extrude00{}.Shape.Vertexes[{}].Point.z".format(n,a),globals(),ldic)
				zp=ldic["zp"]
				zp=str(zp)
				zp=zp.replace('.0','')
				zp=int(zp)
				zp=zp*0.001
				zp=str(zp)
				list1.append(zp)
				a=a+1
			b=str(b)
			tell = """Ver: 1.1
Title: """+FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+"""
 
Bound_Type: 1 AXIS: 0.0 0.0 1.0
NUM_VERTEX: """+b+"""

"""
			n=str(n)
			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".VOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".VOBJ")
			VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".txt", "w")
			VOBJ.write(tell)
			VOBJ.close()
        
			file = open(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".txt" , 'a') 
			n=0
			b=int(b)
			for t in range (0,b):
				a4=3*t
				a2=3*t+1
				a3=3*t+2
				a4=str(a4)
				a2=str(a2)
				a3=str(a3)
				exec("""file.write(list1[{}]+"  "+list1[{}]+"  "+list1[{}]+"\\n")""".format(a4,a2,a3))
				t+=1
			file.close()
        
			nbf=(b-2)/2
			nbe=nbf-1
			nbf=str(nbf)
			nbf=nbf.replace('.0','')
			nbe=str(nbe)
			nbe=nbe.replace('.0','')
			n=1
			c1=3
			c2=4
			c3=6
			c4=5
	
			next="""
NUM_FACES: """+nbf+"""
  
4 
1 3 4 2
  
"""
			n=str(j)
			VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".txt", "a")
			VOBJ.write(next)
			VOBJ.close()

			file2 = open(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".txt", "a")
			nbf=int(nbf)
			for t in range (1,nbf):
				c1=str(c1)
				c2=str(c2)
				c3=str(c3)
				c4=str(c4)
				file2.write("""4 
"""+c1+""" """+c2+""" """+c3+""" """+c4+"""

""")
				c1=int(c1)
				c2=int(c2)
				c3=int(c3)
				c4=int(c4)
				c1=c1+2
				c2=c2+2
				c3=c3+2
				c4=c4+2
				t+=1
			file2.close()

			onext="""
NUM_Edges: """+nbe+"""

"""

			VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".txt", "a")
			VOBJ.write(onext)
			VOBJ.close()
	
			file3 = open(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".txt", "a")
			nbe=int(nbe)
			c1=5
			c2=6
			for t in range (0,nbe):
				c1=str(c1)
				c2=str(c2)
				file3.write(c1+""" """+c2+"""
""")
				c1=int(c1)
				c2=int(c2)
				c1=c1+1
				c2=c2+1
				t+=1
			file3.close()

			oonext="""
_Material_Specifications_
 
COR: """+FreeCAD.getDocument(ap).getObject("Extrude00"+n).COR+"""      
STATICFRICTION: """+FreeCAD.getDocument(ap).getObject("Extrude00"+n).Static_friction+""" 
KINETICFRICTION: """+FreeCAD.getDocument(ap).getObject("Extrude00"+n).Kinetic_friction+"""
 
_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME """+FreeCAD.getDocument(ap).getObject("Extrude00"+n).Contact_time+"""

_TangentParamaters_
CONTACT_TIME """+FreeCAD.getDocument(ap).getObject("Extrude00"+n).Contacttime+"""

_CohesionParamaters(Optional)_
"""

			VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".txt", "a")
			VOBJ.write(oonext)
			VOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Extrude00"+n).Label+".VOBJ")

		a=App.getDocument(ap).getObject("Extrude0"+n)
		if j>10 and a==None:
			pass
		elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Extrude0"+n)) == True:
			a=0
			ldic=locals()
			exec("b=len(App.ActiveDocument.Extrude0{}.Shape.Vertexes)".format(n),globals(),ldic)
			b=ldic["b"]
			print(b)
			list1=[]
			for a in range (0,b):
				exec("xp=App.ActiveDocument.Extrude0{}.Shape.Vertexes[{}].Point.x".format(n,a),globals(),ldic)
				xp=ldic["xp"]
				xp=str(xp)
				xp=xp.replace('.0','')
				xp=int(xp)
				xp=xp*0.001
				xp=str(xp)
				list1.append(xp)
				exec("yp=App.ActiveDocument.Extrude0{}.Shape.Vertexes[{}].Point.y".format(n,a),globals(),ldic)
				yp=ldic["yp"]
				yp=str(yp)
				yp=yp.replace('.0','')
				yp=int(yp)
				yp=yp*0.001
				yp=str(yp)
				list1.append(yp)
				exec("zp=App.ActiveDocument.Extrude0{}.Shape.Vertexes[{}].Point.z".format(n,a),globals(),ldic)
				zp=ldic["zp"]
				zp=str(zp)
				zp=zp.replace('.0','')
				zp=int(zp)
				zp=zp*0.001
				zp=str(zp)
				list1.append(zp)
				a=a+1
			b=str(b)
			tell = """Ver: 1.1
Title: """+FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+"""
 
Bound_Type: 1 AXIS: 0.0 0.0 1.0
NUM_VERTEX: """+b+"""

"""
			n=str(n)
			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".VOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".VOBJ")
			VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".txt", "w")
			VOBJ.write(tell)
			VOBJ.close()
        
			file = open(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".txt" , 'a') 
			n=0
			b=int(b)
			for t in range (0,b):
				a4=3*t
				a2=3*t+1
				a3=3*t+2
				a4=str(a4)
				a2=str(a2)
				a3=str(a3)
				exec("""file.write(list1[{}]+"  "+list1[{}]+"  "+list1[{}]+"\\n")""".format(a4,a2,a3))
				t+=1
			file.close()
        
			nbf=(b-2)/2
			nbe=nbf-1
			nbf=str(nbf)
			nbf=nbf.replace('.0','')
			nbe=str(nbe)
			nbe=nbe.replace('.0','')
			n=1
			c1=3
			c2=4
			c3=6
			c4=5
	
			next="""
NUM_FACES: """+nbf+"""
  
4 
1 3 4 2
  
"""
			n=str(j)
			VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".txt", "a")
			VOBJ.write(next)
			VOBJ.close()

			file2 = open(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".txt", "a")
			nbf=int(nbf)
			for t in range (1,nbf):
				c1=str(c1)
				c2=str(c2)
				c3=str(c3)
				c4=str(c4)
				file2.write("""4 
"""+c1+""" """+c2+""" """+c3+""" """+c4+"""

""")
				c1=int(c1)
				c2=int(c2)
				c3=int(c3)
				c4=int(c4)
				c1=c1+2
				c2=c2+2
				c3=c3+2
				c4=c4+2
				t+=1
			file2.close()

			onext="""
NUM_Edges: """+nbe+"""

"""

			VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".txt", "a")
			VOBJ.write(onext)
			VOBJ.close()
	
			file3 = open(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".txt", "a")
			nbe=int(nbe)
			c1=5
			c2=6
			for t in range (0,nbe):
				c1=str(c1)
				c2=str(c2)
				file3.write(c1+""" """+c2+"""
""")
				c1=int(c1)
				c2=int(c2)
				c1=c1+1
				c2=c2+1
				t+=1
			file3.close()

			oonext="""
_Material_Specifications_
 
COR: """+FreeCAD.getDocument(ap).getObject("Extrude0"+n).COR+"""      
STATICFRICTION: """+FreeCAD.getDocument(ap).getObject("Extrude0"+n).Static_friction+""" 
KINETICFRICTION: """+FreeCAD.getDocument(ap).getObject("Extrude0"+n).Kinetic_friction+"""
 
_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME """+FreeCAD.getDocument(ap).getObject("Extrude0"+n).Contact_time+"""

_TangentParamaters_
CONTACT_TIME """+FreeCAD.getDocument(ap).getObject("Extrude0"+n).Contacttime+"""

_CohesionParamaters(Optional)_
"""

			VOBJ=open(FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".txt", "a")
			VOBJ.write(oonext)
			VOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Extrude0"+n).Label+".VOBJ")
			
converter()