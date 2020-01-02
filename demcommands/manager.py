__title__ = "DEM Commands"
__author__ = "Robin PORQUET"
__url__ = "http://www.freecadweb.org"

##addtogroup DEM
import FreeCAD
import femtools.femutils as femutils
if FreeCAD.GuiUp:
    import FreeCADGui
    from PySide import QtCore

class CommandManager(object):
    def __init__(self):
        self.resources = {'Pixmap': 'DEMWorkbench',
                          'MenuText':QtCore.QT_TRANSLATE_NOOP("DEM_Command", "Default DEM Command MenuText"),
                          'Accel': "",
                          "ToolTip": QtCore.QT_TRANSLATE_NOOP("DEM_Command", "Default DEM Command ToolTip")}
        self.is_active = None
        self.selobj = None
        self.selobj2 = None
        self.active_analysis = None
        
    def GetResources(self):
        return self.resources
    
    def IsActive(self):
        pass
        
    