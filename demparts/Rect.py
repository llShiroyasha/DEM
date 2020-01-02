from FreeCAD import Base
import Part,FreeCAD

class ParametricRectangle:

 def __init__(self,obj):
   obj.Proxy = self
   obj.addProperty("App::PropertyFloat","Length").Length=10
   obj.addProperty("App::PropertyFloat","Width").Width=10

 def execute(self,obj):
   import Part,FreeCAD
   if (obj.Length == 0) or (obj.Width == 0):
     return
   v1 = FreeCAD.Vector(0,0,0)
   v2 = FreeCAD.Vector(obj.Length,0,0)
   v3 = FreeCAD.Vector(obj.Length,obj.Width,0)
   v4 = FreeCAD.Vector(0,obj.Width,0)
   e1 = Part.LineSegment(v1,v2).toShape()
   e2 = Part.LineSegment(v2,v3).toShape()
   e3 = Part.LineSegment(v3,v4).toShape()
   e4 = Part.LineSegment(v4,v1).toShape()
   w = Part.Wire([e1,e2,e3,e4])
   f = Part.Face(w)
   f.Placement = obj.Placement
   obj.Shape = f
   
 def onChanged(self, obj, prop):
  FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
  if prop == "Length" or prop == "Width":
    v1 = FreeCAD.Vector(0,0,0)
    v2 = FreeCAD.Vector(obj.Length,0,0)
    v3 = FreeCAD.Vector(obj.Length,obj.Width,0)
    v4 = FreeCAD.Vector(0,obj.Width,0)
    e1 = Part.LineSegment(v1,v2).toShape()
    e2 = Part.LineSegment(v2,v3).toShape()
    e3 = Part.LineSegment(v3,v4).toShape()
    e4 = Part.LineSegment(v4,v1).toShape()
    w = Part.Wire([e1,e2,e3,e4])
    f = Part.Face(w)
    f.Placement = obj.Placement
    obj.Shape = f
    FreeCAD.ActiveDocument.recompute()

def MakeRect():
    myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Rect")
    ParametricRectangle(myObj)
    myObj.ViewObject.Proxy = 0
    FreeCAD.ActiveDocument.recompute()


Maker = MakeRect()
Maker.exec_()