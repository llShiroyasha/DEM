from PySide import QtGui, QtCore
from PySide.QtGui import QListWidget
import os

dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
os.chdir(dir_)

def POBJ():
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""a=App.getDocument("{}").getObject("Sphere")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""a=App.getDocument("{}").getObject("Sphere")""".format(ap),globals())
	if a==None:
		pass

	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere")) == True:

		#Diameter
		r1=FreeCAD.getDocument(ap).getObject("Sphere").Radius
		numr=str(r1)
		r=numr.replace('mm','')
		r=float(r)
		r=r*2
		r=r*0.001
		r=str(r)

		#Base Coordonates
		x1=App.ActiveDocument.Sphere.Placement.Base.x		
		x1=x1*0.001
		numx1=str(x1)
		x=numx1.replace('mm','')
		y1=App.ActiveDocument.Sphere.Placement.Base.z
		numy1=str(y1)
		y=numy1.replace('mm','')
		z1=App.ActiveDocument.Sphere.Placement.Base.y
		numz1=str(z1)
		z=numz1.replace('mm','')

		Sphere="""VER: 1.1
TYPE: SPHERE
Name: """+FreeCAD.getDocument(ap).getObject("Sphere").Label+"""

_Geometry_Specfications_

Diameter: """ +r+"""

MATERIALFILE:"""+FreeCAD.getDocument("Sans_nom").getObject("Sphere").MATERIALFILE


		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere").Label+".POBJ")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere").Label+".POBJ")

		WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere").Label+".txt", "w")
		WOBJ.write(Sphere)
		WOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere").Label+".POBJ")

	j=1
	for j in range (1,100):
		n=str(j)
		if j < 10 and App.getDocument(ap).getObject("Sphere00"+n)== None:
			pass

		elif j < 10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere00"+n)) == True :

			r1=FreeCAD.getDocument(ap).getObject("Sphere00"+n).Radius
			numr=str(r1)
			r=numr.replace('mm','')
			r=float(r)
			r=r*2*0.001
			r=str(r)

			ldic=locals()
			exec("x1=App.ActiveDocument.Sphere00{}.Placement.Base.x".format(n),globals(),ldic)
			x1=ldic["x1"]
			numx1=str(x1)
			numx=numx1.replace('mm','')

			exec("y1=App.ActiveDocument.Sphere00{}.Placement.Base.y".format(n),globals(),ldic)
			y1=ldic["y1"]
			numy1=str(y1)
			y=numy1.replace('mm','')

			exec("z1=App.ActiveDocument.Sphere00{}.Placement.Base.z".format(n),globals(),ldic)
			z1=ldic["z1"]
			numz1=str(z1)
			z=numz1.replace('mm','')

			Sphere="""VER: 1.1
TYPE: SPHERE
Name: """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+"""

_Geometry_Specfications_


Diameter: """ +r+"""

MATERIALFILE:"""+FreeCAD.getDocument(ap).getObject("Sphere00"+n).MATERIALFILE

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".POBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".POBJ")

			WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".txt", "w")
			WOBJ.write(Sphere)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".POBJ")
		
		if j > 10 and App.getDocument(ap).getObject("Sphere0"+n)== None:
			pass

		elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere0"+n)) == True :

			r1=FreeCAD.getDocument(ap).getObject("Sphere0"+n).Radius
			numr=str(r1)
			r=numr.replace('mm','')
			r=float(r)
			r=r*2
			r=r*0.001
			r=str(r)

			ldic=locals()
			exec("x1=App.ActiveDocument.Sphere0{}.Placement.Base.x".format(n),globals(),ldic)
			x1=ldic["x1"]
			numx1=str(x1)
			numx=numx1.replace('mm','')

			exec("y1=App.ActiveDocument.Sphere0{}.Placement.Base.y".format(n),globals(),ldic)
			y1=ldic["y1"]
			numy1=str(y1)
			y=numy1.replace('mm','')

			exec("z1=App.ActiveDocument.Sphere0{}.Placement.Base.z".format(n),globals(),ldic)
			z1=ldic["z1"]
			numz1=str(z1)
			z=numz1.replace('mm','')

			Sphere="""VER: 1.1
TYPE: SPHERE
Name: """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+"""

_Geometry_Specfications_


Diameter: """ +r+"""

MATERIALFILE:"""+FreeCAD.getDocument(ap).getObject("Sphere0"+n).MATERIALFILE

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".POBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".POBJ")

			WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".txt", "w")
			WOBJ.write(Sphere)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".POBJ")
		
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""b=App.getDocument("{}").getObject("Box")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""b=App.getDocument("{}").getObject("Box")""".format(ap),globals())
	if b==None:
		pass

	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Box")) == True:

		#Specifications inputs
		
		#Scale
		x1=(App.ActiveDocument.Box.Length)
		numx1=str(x1)
		numx=numx1.replace('mm','')
		numx=float(numx)
		numx=numx+App.ActiveDocument.Box.Placement.Base.x
		numx=str(numx)

		y1=(App.ActiveDocument.Box.Height)
		numy1=str(y1)
		numy=numy1.replace('mm','')
		numy=float(numy)
		numy=numy+App.ActiveDocument.Box.Placement.Base.z
		numy=str(numy)


		z1=(App.ActiveDocument.Box.Width)
		numz1=str(z1)
		numz=numz1.replace("mm","")
		numz=float(numz)
		numz=numz+App.ActiveDocument.Box.Placement.Base.y
		numz=str(numz)

		poly="""VER:   1.1
TYPE:  POLYHEDRA
Name:  Rock

_Geometry_Specifications_

GeometryFile: """+FreeCAD.getDocument(ap).getObject("Box").GeometryFile+"""
Scale: """+numx+""" """+numy+""" """+numz+"""

InertiaTensor:  MANUAL

"""+FreeCAD.getDocument(ap).getObject("Box").xx+"""    """+FreeCAD.getDocument(ap).getObject("Box").xy+"""   """+FreeCAD.getDocument(ap).getObject("Box").xz+"""
"""+FreeCAD.getDocument(ap).getObject("Box").yx+"""    """+FreeCAD.getDocument(ap).getObject("Box").yy+"""   """+FreeCAD.getDocument(ap).getObject("Box").yz+"""
"""+FreeCAD.getDocument(ap).getObject("Box").zx+"""    """+FreeCAD.getDocument(ap).getObject("Box").zy+"""   """+FreeCAD.getDocument(ap).getObject("Box").zz+"""

MATERIALFILE: """+FreeCAD.getDocument(ap).getObject("Box").MATERIALFILE

		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box").Label+".POBJ")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Box").Label+".POBJ")
		OBJ=open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt", "w")
		OBJ.write(poly)
		OBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box").Label+".POBJ")

	j=1
	for j in range (1,100):
		n=str(j)
		if j<10 and App.getDocument(ap).getObject("Box00"+n)==None:
			pass

		elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box00"+n)) == True:
			ldic=locals()
			exec("x1=App.ActiveDocument.Box00{}.Length".format(n),globals(),ldic)
			x1=ldic["x1"]
			numx1=str(x1)
			numx=numx1.replace('mm','')
			numx=float(numx)
			exec("r=App.ActiveDocument.Box00{}.Placement.Base.x".format(n),globals(),ldic)
			r=ldic["r"]
			numx=numx+r
			numx=str(numx)

			exec("y1=App.ActiveDocument.Box00{}.Width".format(n),globals(),ldic)
			y1=ldic["y1"]
			numy1=str(y1)
			numy=numy1.replace('mm','')
			numy=float(numy)
			exec("y=App.ActiveDocument.Box00{}.Placement.Base.y".format(n),globals(),ldic)
			y=ldic["y"]
			numy=numy+y
			numy=str(numy)

			exec("z1=App.ActiveDocument.Box00{}.Height".format(n),globals(),ldic)
			z1=ldic["z1"]
			numz1=str(z1)
			numz=numz1.replace('mm','')
			numz=float(numz)
			exec("z=App.ActiveDocument.Box00{}.Placement.Base.z".format(n),globals(),ldic)
			z=ldic["z"]
			numz=numz+z
			numz=str(numz)

			poly="""VER:   1.1
TYPE:  POLYHEDRA
Name:  Rock

_Geometry_Specifications_

GeometryFile: 12S
Scale: """+numx+""" """+numy+""" """+numz+"""

InertiaTensor:  MANUAL

"""+FreeCAD.getDocument(ap).getObject("Box00"+n).xx+"""    """+FreeCAD.getDocument(ap).getObject("Box00"+n).xy+"""   """+FreeCAD.getDocument(ap).getObject("Box00"+n).xz+"""
"""+FreeCAD.getDocument(ap).getObject("Box00"+n).yx+"""    """+FreeCAD.getDocument(ap).getObject("Box00"+n).yy+"""   """+FreeCAD.getDocument(ap).getObject("Box00"+n).yz+"""
"""+FreeCAD.getDocument(ap).getObject("Box00"+n).zx+"""    """+FreeCAD.getDocument(ap).getObject("Box00"+n).zy+"""   """+FreeCAD.getDocument(ap).getObject("Box00"+n).zz+"""

MATERIALFILE: """+FreeCAD.getDocument(ap).getObject("Box00"+n).MATERIALFILE

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".POBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".POBJ")
			OBJ=open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt", "w")
			OBJ.write(poly)
			OBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".POBJ")


		if j>10 and App.getDocument(ap).getObject("Box0"+n)==None:
			pass

		elif j > 10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box0"+n)) == True:
			ldic=locals()
			exec("x1=App.ActiveDocument.Box0{}.Length".format(n),globals(),ldic)
			x1=ldic["x1"]
			numx1=str(x1)
			numx=numx1.replace('mm','')
			numx=float(numx)
			exec("r=App.ActiveDocument.Box0{}.Placement.Base.x".format(n),globals(),ldic)
			r=ldic["r"]
			numx=numx+r
			numx=str(numx)

			exec("y1=App.ActiveDocument.Box0{}.Width".format(n),globals(),ldic)
			y1=ldic["y1"]
			numy1=str(y1)
			numy=numy1.replace('mm','')
			numy=float(numy)
			exec("y=App.ActiveDocument.Box0{}.Placement.Base.y".format(n),globals(),ldic)
			y=ldic["y"]
			numy=numy+y
			numy=str(numy)

			exec("z1=App.ActiveDocument.Box0{}.Height".format(n),globals(),ldic)
			z1=ldic["z1"]
			numz1=str(z1)
			numz=numz1.replace('mm','')
			numz=float(numz)
			exec("z=App.ActiveDocument.Box0{}.Placement.Base.z".format(n),globals(),ldic)
			z=ldic["z"]
			numz=numz+z
			numz=str(numz)

			poly="""VER:   1.1
TYPE:  POLYHEDRA
Name:  Rock

_Geometry_Specifications_

GeometryFile: 12S
Scale: """+numx+""" """+numy+""" """+numz+"""

InertiaTensor:  MANUAL

"""+FreeCAD.getDocument(ap).getObject("Box0"+n).xx+"""    """+FreeCAD.getDocument(ap).getObject("Box0"+n).xy+"""   """+FreeCAD.getDocument(ap).getObject("Box0"+n).xz+"""
"""+FreeCAD.getDocument(ap).getObject("Box0"+n).yx+"""    """+FreeCAD.getDocument(ap).getObject("Box0"+n).yy+"""   """+FreeCAD.getDocument(ap).getObject("Box0"+n).yz+"""
"""+FreeCAD.getDocument(ap).getObject("Box0"+n).zx+"""    """+FreeCAD.getDocument(ap).getObject("Box0"+n).zy+"""   """+FreeCAD.getDocument(ap).getObject("Box0"+n).zz+"""

MATERIALFILE: """+FreeCAD.getDocument(ap).getObject("Box0"+n).MATERIALFILE

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".POBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".POBJ")
			OBJ=open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt", "w")
			OBJ.write(poly)
			OBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".POBJ")

POBJ().exec_()