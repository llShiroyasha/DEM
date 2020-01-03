import FreeCAD, FreeCADGui

class WOBJ:
    def Activated(self):
        import demconverters.FCStdWOBJ2converter as FCStdWOBJ2converter
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'', 'MenuText': 'FCStd > WOBJ converter', 'ToolTip':'FCStd to WOBJ Converter'}
        
        
class POBJ:
    def Activated(self):
        import demconverters.FCstdPOBJconverter as FCstdPOBJconverter
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'', 'MenuText':'FCStd > VOBJ Converter','ToolTip':'FCStd to VOBJ Converter'}
       
FreeCADGui.addCommand('WOBJ', WOBJ())
FreeCADGui.addCommand('POBJ', POBJ())

