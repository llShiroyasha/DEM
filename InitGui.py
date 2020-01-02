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
# ***************************************************************************/


import FreeCAD
import FreeCADGui

class DEMWorkbench(Workbench):
    "DEM Workbench Object"
    def __init__(self):
        self.__class__.Icon = FreeCAD.getResourceDir() + "Mod/DEM/Resources/icon/icon.svg"
        self.__class__.MenuText = "DEM"
        self.__class__.ToolTip = "DEM Workbench"

    def Initialize(self):
        import Script
        import CAD
        list = ["WOBJ"]
        list1 = ["Cube", "Sphere", "Rectangle", "Cylinder"]
        self.appendToolbar("Converter",list)
        self.appendToolbar("CAD",list1)



    def GetClassName(self):
        return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(DEMWorkbench())
