import FreeCAD
import FreeCADGui
from .manager import CommandManager
from PySide import QtCore

class _CommandDEMWobjConverter(CommandManager):
    "The DEM WOBJ Converter command definition"
    def __init__(self):
        super(_CommandDEMWobjConverter, self).__init__()
        self.resources = {"Pixmap": "applications-accessoiries",
                          "MenuText": QtCore.QT_TRANSLATE_NOOP("DEM_WOBJ_Converter", "WOBJ Converter"),
                          "Accel": "",
                          'ToolTip': QtCore.QT_TRANSLATE_NOOP("DEM_WOBJ_Converter", "Creates a Wobj File for Blaez-DEM")}
        self.is_active = 'with_document'
       
    def Activated(self):
        FreeCAD.ActiveDocument.openTransaction("Create WOBJConverter")
        FreeCADGui.addModule("demconverters")
        FreeCADGui.doCommand("FemGui.getActiveAnalysis().addObject(demconverters.FCStd-WOBJ2 converter(FreeCAD.ActiveDocument))")
        FreeCAD.ActiveDocument.recompute()


FreeCADGui.addCommand('WOBJ Converter',_CommandDEMWobjConverter())