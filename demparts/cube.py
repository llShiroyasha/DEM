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


import FreeCAD, Part, math
from FreeCAD import Base
from pivy import coin
import FreeCAD, FreeCADGui

App=FreeCAD
Gui=FreeCADGui

class PartFeature:
	def __init__(self, obj):
		obj.Proxy = self

class Box(PartFeature):
	def __init__(self, obj):
		PartFeature.__init__(self, obj)
		obj.addProperty("App::PropertyLength","Length","Box","Length of the box").Length=10.0
		obj.addProperty("App::PropertyLength","Width","Box","Width of the box").Width=10.0
		obj.addProperty("App::PropertyLength","Height","Box", "Height of the box").Height=10.0
		obj.addProperty("App::PropertyString","COR","Material specifications","COR of the box").COR=""
		obj.addProperty("App::PropertyString","Static_friction","Material specifications","Static friction of the box").Static_friction=""
		obj.addProperty("App::PropertyString","Kinetic_friction","Material specifications","Kinetic friction of the box").Kinetic_friction=""
		obj.addProperty("App::PropertyString","Contact_time","Normal parameters","Contact time for normal parameters of the box").Contact_time=""
		obj.addProperty("App::PropertyString","Contacttime","Tangent parameters","Contact time for tangent parameters of the box").Contacttime=""
		obj.addProperty("App::PropertyString","xx","Inertia tensor","Inertia tensor for xx").xx=""
		obj.addProperty("App::PropertyString","xy","Inertia tensor","Inertia tensor for xy").xy=""
		obj.addProperty("App::PropertyString","xz","Inertia tensor","Inertia tensor for xz").xz=""
		obj.addProperty("App::PropertyString","yx","Inertia tensor","Inertia tensor for yx").yx=""
		obj.addProperty("App::PropertyString","yy","Inertia tensor","Inertia tensor for yy").yy=""
		obj.addProperty("App::PropertyString","yz","Inertia tensor","Inertia tensor for yz").yz=""
		obj.addProperty("App::PropertyString","zx","Inertia tensor","Inertia tensor for zx").zx=""
		obj.addProperty("App::PropertyString","zy","Inertia tensor","Inertia tensor for zy").zy=""
		obj.addProperty("App::PropertyString","zz","Inertia tensor","Inertia tensor for zz").zz=""
		obj.addProperty("App::PropertyString","Density","Material specifications","Density of the sphere").Density=""
		obj.addProperty("App::PropertyString","RollingDamp","Rotation parameters","Rolling Damp of the sphere").RollingDamp=""
		obj.addProperty("App::PropertyString","ThermalCond","HeatParameters","Thermal condition").ThermalCond=""
		obj.addProperty("App::PropertyString","ThermalCap","HeatParameters","Thermal Capacity").ThermalCap=""
		obj.addProperty("App::PropertyString","InitTemp","HeatParameters","Initial temperature").InitTemp=""
		obj.addProperty("App::PropertyBool","Face1Front","Visibility on WOBJ file","Is visible on WOBJ file").Face1Front= True
		obj.addProperty("App::PropertyBool","Face2Bottom","Visibility on WOBJ file","Is visible on WOBJ file").Face2Bottom= True
		obj.addProperty("App::PropertyBool","Face3Top","Visibility on WOBJ file","Is visible on WOBJ file").Face3Top= True
		obj.addProperty("App::PropertyBool","Face4Rear","Visibility on WOBJ file","Is visible on WOBJ file").Face4Rear= True
		obj.addProperty("App::PropertyBool","Face5Right","Visibility on WOBJ file","Is visible on WOBJ file").Face5Right= True
		obj.addProperty("App::PropertyBool","Face6Left","Visibility on WOBJ file","Is visible on WOBJ file").Face6Left= True
		obj.addProperty("App::PropertyString","GeometryFile").GeometryFile=""
		obj.addProperty("App::PropertyString","MATERIALFILE","Material File").MATERIALFILE=""

	def onChanged(self, fp, prop):
		FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
		if prop == "Length" or prop == "Width" or prop == "Height":
			fp.Shape = Part.makeBox(fp.Length,fp.Width,fp.Height)

	def execute(self, fp):
		FreeCAD.Console.PrintMessage("Recompute Python Box feature\n")
		fp.Shape = Part.makeBox(fp.Length,fp.Width,fp.Height)

class ViewProviderBox:
	def __init__(self, obj):
		obj.Proxy = self

def makeBox():
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Box")
	Box(a)
	ViewProviderBox(a.ViewObject)


exec(makeBox())

