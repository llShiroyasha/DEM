# ***************************************************************************
# *   (c) Robin PORQUET (robin.porquet@gmail.com) 2019                      *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# *   Made during my internship in South Africa                             *
# *   Director of my internship: Pr. Daniel N. Wilke                        *
# *   Tutor in France: Pr. Patrick Pizette                                  *       
# *                                                                         *
# *   Robin PORQUET 2019                                                    *
# ***************************************************************************


from PySide import QtGui, QtCore
from PySide.QtGui import QListWidget
import os
import platform
import FreeCAD, FreeCADGui

App=FreeCAD
Gui=FreeCADGui

dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
os.chdir(dir_)

def box():
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""a1=App.getDocument("{}").getObject("Box")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""a1=App.getDocument("{}").getObject("Box")""".format(ap),globals())
	if a1 == None:
		pass
	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Box")) == True:
		a=0
		list1=[]
		i=0
		if FreeCAD.getDocument(ap).getObject("Box").Face1Front == True:
			i=i+1
		if FreeCAD.getDocument(ap).getObject("Box").Face2Bottom == True:
			i=i+1
		if FreeCAD.getDocument(ap).getObject("Box").Face3Top == True:
			i=i+1
		if FreeCAD.getDocument(ap).getObject("Box").Face4Rear == True:
			i=i+1
		if FreeCAD.getDocument(ap).getObject("Box").Face5Right == True:
			i=i+1
		if FreeCAD.getDocument(ap).getObject("Box").Face6Left == True:
			i=i+1
		i=str(i)
		print(i)

		for a in range (0,8):
			xp=App.ActiveDocument.Box.Shape.Vertexes[a].Point.x
			xp=xp*0.001
			xp=str(xp)
			list1.append(xp)
			yp=App.ActiveDocument.Box.Shape.Vertexes[a].Point.z
			yp=yp*0.001
			yp=str(yp)
			list1.append(yp)
			zp=App.ActiveDocument.Box.Shape.Vertexes[a].Point.y
			zp=zp*0.001
			zp=str(zp)
			list1.append(zp)
			a=a+1

		box="""Ver: 1.1
Type: PLANAR
	
Geometry-Specfications

NUM_VERTEX: 8

1 """+list1[3]+""" """+list1[4]+""" """+list1[5]+""" 
2 """+list1[9]+""" """+list1[10]+""" """+list1[11]+"""
3 """+list1[21]+""" """+list1[22]+""" """+list1[23]+"""
4 """+list1[15]+""" """+list1[16]+""" """+list1[17]+"""
5 """+list1[0]+""" """+list1[1]+""" """+list1[2]+"""
6 """+list1[6]+""" """+list1[7]+""" """+list1[8]+"""
7 """+list1[18]+""" """+list1[19]+""" """+list1[20]+"""
8 """+list1[12]+""" """+list1[13]+""" """+list1[14]+"""

NUM_SURFACES: """+i+""" """

		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box").Label+".WOBJ")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Box").Label+".WOBJ")
		WOBJ=open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt", "w+")
		WOBJ.write(box)
		WOBJ.close()

	
		if FreeCAD.getDocument(ap).getObject("Box").Face1Front == True:
			file = open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt" , 'a') 
			file.write("""

4
8 4 1 5
""")
			file.close()
		if FreeCAD.getDocument(ap).getObject("Box").Face2Bottom == True:
			file = open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt" , 'a') 
			file.write("""
4
4 3 2 1
""")
			file.close()
		if FreeCAD.getDocument(ap).getObject("Box").Face3Top == True:
			file = open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt" , 'a') 
			file.write("""
4
5 6 7 8
""")
			file.close()
		if FreeCAD.getDocument(ap).getObject("Box").Face4Rear == True:
			file = open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt" , 'a') 
			file.write("""
4
6 2 3 7
""")
			file.close()
		if FreeCAD.getDocument(ap).getObject("Box").Face5Right == True:
			file = open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt" , 'a') 
			file.write("""
4
7 3 4 8
""")
			file.close()
		if FreeCAD.getDocument(ap).getObject("Box").Face6Left == True:
			file = open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt" , 'a') 
			file.write("""
4
5 1 2 6
""")
			file.close()

		tell="""MATERIALFILE: Wall

"""
		WOBJ=open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt", "a")
		WOBJ.write(tell)
		WOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box").Label+".WOBJ")
		
	j=1
	for j in range (1,100):
		n=str(j)
		a=App.getDocument(ap).getObject("Box00"+n)
		if j<10 and a==None:
			pass
		elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box00"+n)) == True:
			a=0
			list1=[]
			for a in range (0,8):
				a=str(a)
				ldic=locals()			
				exec("f=App.ActiveDocument.Box00{}.Shape.Vertexes[{}].Point.x".format(n,a),globals(),ldic) 
				f=ldic["f"]
				f=float(f)
				f=f*0.001
				f=str(f)
				list1.append(f)
				exec("r=App.ActiveDocument.Box00{}.Shape.Vertexes[{}].Point.z".format(n,a),globals(),ldic)
				r=ldic["r"]
				r=float(r)
				r=r*0.001
				r=str(r)
				list1.append(r)
				exec("p=App.ActiveDocument.Box00{}.Shape.Vertexes[{}].Point.y".format(n,a),globals(),ldic)
				p=ldic["p"]
				p=float(p)
				p=p*0.001
				p=str(p)
				list1.append(p)
				a=float(a)
				a=a+1

			i1=0
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face1Front == True:
				i1=i1+1
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face2Bottom == True:
				i1=i1+1
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face3Top == True:
				i1=i1+1
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face4Rear == True:
				i1=i1+1
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face5Right == True:
				i1=i1+1
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face6Left == True:
				i1=i1+1
			i1=str(i1)
			print(i1)

			Cam="""Ver: 1.1
Type: PLANAR
	
Geometry-Specfications

NUM_VERTEX: 8

1 """+list1[3]+""" """+list1[4]+""" """+list1[5]+""" 
2 """+list1[9]+""" """+list1[10]+""" """+list1[11]+"""
3 """+list1[21]+""" """+list1[22]+""" """+list1[23]+"""
4 """+list1[15]+""" """+list1[16]+""" """+list1[17]+"""
5 """+list1[0]+""" """+list1[1]+""" """+list1[2]+"""
6 """+list1[6]+""" """+list1[7]+""" """+list1[8]+"""
7 """+list1[18]+""" """+list1[19]+""" """+list1[20]+"""
8 """+list1[12]+""" """+list1[13]+""" """+list1[14]+"""

NUM_SURFACES: """+i1+""" """

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".WOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".WOBJ")
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt", "w+")
			WOBJ.write(Cam)
			WOBJ.close()

	
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face1Front == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt" , 'a') 
				file.write("""

4
8 4 1 5
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face2Bottom == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt" , 'a') 
				file.write("""
4
8 7 6 5
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face3Top == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt" , 'a') 
				file.write("""
4
7 3 1 5
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face4Rear == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt" , 'a') 
				file.write("""
4
6 2 3 7
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face5Right == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt" , 'a') 
				file.write("""
4
5 6 8 7
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Face6Left == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt" , 'a') 
				file.write("""
4
7 3 4 8
""")
				file.close()

			tell="""MATERIALFILE: Wall

"""
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt", "a")
			WOBJ.write(tell)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".WOBJ")

		a=App.getDocument(ap).getObject("Box0"+n)
		if j > 10 and a==None:
			pass

		elif j > 10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box0"+n)) == True:
			i=0
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face1Front == True:
				i=i+1
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face2Bottom == True:
				i=i+1
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face3Top == True:
				i=i+1
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face4Rear == True:
				i=i+1
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face5Right == True:
				i=i+1
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face6Left == True:
				i=i+1
			i=str(i)
			a=0
			list1=[]
			for a in range (0,8):
				a=str(a)
				ldic=locals()			
				exec("f=App.ActiveDocument.Box0{}.Shape.Vertexes[{}].Point.x".format(n,a),globals(),ldic) 
				f=ldic["f"]
				f=f*0.001
				f=str(f)
				list1.append(f)
				exec("r=App.ActiveDocument.Box0{}.Shape.Vertexes[{}].Point.z".format(n,a),globals(),ldic)
				r=ldic["r"]
				r=r*0.001
				r=str(r)
				list1.append(r)
				exec("p=App.ActiveDocument.Box0{}.Shape.Vertexes[{}].Point.y".format(n,a),globals(),ldic)
				p=ldic["p"]
				p=p*0.001
				p=str(p)
				list1.append(p)
				a=float(a)
				a=a+1
			Cam="""Ver: 1.1
Type: PLANAR
	
Geometry-Specfications

NUM_VERTEX: 8

1 """+list1[3]+""" """+list1[4]+""" """+list1[5]+""" 
2 """+list1[9]+""" """+list1[10]+""" """+list1[11]+"""
3 """+list1[21]+""" """+list1[22]+""" """+list1[23]+"""
4 """+list1[15]+""" """+list1[16]+""" """+list1[17]+"""
5 """+list1[0]+""" """+list1[1]+""" """+list1[2]+"""
6 """+list1[6]+""" """+list1[7]+""" """+list1[8]+"""
7 """+list1[18]+""" """+list1[19]+""" """+list1[20]+"""
8 """+list1[12]+""" """+list1[13]+""" """+list1[14]+"""

NUM_SURFACES: """+i+""" """

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".WOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".WOBJ")
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt", "w+")
			WOBJ.write(Cam)
			WOBJ.close()

	
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face1Front == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt" , 'a') 
				file.write("""

4
8 4 1 5
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face2Bottom == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt" , 'a') 
				file.write("""
4
8 7 6 5
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face3Top == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt" , 'a') 
				file.write("""
4
7 3 1 5
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face4Rear == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt" , 'a') 
				file.write("""
4
6 2 3 7
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face5Right == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt" , 'a') 
				file.write("""
4
5 6 8 7
""")
				file.close()
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Face6Left == True:
				file = open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt" , 'a') 
				file.write("""
4
7 3 4 8
""")
				file.close()

			tell="""

MATERIALFILE: Wall

"""
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt", "a")
			WOBJ.write(tell)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".WOBJ")
			j=j+1

box()

def rectangle():
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""b=App.getDocument("{}").getObject("Rect")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""b=App.getDocument("{}").getObject("Rect")""".format(ap),globals())
	if b==None:
		pass
	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Rect")) == True:
		a=0
		list1=[]
		for a in range (0,4):
			xp=App.ActiveDocument.Rect.Shape.Vertexes[a].Point.x
			xp=xp*0.001
			xp=str(xp)
			list1.append(xp)
			yp=App.ActiveDocument.Rect.Shape.Vertexes[a].Point.z
			yp=yp*0.001
			yp=str(yp)
			list1.append(yp)
			zp=App.ActiveDocument.Rect.Shape.Vertexes[a].Point.y
			zp=zp*0.001
			zp=str(zp)
			list1.append(zp)
			a=a+1
			print(xp,yp,zp)
		rect="""Ver: 1.1
Type: PLANAR
	
Geometry-Specfications

NUM_VERTEX: 4

1 """+list1[0]+""" """+list1[1]+""" """+list1[2]+"""
2 """+list1[3]+""" """+list1[4]+""" """+list1[5]+""" 
3 """+list1[6]+""" """+list1[7]+""" """+list1[8]+"""
4 """+list1[9]+""" """+list1[10]+""" """+list1[11]+"""


NUM_SURFACES: 1
	
4
1 2 3 4

MATERIALFILE: Wall

"""

		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Rect").Label+".WOBJ")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Rect").Label+".WOBJ")
		WOBJ=open(FreeCAD.getDocument(ap).getObject("Rect").Label+".txt", "w")
		WOBJ.write(rect)
		WOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Rect").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Rect").Label+".WOBJ")

	j=1
	for j in range (1,100):
		n=str(j)
		a=App.getDocument(ap).getObject("Rect00"+n)
		if j<10 and a==None:
			pass
		elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Rect00"+n)) == True:
			a=0
			list1=[]
			for a in range (0,4):
				a=str(a)
				ldic=locals()			
				exec("f=App.ActiveDocument.Rect00{}.Shape.Vertexes[{}].Point.x".format(n,a),globals(),ldic) 
				f=ldic["f"]
				f=f*0.001
				f=str(f)
				list1.append(f)
				exec("r=App.ActiveDocument.Rect00{}.Shape.Vertexes[{}].Point.z".format(n,a),globals(),ldic)
				r=ldic["r"]
				r=r*0.001
				r=str(r)
				list1.append(r)
				exec("p=App.ActiveDocument.Rect00{}.Shape.Vertexes[{}].Point.y".format(n,a),globals(),ldic)
				p=ldic["p"]
				p=p*0.001
				p=str(p)
				list1.append(p)
				a=float(a)
				a=a+1
			Cam="""Ver: 1.1
Type: PLANAR
	
Geometry-Specfications

NUM_VERTEX: 8

1 """+list1[0]+""" """+list1[1]+""" """+list1[2]+"""
2 """+list1[3]+""" """+list1[4]+""" """+list1[5]+""" 
3 """+list1[6]+""" """+list1[7]+""" """+list1[8]+"""
4 """+list1[9]+""" """+list1[10]+""" """+list1[11]+"""

NUM_SURFACES: 1
	
4
1 2 3 4
	
MATERIALFILE: Wall

"""
			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Rect00"+n).Label+".WOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Rect00"+n).Label+".WOBJ")
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Rect00"+n).Label+".txt", "w")
			WOBJ.write(Cam)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Rect00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Rect00"+n).Label+".WOBJ")

		a=App.getDocument(ap).getObject("Rect0"+n)
		if j > 10 and a==None:
			pass
		elif j > 10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Rect0"+n)) == True:
			a=0
			list1=[]
			for a in range (0,4):
				a=str(a)
				ldic=locals()			
				exec("f=App.ActiveDocument.Rect0{}.Shape.Vertexes[{}].Point.x".format(n,a),globals(),ldic) 
				f=ldic["f"]
				f=f*0.001
				f=str(f)
				list1.append(f)
				exec("r=App.ActiveDocument.Rect0{}.Shape.Vertexes[{}].Point.z".format(n,a),globals(),ldic)
				r=ldic["r"]
				r=r*0.001
				r=str(r)
				list1.append(r)
				exec("p=App.ActiveDocument.Rect0{}.Shape.Vertexes[{}].Point.y".format(n,a),globals(),ldic)
				p=ldic["p"]
				p=p*0.001
				p=str(p)
				list1.append(p)
				a=float(a)
				a=a+1
			Cam="""Ver: 1.1
Type: PLANAR
	
Geometry-Specfications

NUM_VERTEX: 8

1 """+list1[0]+""" """+list1[1]+""" """+list1[2]+"""
2 """+list1[3]+""" """+list1[4]+""" """+list1[5]+""" 
3 """+list1[6]+""" """+list1[7]+""" """+list1[8]+"""
4 """+list1[9]+""" """+list1[10]+""" """+list1[11]+"""

NUM_SURFACES: 1
	
4
1 2 3 4
	
MATERIALFILE: Wall

"""
			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Rect0"+n).Label+".WOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Rect0"+n).Label+".WOBJ")
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Rect0"+n).Label+".txt", "w")
			WOBJ.write(Cam)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Rect0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Rect0"+n).Label+".WOBJ")


rectangle()

def cylinder():
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""e=App.getDocument("{}").getObject("Cylinder")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""e=App.getDocument("{}").getObject("Cylinder")""".format(ap),globals())
	if e==None:
		pass
	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder"))== True:
	
		d1=FreeCAD.getDocument(ap).getObject("Cylinder").Radius*2
		d1=d1*0.001
		numd=str(d1)
		d=numd.replace('mm','')
		r1=FreeCAD.getDocument(ap).getObject("Cylinder").Radius
		r1=r1*0.001
		numr=str(r1)
		r=numr.replace('mm','')

		z=App.ActiveDocument.Cylinder.Placement.Base.z
		h1=FreeCAD.getDocument(ap).getObject("Cylinder").Height
		numh=str(h1)
		h=numh.replace('mm','')
		h=float(h)
		h=h*0.001
		z=z*0.001
		h=h+z
		h=str(h)
		z=str(z)

		Shell="""VER:     1.1
Type:    ANALYTICAL
Shape:   CYLINDER
Normal:  INWARD

Geometry-Specfications
Diameter:   """+d+"""
BaseCenter: """+r+""" """+r+"""  """+z+"""
TopCenter:  """+r+""" """+r+"""  """+h+"""
HasTop:     true
HasBot:     true
"""

		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Cylinder").Label+".WOBJ")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Cylinder").Label+".WOBJ")
		WOBJ=open(FreeCAD.getDocument(ap).getObject("Cylinder").Label+".txt", "w")
		WOBJ.write(Shell)
		WOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder").Label+".WOBJ")
	j=1
	for j in range (1,100):
		n=str(j)
		a=App.getDocument(ap).getObject("Cylinder00"+n)
		if j<10 and a==None:
			pass

		elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder00"+n)) == True:
			d1=FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Radius*2
			d1=d1*0.001
			numd=str(d1)
			d=numd.replace('mm','')

			r1=FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Radius
			r1=r1*0.001
			numr=str(r1)
			r=numr.replace('mm','')
	
			ldic=locals()
			exec("z=App.ActiveDocument.Cylinder00{}.Placement.Base.z".format(n),globals(),ldic)
			z=ldic["z"]
			z=float(z)
			h1=FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Height
			numh=str(h1)
			h=numh.replace('mm','')
			h=float(h)
			z=z*0.001
			h=h*0.001
			h=h+z
			h=str(h)
			z=str(z)

			Shell="""VER:     1.1
Type:    ANALYTICAL
Shape:   CYLINDER
Normal:  INWARD

Geometry-Specfications
Diameter:   """+d+"""
BaseCenter: """+r+""" """+r+"""  """+z+"""
TopCenter:  """+r+""" """+r+"""  """+h+"""
HasTop:     true
HasBot:     true
"""
			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".WOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".WOBJ")
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".txt", "w")
			WOBJ.write(Shell)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".WOBJ")
	
		a=App.getDocument(ap).getObject("Cylinder0"+n)
		if j>10 and a==None:
			pass
		elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder0"+n)) == True:
			d1=FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Radius*2
			d1=d1*0.001
			numd=str(d1)
			d=numd.replace('mm','')

			r1=FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Radius
			r1=r1*0.001
			numr=str(r1)
			r=numr.replace('mm','')
	
			ldic=locals()
			exec("z=App.ActiveDocument.Cylinder0{}.Placement.Base.z".format(n),globals(),ldic)
			z=ldic["z"]
			z=float(z)
			h1=FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Height
			numh=str(h1)
			h=numh.replace('mm','')
			h=float(h)
			h=h*0.001
			z=z*0.001
			h=h+z
			h=str(h)
			z=str(z)

			Shell="""VER:     1.1
Type:    ANALYTICAL
Shape:   CYLINDER
Normal:  INWARD

Geometry-Specfications
Diameter:   """+d+"""
BaseCenter: """+r+""" """+r+"""  """+z+"""
TopCenter:  """+r+""" """+r+"""  """+h+"""
HasTop:     true
HasBot:     true
"""
			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".WOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".WOBJ")
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".txt", "w")
			WOBJ.write(Shell)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".WOBJ")

cylinder()

def sphere():
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""c=App.getDocument("{}").getObject("Sphere")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""c=App.getDocument("{}").getObject("Sphere")""".format(ap),globals())
	if c==None:
		pass

	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere"))== True:
		r1=FreeCAD.getDocument(ap).getObject("Sphere").Radius*2
		numr=str(r1)
		r=numr.replace('mm','')
		f=float(r)
		f=f*0.001
		f=str(f)
		x1=App.ActiveDocument.Sphere.Placement.Base.x	
		x1=x1*0.001	
		numx1=str(x1)
		x=numx1.replace('mm','')
		y1=App.ActiveDocument.Sphere.Placement.Base.z
		y1=y1*0.001
		numy1=str(y1)
		y=numy1.replace('mm','')
		z1=App.ActiveDocument.Sphere.Placement.Base.y
		z1=z1*0.001
		numz1=str(z1)
		z=numz1.replace('mm','')

		Sphere=""" VER: 1.1
TYPE: SPHERE

Geometry-Specfications

Diameter: """ +r+"""
Center = """+x+""" """+y+""" """+z

		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere").Label+".WOBJ")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere").Label+".WOBJ")
		WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere").Label+".txt", "w")
		WOBJ.write(Sphere)
		WOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere").Label+".WOBJ")

	j=1
	for j in range (1,100):
		n=str(j)
		a=App.getDocument(ap).getObject("Sphere00"+n)
		if j<10 and a==None:
			pass
		elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere00"+n)) == True:
			a=0
			r1=FreeCAD.getDocument(ap).getObject("Sphere00"+n).Radius*2
			numr=str(r1)
			r=numr.replace('mm','')
			ldic=locals()			
			exec("f=App.ActiveDocument.Sphere00"+n+".Placement.Base.x",globals(),ldic) 
			f=ldic["f"]
			f=f*0.001
			f=str(f)
			exec("z=App.ActiveDocument.Sphere00"+n+".Placement.Base.y",globals(),ldic)
			z=ldic["z"]
			z=z*0.001
			z=str(z)
			exec("p=App.ActiveDocument.Sphere00"+n+".Placement.Base.z",globals(),ldic)
			p=ldic["p"]
			p=p*0.001
			p=str(p)
			a=float(a)
			a=a+1
			Sphere=""" VER: 1.1
TYPE: SPHERE

Geometry-Specfications

Diameter: """ +r+"""
Center = """+f+""" """+z+""" """+p

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".WOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".WOBJ")
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".txt", "w")
			WOBJ.write(Sphere)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".WOBJ")
		
		a=App.getDocument(ap).getObject("Sphere0"+n)
		if j>10 and a==None:
			pass
		elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere0"+n)) == True:
			a=0
			r1=FreeCAD.getDocument(ap).getObject("Sphere0"+n).Radius*2
			numr=str(r1)
			r=numr.replace('mm','')
			ldic=locals()			
			exec("f=App.ActiveDocument.Sphere0"+n+".Placement.Base.x",globals(),ldic)
			f=f*0.001
			f=ldic["f"]
			f=str(f)
			exec("z=App.ActiveDocument.Sphere0"+n+".Placement.Base.y",globals(),ldic)
			z=z*0.001
			z=ldic["z"]
			z=str(z)
			exec("p=App.ActiveDocument.Sphere0"+n+".Placement.Base.z",globals(),ldic)
			p=ldic["p"]
			p=p*0.001
			p=str(p)
			a=float(a)
			a=a+1
			Sphere=""" VER: 1.1
TYPE: SPHERE

Geometry-Specfications

Diameter: """ +r+"""
Center = """+f+""" """+z+""" """+p

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".WOBJ")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".WOBJ")
			WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".txt", "w")
			WOBJ.write(Sphere)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".WOBJ")
            
Maker = sphere()
Maker()