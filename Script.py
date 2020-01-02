import FreeCAD, FreeCADGui

class WOBJ:
    def Activated(self):
        import demconverters.FCStdWOBJ2converter as FCStdWOBJ2converter
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'', 'MenuText': 'FCStd > WOBJ converter', 'ToolTip':'FCStd to WOBJ Converter'}
       
FreeCADGui.addCommand('WOBJ', WOBJ())
