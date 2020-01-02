from FreeCAD import Base
import Part,FreeCAD

class PartFeature():
	def __init__(self,obj):
		obj.Proxy=self

class Cylinder(PartFeature):
	def __init__(self, obj):
		PartFeature.__init__(self, obj)
		obj.addProperty("App::PropertyLength","Radius","Cylinder","Radius of the cylinder").Radius=10.0
		obj.addProperty("App::PropertyLength","Height","Cylinder", "Height of the cylinder").Height=10.0
		obj.addProperty("App::PropertyString","COR","Material specifications","COR of the box").COR=""
		obj.addProperty("App::PropertyString","Static_friction","Material specifications","Static friction of the cylinder").Static_friction=""
		obj.addProperty("App::PropertyString","Kinetic_friction","Material specifications","Kinetic friction of the cylinder").Kinetic_friction=""
		obj.addProperty("App::PropertyString","Contact_time","Normal parameters","Contact time for normal parameters of the cylinder").Contact_time=""
		obj.addProperty("App::PropertyString","Contacttime","Tangent parameters","Contact time for tangent parameters of the cylinder").Contacttime=""
		obj.addProperty("App::PropertyString","xx","Inertia tensor","Inertia tensor for xx").xx=""
		obj.addProperty("App::PropertyString","xy","Inertia tensor","Inertia tensor for xy").xy=""
		obj.addProperty("App::PropertyString","xz","Inertia tensor","Inertia tensor for xz").xz=""
		obj.addProperty("App::PropertyString","yx","Inertia tensor","Inertia tensor for yx").yx=""
		obj.addProperty("App::PropertyString","yy","Inertia tensor","Inertia tensor for yy").yy=""
		obj.addProperty("App::PropertyString","yz","Inertia tensor","Inertia tensor for yz").yz=""
		obj.addProperty("App::PropertyString","zx","Inertia tensor","Inertia tensor for zx").zx=""
		obj.addProperty("App::PropertyString","zy","Inertia tensor","Inertia tensor for zy").zy=""
		obj.addProperty("App::PropertyString","zz","Inertia tensor","Inertia tensor for zz").zz=""
		obj.addProperty("App::PropertyString","Density","Material specifications","Density of the cylinder").Density=""
		obj.addProperty("App::PropertyString","RollingDamp","Rotation parameters","Rolling Damp of the cylinder").RollingDamp=""
		obj.addProperty("App::PropertyString","ThermalCond","HeatParameters","Thermal condition").ThermalCond=""
		obj.addProperty("App::PropertyString","ThermalCap","HeatParameters","Thermal Capacity").ThermalCap=""
		obj.addProperty("App::PropertyString","InitTemp","HeatParameters","Initial temperature").InitTemp=""

	def onChanged(self, fp, prop):
		FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
		if prop == "Height":
			fp.Shape = Part.makeCylinder(fp.Radius,fp.Height)

	def execute(self, fp):
		FreeCAD.Console.PrintMessage("Recompute Python Box feature\n")
		fp.Shape = Part.makeCylinder(fp.Radius,fp.Height)

class ViewProviderCylinder:
	def __init__(self, obj):
		obj.Proxy = self

def makeCylinder():
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Cylinder")
	Cylinder(a)
	ViewProviderCylinder(a.ViewObject)

Maker = makeCylinder()
Maker.exec_()