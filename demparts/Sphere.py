import FreeCAD, Part, math
from FreeCAD import Base
from pivy import coin
from FreeCAD import Vector
import sys
from PySide import QtGui


class PartFeature:
	def __init__(self, obj):
		obj.Proxy = self

class Sphere(PartFeature):
	def __init__(self, obj):
		PartFeature.__init__(self, obj)
		obj.addProperty("App::PropertyLength","Radius","bSphere","Radius of the sphere").Radius=1.0
		obj.addProperty("App::PropertyString","COR","Material specifications","COR of the sphere").COR=""
		obj.addProperty("App::PropertyAngle","Angle1","bSphere","Angle1").Angle1=-90
		obj.addProperty("App::PropertyAngle","Angle2","bSphere","Angle2").Angle2=90
		obj.addProperty("App::PropertyAngle","Angle3","bSphere","Angle3").Angle3=360
		obj.addProperty("App::PropertyString","Static_friction","Material specifications","Static friction of the sphere").Static_friction=""
		obj.addProperty("App::PropertyString","Kinetic_friction","Material specifications","Kinetic friction of the sphere").Kinetic_friction=""
		obj.addProperty("App::PropertyString","Contact_time","Normal parameters","Contact time for normal parameters of the sphere").Contact_time=""
		obj.addProperty("App::PropertyString","Contacttime","Tangent parameters","Contact time for tangent parameters of the sphere").Contacttime=""
		obj.addProperty("App::PropertyString","RollingDamp","Rotation parameters","Rolling Damp of the sphere").RollingDamp=""
		obj.addProperty("App::PropertyString","Density","Material specifications","Density of the sphere").Density=""
		obj.addProperty("App::PropertyString","ThermalCond","HeatParameters","Thermal condition").ThermalCond=""
		obj.addProperty("App::PropertyString","ThermalCap","HeatParameters","Thermal Capacity").ThermalCap=""
		obj.addProperty("App::PropertyString","InitTemp","HeatParameters","Initial temperature").InitTemp=""
		obj.addProperty("App::PropertyString","MATERIALFILE","Material File").MATERIALFILE=""

	def onChanged(self, fp, prop):
		FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
		if prop == "Radius" or prop == "Angle1" or prop == "Angle2" or prop == "Angle3":
			fp.Shape = Part.makeSphere(fp.Radius,Vector(0,0,0),Vector(0,0,1),fp.Angle1,fp.Angle2,fp.Angle3)

	def execute(self, fp):
		FreeCAD.Console.PrintMessage("Recompute Python Sphere feature\n")
		fp.Shape = Part.makeSphere(fp.Radius,Vector(0,0,0),Vector(0,0,1),fp.Angle1,fp.Angle2,fp.Angle3)

class ViewProviderSphere:
	def __init__(self, obj):
		obj.Proxy = self

def makeSphere():
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Sphere")
	Sphere(a)
	ViewProviderSphere(a.ViewObject)

exec(makeSphere())