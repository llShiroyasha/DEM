from FreeCAD import Base
import Part,FreeCAD

class ParametricRectangle:
	def __init__(self,obj):
		obj.Proxy = self
		obj.addProperty("App::PropertyFloat","X1").X1=0
		obj.addProperty("App::PropertyFloat","Y1").Y1=0
		obj.addProperty("App::PropertyFloat","X2").X2=10
		obj.addProperty("App::PropertyFloat","Y2").Y2=0
		obj.addProperty("App::PropertyFloat","X3").X3=10
		obj.addProperty("App::PropertyFloat","Y3").Y3=10
		obj.addProperty("App::PropertyFloat","X4").X4=0
		obj.addProperty("App::PropertyFloat","Y4").Y4=10
		obj.addProperty("App::PropertyFloat","X5").X5=0
		obj.addProperty("App::PropertyFloat","Y5").Y5=20
		obj.addProperty("App::PropertyFloat","Height").Height=10
		obj.addProperty("App::PropertyString","COR","Material specifications","COR of the box").COR=""
		obj.addProperty("App::PropertyString","Static_friction","Material specifications","Static friction of the box").Static_friction=""
		obj.addProperty("App::PropertyString","Kinetic_friction","Material specifications","Kinetic friction of the box").Kinetic_friction=""
		obj.addProperty("App::PropertyString","Contact_time","Normal parameters","Contact time for normal parameters of the box").Contact_time=""
		obj.addProperty("App::PropertyString","Contacttime","Tangent parameters","Contact time for tangent parameters of the box").Contacttime=""

	def onChanged(self, obj, prop):
		FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")	
		if prop == "X1" :
			v1 = FreeCAD.Vector(obj.X1,obj.Y1,0)
			v2 = FreeCAD.Vector(obj.X2,obj.Y2,0)
			v3 = FreeCAD.Vector(obj.X3,obj.Y3,0)
			v4 = FreeCAD.Vector(obj.X4,obj.Y4,0)
			v5 = FreeCAD.Vector(obj.X5,obj.Y5,0)
			e1 = Part.LineSegment(v1,v2).toShape()
			e2 = Part.LineSegment(v2,v3).toShape()
			e3 = Part.LineSegment(v3,v4).toShape()
			e4 = Part.LineSegment(v4,v5).toShape()
			w = Part.Wire([e1,e2,e3,e4])
			f = w.extrude(Base.Vector(0,0,obj.Height))
			f.Placement = obj.Placement
			obj.Shape = f

	def execute(self,obj):
		v1 = FreeCAD.Vector(obj.X1,obj.Y1,0)
		v2 = FreeCAD.Vector(obj.X2,obj.Y2,0)
		v3 = FreeCAD.Vector(obj.X3,obj.Y3,0)
		v4 = FreeCAD.Vector(obj.X4,obj.Y4,0)
		v5 = FreeCAD.Vector(obj.X5,obj.Y5,0)
		e1 = Part.LineSegment(v1,v2).toShape()
		e2 = Part.LineSegment(v2,v3).toShape()
		e3 = Part.LineSegment(v3,v4).toShape()
		e4 = Part.LineSegment(v4,v5).toShape()
		w = Part.Wire([e1,e2,e3,e4])
		f = w.extrude(Base.Vector(0,0,obj.Height))
		f.Placement = obj.Placement
		obj.Shape = f

myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Extrude")
ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0
FreeCAD.ActiveDocument.recompute()

