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

ap=App.ActiveDocument.Name


            
def matBox():
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""a=App.getDocument("{}").getObject("Box")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""a=App.getDocument("{}").getObject("Box")""".format(ap),globals())

		if FreeCAD.getDocument(ap).getObject("Box").Density=="":
			ar=""
		else:
			ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Box").Density
	
		if FreeCAD.getDocument(ap).getObject("Box").COR=="":
			art=""
		else:
			art="""COR:          """+FreeCAD.getDocument(ap).getObject("Box").COR

		if FreeCAD.getDocument(ap).getObject("Box").Static_friction=="":
			arte=""
		else:
			arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Box").Static_friction
	
		if FreeCAD.getDocument(ap).getObject("Box").Kinetic_friction=="":
			artem=""
		else:
			artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Box").Kinetic_friction
	
		if FreeCAD.getDocument(ap).getObject("Box").ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Box").ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Box").InitTemp=="":
			artemi=""
		else:
			artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Box").ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Box").ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Box").InitTemp)

		if FreeCAD.getDocument(ap).getObject("Box").RollingDamp=="":
			artemis=""
		else:
			artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Box").RollingDamp

	if a==None:
		pass
	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Box")) == True:

		Box="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""

_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Box").Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Box").Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box").Label+".MAT")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Box").Label+".MAT")

		WOBJ=open(FreeCAD.getDocument(ap).getObject("Box").Label+".txt", "w")
		WOBJ.write(Box)
		WOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box").Label+".MAT")
	j=1
	for j in range (1,100):
		n=str(j)
		if j < 10 and App.getDocument(ap).getObject("Box00"+n)== None:
			pass
		elif j < 10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box00"+n)) == True :

			if FreeCAD.getDocument(ap).getObject("Box00"+n).Density=="":
				ar=""
			else:
				ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Box00"+n).Density
	
			if FreeCAD.getDocument(ap).getObject("Box00"+n).COR=="":
				art=""
			else:
				art="""COR:          """+FreeCAD.getDocument(ap).getObject("Box00"+n).COR

			if FreeCAD.getDocument(ap).getObject("Box00"+n).Static_friction=="":
				arte=""
			else:
				arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Box00"+n).Static_friction
	
			if FreeCAD.getDocument(ap).getObject("Box00"+n).Kinetic_friction=="":
				artem=""
			else:
				artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Box00"+n).Kinetic_friction
	
			if FreeCAD.getDocument(ap).getObject("Box00"+n).ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Box00"+n).ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Box00"+n).InitTemp=="":
				artemi=""
			else:
				artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Box00"+n).ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Box00"+n).ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Box00"+n).InitTemp)

			if FreeCAD.getDocument(ap).getObject("Box00"+n).RollingDamp=="":
				artemis=""
			else:
				artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Box00"+n).RollingDamp

			Box="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""

_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Box00"+n).Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Box00"+n).Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".MAT")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".MAT")

			WOBJ=open(FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt", "w")
			WOBJ.write(Box)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box00"+n).Label+".MAT")

		if j > 10 and App.getDocument(ap).getObject("Box0"+n)== None:
			pass
		elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box0"+n)) == True :

			if FreeCAD.getDocument(ap).getObject("Box0"+n).Density=="":
				ar=""
			else:
				ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Box0"+n).Density
	
			if FreeCAD.getDocument(ap).getObject("Box0"+n).COR=="":
				art=""
			else:
				art="""COR:          """+FreeCAD.getDocument(ap).getObject("Box0"+n).COR

			if FreeCAD.getDocument(ap).getObject("Box0"+n).Static_friction=="":
				arte=""
			else:
				arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Box0"+n).Static_friction
	
			if FreeCAD.getDocument(ap).getObject("Box0"+n).Kinetic_friction=="":
				artem=""
			else:
				artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Box0"+n).Kinetic_friction
	
			if FreeCAD.getDocument(ap).getObject("Box0"+n).ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Box0"+n).ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Box0"+n).InitTemp=="":
				artemi=""
			else:
				artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Box0"+n).ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Box0"+n).ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Box0"+n).InitTemp)

			if FreeCAD.getDocument(ap).getObject("Box0"+n).RollingDamp=="":
				artemis=""
			else:
				artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Box0"+n).RollingDamp

			Box="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""

_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Box0"+n).Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Box0"+n).Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".MAT")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".MAT")

			WOBJ=open(FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt", "w")
			WOBJ.write(Box)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Box0"+n).Label+".MAT")

def MatCyl():
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""a=App.getDocument("{}").getObject("Cylinder")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""a=App.getDocument("{}").getObject("Cylinder")""".format(ap),globals())
    
		if FreeCAD.getDocument(ap).getObject("Cylinder").Density=="":
			ar=""
		else:
			ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Cylinder").Density
	
		if FreeCAD.getDocument(ap).getObject("Cylinder").COR=="":
			art=""
		else:
			art="""COR:          """+FreeCAD.getDocument(ap).getObject("Cylinder").COR

		if FreeCAD.getDocument(ap).getObject("Cylinder").Static_friction=="":
			arte=""
		else:
			arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Cylinder").Static_friction
	
		if FreeCAD.getDocument(ap).getObject("Cylinder").Kinetic_friction=="":
			artem=""
		else:
			artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Cylinder").Kinetic_friction
	
		if FreeCAD.getDocument(ap).getObject("Cylinder").ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Cylinder").ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Cylinder").InitTemp=="":
			artemi=""
		else:
			artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Cylinder").ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Cylinder").ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Cylinder").InitTemp)

		if FreeCAD.getDocument(ap).getObject("Cylinder").RollingDamp=="":
			artemis=""
		else:
			artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Cylinder").RollingDamp

	if a==None:
		pass
	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder")) == True:

		Cylinder="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""

_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Cylinder").Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Cylinder").Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Cylinder").Label+".MAT")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Cylinder").Label+".MAT")

		WOBJ=open(FreeCAD.getDocument(ap).getObject("Cylinder").Label+".txt", "w")
		WOBJ.write(Cylinder)
		WOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder").Label+".MAT")
	j=1
	for j in range (1,100):
		n=str(j)
		if j < 10 and App.getDocument(ap).getObject("Cylinder00"+n)== None:
			pass
		elif j < 10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder00"+n)) == True :

			if FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Density=="":
				ar=""
			else:
				ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Density
	
			if FreeCAD.getDocument(ap).getObject("Cylinder00"+n).COR=="":
				art=""
			else:
				art="""COR:          """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).COR

			if FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Static_friction=="":
				arte=""
			else:
				arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Static_friction
	
			if FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Kinetic_friction=="":
				artem=""
			else:
				artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Kinetic_friction
	
			if FreeCAD.getDocument(ap).getObject("Cylinder00"+n).ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Cylinder00"+n).ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Cylinder00"+n).InitTemp=="":
				artemi=""
			else:
				artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).InitTemp)

			if FreeCAD.getDocument(ap).getObject("Cylinder00"+n).RollingDamp=="":
				artemis=""
			else:
				artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).RollingDamp

			Cylinder="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""


_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".MAT")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".MAT")

			WOBJ=open(FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".txt", "w")
			WOBJ.write(Cylinder)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder00"+n).Label+".MAT")

		if j > 10 and App.getDocument(ap).getObject("Cylinder0"+n)== None:
			pass
		elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder0"+n)) == True :

			if FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Density=="":
				ar=""
			else:
				ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Density
	
			if FreeCAD.getDocument(ap).getObject("Cylinder0"+n).COR=="":
				art=""
			else:
				art="""COR:          """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).COR

			if FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Static_friction=="":
				arte=""
			else:
				arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Static_friction
	
			if FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Kinetic_friction=="":
				artem=""
			else:
				artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Kinetic_friction
	
			if FreeCAD.getDocument(ap).getObject("Cylinder0"+n).ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Cylinder0"+n).ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Cylinder0"+n).InitTemp=="":
				artemi=""
			else:
				artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).InitTemp)

			if FreeCAD.getDocument(ap).getObject("Cylinder0"+n).RollingDamp=="":
				artemis=""
			else:
				artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).RollingDamp

			Cylinder="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""

_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".MAT")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".MAT")

			WOBJ=open(FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".txt", "w")
			WOBJ.write(Cylinder)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Cylinder0"+n).Label+".MAT")
            
def matSphere():
	if App.ActiveDocument.Name == "Unnamed":
		ap=App.ActiveDocument.Name
		exec("""a=App.getDocument("{}").getObject("Sphere")""".format(ap),globals())
	elif App.ActiveDocument.Name == "Sans_nom":
		ap=App.ActiveDocument.Name
		exec("""a=App.getDocument("{}").getObject("Sphere")""".format(ap),globals())

		if FreeCAD.getDocument(ap).getObject("Sphere").Density=="":
			ar=""
		else:
			ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Sphere").Density
	
		if FreeCAD.getDocument(ap).getObject("Sphere").COR=="":
			art=""
		else:
			art="""COR:          """+FreeCAD.getDocument(ap).getObject("Sphere").COR

		if FreeCAD.getDocument(ap).getObject("Sphere").Static_friction=="":
			arte=""
		else:
			arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Sphere").Static_friction
	
		if FreeCAD.getDocument(ap).getObject("Sphere").Kinetic_friction=="":
			artem=""
		else:
			artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Sphere").Kinetic_friction
	
		if FreeCAD.getDocument(ap).getObject("Sphere").ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Sphere").ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Sphere").InitTemp=="":
			artemi=""
		else:
			artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Sphere").ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Sphere").ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Sphere").InitTemp)

		if FreeCAD.getDocument(ap).getObject("Sphere").RollingDamp=="":
			artemis=""
		else:
			artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Sphere").RollingDamp

	if a==None:
		pass
	elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere")) == True:

		Sphere="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""

_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Sphere").Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Sphere").Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

		if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere").Label+".MAT")==True:
			test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere").Label+".MAT")

		WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere").Label+".txt", "w")
		WOBJ.write(Sphere)
		WOBJ.close()
		os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere").Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere").Label+".MAT")
	j=1
	for j in range (1,100):
		n=str(j)
		if j < 10 and App.getDocument(ap).getObject("Sphere00"+n)== None:
			pass
		elif j < 10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere00"+n)) == True :

			if FreeCAD.getDocument(ap).getObject("Sphere00"+n).Density=="":
				ar=""
			else:
				ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Density
	
			if FreeCAD.getDocument(ap).getObject("Sphere00"+n).COR=="":
				art=""
			else:
				art="""COR:          """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).COR

			if FreeCAD.getDocument(ap).getObject("Sphere00"+n).Static_friction=="":
				arte=""
			else:
				arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Static_friction
	
			if FreeCAD.getDocument(ap).getObject("Sphere00"+n).Kinetic_friction=="":
				artem=""
			else:
				artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Kinetic_friction
	
			if FreeCAD.getDocument(ap).getObject("Sphere00"+n).ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Sphere00"+n).ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Sphere00"+n).InitTemp=="":
				artemi=""
			else:
				artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).InitTemp)

			if FreeCAD.getDocument(ap).getObject("Sphere00"+n).RollingDamp=="":
				artemis=""
			else:
				artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).RollingDamp

			Sphere="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""

_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".MAT")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".MAT")

			WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".txt", "w")
			WOBJ.write(Sphere)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere00"+n).Label+".MAT")

		if j > 10 and App.getDocument(ap).getObject("Sphere0"+n)== None:
			pass
		elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere0"+n)) == True :

			if FreeCAD.getDocument(ap).getObject("Sphere0"+n).Density=="":
				ar=""
			else:
				ar="""Density:          """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Density
	
			if FreeCAD.getDocument(ap).getObject("Sphere0"+n).COR=="":
				art=""
			else:
				art="""COR:          """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).COR

			if FreeCAD.getDocument(ap).getObject("Sphere0"+n).Static_friction=="":
				arte=""
			else:
				arte="""STATICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Static_friction
	
			if FreeCAD.getDocument(ap).getObject("Sphere0"+n).Kinetic_friction=="":
				artem=""
			else:
				artem="""KINETICFRICTION:          """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Kinetic_friction
	
			if FreeCAD.getDocument(ap).getObject("Sphere0"+n).ThermalCond=="" and FreeCAD.getDocument(ap).getObject("Sphere0"+n).ThermalCap=="" and FreeCAD.getDocument(ap).getObject("Sphere0"+n).InitTemp=="":
				artemi=""
			else:
				artemi=("""_HeatParamaters_

ThermalCond:  """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).ThermalCond+"""
ThermalCap:   """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).ThermalCap+"""
InitTemp:     """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).InitTemp)

			if FreeCAD.getDocument(ap).getObject("Sphere0"+n).RollingDamp=="":
				artemis=""
			else:
				artemis="""_RotationParamaters_
ROLLINGDAMP:  """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).RollingDamp

			Sphere="""_Material_Specifications_

"""+ar+"""

"""+art+"""
"""+arte+"""
"""+artem+"""

"""+artemi+"""

_Numerical_Specifications_

_NormalParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Contact_time+"""

_TangentParamaters_
CONTACT_TIME  """+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Contacttime+"""

"""+artemis+"""

_CohesionParamaters(Optional)_"""

			if os.path.isfile(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".MAT")==True:
				test=os.remove(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".MAT")

			WOBJ=open(FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".txt", "w")
			WOBJ.write(Sphere)
			WOBJ.close()
			os.rename(dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".txt",dir_+"/"+FreeCAD.getDocument(ap).getObject("Sphere0"+n).Label+".MAT")

def MatConv():
    if App.getDocument(ap).getObject("Box")==None:
        pass
    elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Box"))== True:
        matBox()
        
    if App.getDocument(ap).getObject("Cylinder")==None:
        pass        
    elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder"))== True:
        MatCyl()
        
    if App.getDocument(ap).getObject("Sphere")==None:
        pass
    elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere"))== True:
        matSphere()


Mat=MatConv()
Mat.exec_()

    
