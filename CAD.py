import FreeCAD, FreeCADGui

class Cube:
    def Activated(self):
        import demparts.cube as cube
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'Part_Box', 'MenuText': 'Box', 'ToolTip':'Make a box'}
        
class Sphere:
    def Activated(self):
        import demparts.Sphere as Sphere
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'Part_Sphere', 'MenuText': 'Sphere', 'ToolTip':'Make a sphere'}
        
class Rectangle:
    def Activated(self):
        import demparts.Rect as Rect
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'Draft_Rectangle', 'MenuText': 'Rectangle', 'ToolTip':'Make a rectangle'}
        
class Cylinder:
    def Activated(self):
        import demparts.Cylinder as Cylinder
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'Part_Cylinder', 'MenuText': 'Cylinder', 'ToolTip':'Make a cylinder'}
       
FreeCADGui.addCommand('Cube', Cube())
FreeCADGui.addCommand('Sphere', Sphere())
FreeCADGui.addCommand('Rectangle', Rectangle())
FreeCADGui.addCommand('Cylinder', Cylinder())