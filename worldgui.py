import FreeCAD, FreeCADGui

class World:
    def Activated(self):
        import demworld.WorldFileCreator as WorldFileCreator
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'WebWorkbench', 'MenuText': '', 'ToolTip':'World File Creator'}
       
FreeCADGui.addCommand('World', World())


