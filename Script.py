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
        return {'Pixmap':'', 'MenuText':'FCStd > POBJ Converter','ToolTip':'FCStd to POBJ Converter'}
        
class VOBJ:
    def Activated(self):
        import demconverters.FCstdVOBJconverter as FCstdVOBJconverter
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'', 'MenuText':'FCStd > VOBJ Converter','ToolTip':'FCStd to VOBJ Converter'}
    
        
class Material:
    def Activated(self):
        import demconverters.Materialfiles as Materialfiles
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'', 'MenuText':'FCStd > Material', "ToolTip":"FCStd to Material files"}
       
FreeCADGui.addCommand('WOBJ', WOBJ())
FreeCADGui.addCommand('POBJ', POBJ())
FreeCADGui.addCommand('VOBJ', VOBJ())
FreeCADGui.addCommand("Material",Material())