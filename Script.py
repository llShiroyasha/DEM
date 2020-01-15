import FreeCAD, FreeCADGui

class WOBJ:
    def Activated(self):
        import demconverters.FCStdWOBJ2converter as FCStdWOBJ2converter
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'E:\Programmes x86\FreeCAD 0.18\data\Mod\DEM\Resources\icon\W', 'MenuText': '', 'ToolTip':'FCStd to WOBJ Converter'}
        
        
class POBJ:
    def Activated(self):
        import demconverters.FCstdPOBJconverter as FCstdPOBJconverter
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'E:\Programmes x86\FreeCAD 0.18\data\Mod\DEM\Resources\icon\P','MenuText': '','ToolTip':'FCStd to POBJ Converter'}
        
class VOBJ:
    def Activated(self):
        import demconverters.FCstdVOBJconverter as FCstdVOBJconverter
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'E:\Programmes x86\FreeCAD 0.18\data\Mod\DEM\Resources\icon\V','MenuText': '','ToolTip':'FCStd to VOBJ Converter'}
    
        
class Material:
    def Activated(self):
        import demconverters.Materialfiles as Materialfiles
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap':'E:\Programmes x86\FreeCAD 0.18\data\Mod\DEM\Resources\icon\M','MenuText': '','ToolTip':'FCStd to VOBJ Converter'}
       
FreeCADGui.addCommand('WOBJ', WOBJ())
FreeCADGui.addCommand('POBJ', POBJ())
FreeCADGui.addCommand('VOBJ', VOBJ())
FreeCADGui.addCommand("Material",Material())