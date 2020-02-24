# ***************************************************************************
# *   (c) Robin PORQUET (robin.porquet@gmail.com) 2019                      *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# *   Made during my internship in South Africa                             *
# *   Director of my internship: Pr. Daniel N. Wilke                        *
# *   Tutor in France: Pr. Patrick Pizette                                  *       
# *                                                                         *
# *   Robin PORQUET 2019                                                    *
# ***************************************************************************


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