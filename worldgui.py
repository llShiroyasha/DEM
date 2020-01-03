import FreeCAD, FreeCADGui

class World:
    def Activated(self):
        import demworld.WorldFileCreator as WorldFileCreator
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'', 'MenuText': 'World File Creator', 'ToolTip':'World File Creator'}
       
FreeCADGui.addCommand('World', World())


