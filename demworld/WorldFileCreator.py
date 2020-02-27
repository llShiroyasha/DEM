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


from PySide import QtGui, QtCore
from PySide.QtGui import QListWidget
import os

import platform
import FreeCAD, FreeCADGui

App=FreeCAD
Gui=FreeCADGui

reply2 = QtGui.QInputDialog.getText(None, "World file name","Enter the World File Name :")
filename=reply2[0]

list9=[]
list91=[]
nombre=[]
nombre1=[]
nbextrude=[]
list10=[]
name=""
listWOBJ=[]

dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
os.chdir(dir_)

class Test(QtGui.QDialog):
	def __init__(self):
		super(Test, self).__init__()
		self.initUI()
	def initUI(self):
		#Set up GUI
		# define window	xLoc,yLoc,xDim,yDim
		self.setGeometry(150, 30, 1300, 1000)
		self.setWindowTitle("World file creation")
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.label100=QtGui.QLabel("--------------------------------------------World Object File------------------------------------",self)
		self.label100.move(0,10)
		self.label1=QtGui.QLabel("Input your WOBJ", self)
		self.label1.move(50,30)
		self.label2 = QtGui.QLabel("                                                                                                                  ", self)
		self.label2.move(150, 60)
		self.label3 = QtGui.QLabel("Your WOBJ file are:",self)
		self.label3.move(50,60)
		self.Label4 = QtGui.QLabel("Speed",self)
		self.Label4.move(50,90)
		self.Label5 = QtGui.QLabel("Start Time",self)
		self.Label5.move(50,120)
		self.Label6 = QtGui.QLabel("TotalRevs",self)
		self.Label6.move(50,150)
		self.label1110 = QtGui.QLabel("About",self)
		self.label1110.move(50,180)
		self.label101=QtGui.QLabel("--------------------------------------------Particules Objects------------------------------------",self)
		self.label101.move(0,200)
		self.label7 = QtGui.QLabel("Input your POBJ files", self)
		self.label7.move(50,230)
		self.label8 = QtGui.QLabel("Your POBJ files are:",self)
		self.label8.move(50,260)
		self.label20 = QtGui.QLabel("                                                                                                                                                                                                                                                              ", self)
		self.label20.move(150, 260)
		self.label9 = QtGui.QLabel("Number of POBJ",self)
		self.label9.move(50,290)
		self.label9.hide()
		self.label102=QtGui.QLabel("--------------------------------------------Volume Objects------------------------------------",self)
		self.label102.move(0,300)
		self.label21 = QtGui.QLabel("Input your VOBJ files", self)
		self.label21.move(50,330)
		self.label22 = QtGui.QLabel("Your VOBJ files are:",self)
		self.label22.move(50,360)
		self.label23 = QtGui.QLabel("                                                                                                                                                                                                                                                              ", self)
		self.label23.move(150,360)
		self.label24 = QtGui.QLabel("Attached to",self)
		self.label24.move(50,390)
		self.label24.hide()
		self.label25 = QtGui.QLabel("Repeat",self)
		self.label25.move(50,400)
		self.label25.hide()
		self.label26 = QtGui.QLabel("Type",self)
		self.label26.move(50,430)
		self.label26.hide()
		self.label27 = QtGui.QLabel("Start angle",self)
		self.label27.move(50,460)
		self.label27.hide()
		self.label28 = QtGui.QLabel("End angle",self)
		self.label28.move(50,490)
		self.label28.hide()
		self.label30 = QtGui.QLabel("-----------------------------------------Simulation Setup------------------------------------",self)
		self.label30.move(0,490)
		self.label31 = QtGui.QLabel("Total Time",self)
		self.label31.move(50,520)
		self.label32 = QtGui.QLabel("Force field (cm/s)",self)
		self.label32.move(50,550)
		self.label33 = QtGui.QLabel("Particles rotation",self)
		self.label33.move(50,580)
		self.label34 = QtGui.QLabel("Velocity limit",self)
		self.label34.move(50,610)
		self.label35 = QtGui.QLabel("Valid Zone",self)
		self.label35.move(50,640)
		self.label36 = QtGui.QLabel("true",self)
		self.label36.move(210,605)
		self.label36.hide()
		self.label37 = QtGui.QLabel("true",self)
		self.label37.move(210,635)
		self.label37.hide()
		self.label38 = QtGui.QLabel("true",self)
		self.label38.move(210,665)
		self.label38.hide()
		self.label39 = QtGui.QLabel("-----------------------------------------Broad Phase------------------------------------",self)
		self.label39.move(0,690)
		self.label40 = QtGui.QLabel("Grid per size",self)
		self.label40.move(50,720)
		self.label41 = QtGui.QLabel("Over ride",self)
		self.label41.move(50,750)
		self.label42 = QtGui.QLabel("Origin",self)
		self.label42.move(50,780)
		self.label43 = QtGui.QLabel("WorldSize",self)
		self.label43.move(50,810)
		self.label44 = QtGui.QLabel("Cell Size", self)
		self.label44.move(50,840)
		self.label45 = QtGui.QLabel("true",self)
		self.label45.move(210,720)
		self.label45.hide()
		self.label46 = QtGui.QLabel("true",self)
		self.label46.move(210,750)
		self.label46.hide()
		self.label47 = QtGui.QLabel("-----------------------------------------Initialisation Particle setup------------------------------------",self)
		self.label47.move(400,10)
		self.label48 = QtGui.QLabel("ReadFromFile",self)
		self.label48.move(420,40)
		self.label49 = QtGui.QLabel("StartType",self)
		self.label49.move(420,70)
		#self.label49.hide()
		self.label50 = QtGui.QLabel("Random Orient",self)
		self.label50.move(420,100)
		#self.label50.hide()
		self.label51 = QtGui.QLabel("Random Start Velocity",self)
		self.label51.move(420,130)
		#self.label51.hide()
		self.label52 = QtGui.QLabel("Launch Velocity (cm/s)", self)
		self.label52.move(420,160)
		#self.label52.hide()
		self.label53 = QtGui.QLabel("Launch A Velocity",self)
		self.label53.move(420,190)
		#self.label53.hide()
		self.label54 = QtGui.QLabel("Spawn Start",self)
		self.label54.move(420,220)
		#self.label54.hide()
		self.label55 = QtGui.QLabel("Spawn End",self)
		self.label55.move(420,250)
		self.label56 = QtGui.QLabel("false",self)
		self.label56.move(550,40)
		self.label56.hide()
		self.label57 = QtGui.QLabel("true",self)
		self.label57.move(550,100)
		self.label57.hide()
		self.label58 = QtGui.QLabel("true",self)
		self.label58.move(550,130)
		self.label58.hide()
		self.label59 = QtGui.QLabel("-----------------------------------------Output Options------------------------------------",self)
		self.label59.move(390,280)
		self.label60 = QtGui.QLabel("Display",self)
		self.label60.move(420,310)
		self.label61 = QtGui.QLabel("View",self)
		self.label61.move(420,340)
		self.label62 = QtGui.QLabel("Cut",self)
		self.label62.move(420,370)
		self.label63 = QtGui.QLabel("FPS",self)
		self.label63.move(420,400)
		self.label64 = QtGui.QLabel("GLDebug", self)
		self.label64.move(420,430)
		self.label65 = QtGui.QLabel("File Write",self)
		self.label65.move(420,460)
		self.label66 = QtGui.QLabel("Snapshot Write",self)
		self.label66.move(420,490)
		self.label67 = QtGui.QLabel("Energy diss",self)
		self.label67.move(420,520)
		self.label68 = QtGui.QLabel("Spectra",self)
		self.label68.move(420,550)
		self.label69 = QtGui.QLabel("Contact Info",self)
		self.label69.move(420,580)
		self.label70 = QtGui.QLabel("VolCellInfo",self)
		self.label70.move(420,610)
		self.label71 = QtGui.QLabel("(0=type,1=vel(binsize),2=pen(binsize))",self)
		self.label71.move(420,320)
		self.label72 = QtGui.QLabel("Type", self)
		self.label72.move(630,310)
		self.label73 = QtGui.QLabel("true",self)
		self.label73.move(580,310)
		self.label74 = QtGui.QLabel("Bin", self)
		self.label74.move(720,310)
		self.label75 = QtGui.QLabel("true",self)
		self.label75.move(580,370)
		self.label76 = QtGui.QLabel("true",self)
		self.label76.move(580,460)
		self.label77 = QtGui.QLabel("true",self)
		self.label77.move(580,490)
		self.label78 = QtGui.QLabel("true",self)
		self.label78.move(580,520)
		self.label79 = QtGui.QLabel("Type",self)
		self.label79.move(630,370)
		self.label80 = QtGui.QLabel("Freq",self)
		self.label80.move(720,370)
		self.label81 = QtGui.QLabel("true",self)
		self.label81.move(580,550)
		self.label82 = QtGui.QLabel("true",self)
		self.label82.move(580,580)
		self.label83 = QtGui.QLabel("true",self)
		self.label83.move(580,610)
		self.label130 = QtGui.QLabel("Freq",self)
		self.label130.move(630,460)
		self.label131 = QtGui.QLabel("Detail",self)
		self.label131.move(720,460)
		self.label132 = QtGui.QLabel("Freq",self)
		self.label132.move(630,490)
		self.label133 = QtGui.QLabel("ColorType",self)
		self.label133.move(720,490)

		self.label84 = QtGui.QLabel("-----------------------------------------Tallies----------------------------------------",self)
		self.label84.move(390,640)
		self.label85 = QtGui.QLabel("Number of tallies",self)
		self.label85.move(390,670)

		self.label86 = QtGui.QLabel("-----------------------------------------Color setting------------------------------------",self)
		self.label86.move(390,700)
		self.label87 = QtGui.QLabel("Custom Color",self)
		self.label87.move(390,730)
		self.label88 = QtGui.QLabel("Manual Layer Colors",self)
		self.label88.move(390,760)
		self.label89 = QtGui.QLabel("true",self)
		self.label89.move(580,730)
		self.label90 = QtGui.QLabel("true",self)
		self.label90.move(580,760)
		self.label91 = QtGui.QLabel("Type", self)
		self.label91.move(390,790)
		self.label92 = QtGui.QLabel("Layer Width", self)
		self.label92.move(390,820)
		self.label93 = QtGui.QLabel("Direction", self)
		self.label93.move(390,850)
		self.label2000 = QtGui.QLabel("NumColor", self)
		self.label2000.move(610,730)

		self.label95 = QtGui.QLabel("------------------------------------------------------------------------------------------",self)
		self.label95.move(390,864)
		self.label94 = QtGui.QLabel("LOADPROFILE",self)
		self.label94.move(390,880)

		self.label200 = QtGui.QLabel("--------------------------------Begin Modelisation-----------------------------------------",self)
		self.label200.move(800,10)
		self.label201 = QtGui.QLabel("Normal Contact Model", self)
		self.label201.move(800,40)
		self.label202 = QtGui.QLabel("Tangent Contact Model", self)
		self.label202.move(800,70)
		self.label203 = QtGui.QLabel("Rolling Contact Model", self)
		self.label203.move(800,100)
		self.label204 = QtGui.QLabel("Cohesion Contact Model", self)
		self.label204.move(800,130)
		self.label205 = QtGui.QLabel("Particle Type", self)
		self.label205.move(800,160)
		self.label206 = QtGui.QLabel("Time Step",self)
		self.label206.move(800,190)
		self.NCM = QtGui.QLineEdit(self)
		self.NCM.setText("None")
		self.NCM.setFixedWidth(100)
		self.NCM.move(950,35)
		self.TCM = QtGui.QLineEdit(self)
		self.TCM.setText("None")
		self.TCM.setFixedWidth(100)
		self.TCM.move(950,65)
		self.RCM = QtGui.QLineEdit(self)
		self.RCM.setText("None")
		self.RCM.setFixedWidth(100)
		self.RCM.move(950,95)
		self.CCM = QtGui.QLineEdit(self)
		self.CCM.setText("None")
		self.CCM.setFixedWidth(100)
		self.CCM.move(950,125)
		self.ParticleType = QtGui.QLineEdit(self)
		self.ParticleType.setText("None")
		self.ParticleType.setFixedWidth(100)
		self.ParticleType.move(950,155)
		self.TimeStep = QtGui.QLineEdit(self)
		self.TimeStep.setText("0.0")
		self.TimeStep.setFixedWidth(100)
		self.TimeStep.move(950,185)
		self.label1207= QtGui.QLabel("-----------------------------------------------------------Fluid Coupling-------------------------------------------------",self)
		self.label1207.move(750,280)
		self.label1208 = QtGui.QLabel("FluidCoupling?",self)
		self.label1208.move(800,310)
		self.label1209 = QtGui.QLabel("True", self)
		self.label1209.move(390,790)
		self.label1209.hide()

		#Text Inputs
		self.SpeedI = QtGui.QLineEdit(self)
		self.SpeedI.setText("0.0")
		self.SpeedI.setFixedWidth(90)
		self.SpeedI.move(210, 85)
		self.Aboutx = QtGui.QLineEdit(self)
		self.Aboutx.setText("0.0")
		self.Aboutx.setFixedWidth(40)
		self.Aboutx.move(160,175)
		self.Abouty = QtGui.QLineEdit(self)
		self.Abouty.setText("0.0")
		self.Abouty.setFixedWidth(40)
		self.Abouty.move(210,175)
		self.Aboutz = QtGui.QLineEdit(self)
		self.Aboutz.setText("0.0")
		self.Aboutz.setFixedWidth(40)
		self.Aboutz.move(260,175)
		self.StartT = QtGui.QLineEdit(self)
		self.StartT.setText("0.0")
		self.StartT.setFixedWidth(90)
		self.StartT.move(210, 115)
		self.TotalR = QtGui.QLineEdit(self)
		self.TotalR.setText("0")
		self.TotalR.setFixedWidth(90)
		self.TotalR.move(210,145)
		self.Num = QtGui.QLineEdit(self)
		self.Num.setText("0")
		self.Num.setFixedWidth(90)
		self.Num.move(210,255)
		self.Num.hide()
		self.AttachedT = QtGui.QLineEdit(self)
		self.AttachedT.setText("0")
		self.AttachedT.setFixedWidth(90)
		self.AttachedT.move(210,365)
		self.AttachedT.hide()
		self.Repeat1 = QtGui.QLineEdit(self)
		self.Repeat1.setText("0")
		self.Repeat1.setFixedWidth(90)
		self.Repeat1.move(210,395)
		self.Repeat1.hide()
		self.Type1 =  QtGui.QLineEdit(self)
		self.Type1.setText("0")
		self.Type1.setFixedWidth(90)
		self.Type1.move(210,425)
		self.Type1.hide()
		self.StartA = QtGui.QLineEdit(self)
		self.StartA.setText("0")
		self.StartA.setFixedWidth(90)
		self.StartA.move(210,455)
		self.StartA.hide()
		self.EndA = QtGui.QLineEdit(self)
		self.EndA.setText("360")
		self.EndA.setFixedWidth(90)
		self.EndA.move(210,485)
		self.EndA.hide()

		self.TotalT = QtGui.QLineEdit(self)
		self.TotalT.setText("0.0")
		self.TotalT.setFixedWidth(90)
		self.TotalT.move(210, 515)
		self.ForceFx = QtGui.QLineEdit(self)
		self.ForceFx.setText("0.0")
		self.ForceFx.setFixedWidth(40)
		self.ForceFx.move(160, 545)
		self.ForceFy = QtGui.QLineEdit(self)
		self.ForceFy.setText("0.0")
		self.ForceFy.setFixedWidth(40)
		self.ForceFy.move(210, 545)
		self.ForceFz = QtGui.QLineEdit(self)
		self.ForceFz.setText("0.0")
		self.ForceFz.setFixedWidth(40)
		self.ForceFz.move(260, 545)
		self.n1 = QtGui.QLineEdit(self)
		self.n1.setFixedWidth(40)
		self.n1.setText("0.0")
		self.n1.move(50,665)
		self.n2 = QtGui.QLineEdit(self)
		self.n2.setFixedWidth(40)
		self.n2.setText("0.0")
		self.n2.move(100,665)
		self.n3 = QtGui.QLineEdit(self)
		self.n3.setFixedWidth(40)
		self.n3.setText("0.0")
		self.n3.move(150,665)
		self.n4 = QtGui.QLineEdit(self)
		self.n4.setFixedWidth(40)
		self.n4.setText("0.0")
		self.n4.move(200,665)
		self.n5 = QtGui.QLineEdit(self)
		self.n5.setFixedWidth(40)
		self.n5.setText("0.0")
		self.n5.move(250,665)
		self.n6 = QtGui.QLineEdit(self)
		self.n6.setFixedWidth(40)
		self.n6.setText("0.0")
		self.n6.move(300,665)

		self.Originx = QtGui.QLineEdit(self)
		self.Originx.setText("0.0")
		self.Originx.setFixedWidth(40)
		self.Originx.move(160, 775)
		self.Originy = QtGui.QLineEdit(self)
		self.Originy.setText("0.0")
		self.Originy.setFixedWidth(40)
		self.Originy.move(210, 775)
		self.Originz = QtGui.QLineEdit(self)
		self.Originz.setText("0.0")
		self.Originz.setFixedWidth(40)
		self.Originz.move(260, 775)
		self.WorldSx = QtGui.QLineEdit(self)
		self.WorldSx.setText("0.0")
		self.WorldSx.setFixedWidth(40)
		self.WorldSx.move(160, 805)
		self.WorldSy = QtGui.QLineEdit(self)
		self.WorldSy.setText("0.0")
		self.WorldSy.setFixedWidth(40)
		self.WorldSy.move(210, 805)
		self.WorldSz = QtGui.QLineEdit(self)
		self.WorldSz.setText("0.0")
		self.WorldSz.setFixedWidth(40)
		self.WorldSz.move(260, 805)
		self.CellSix = QtGui.QLineEdit(self)
		self.CellSix.setText("0.0")
		self.CellSix.setFixedWidth(40)
		self.CellSix.move(160, 835)
		self.CellSiy = QtGui.QLineEdit(self)
		self.CellSiy.setText("0.0")
		self.CellSiy.setFixedWidth(40)
		self.CellSiy.move(210, 835)
		self.CellSiz = QtGui.QLineEdit(self)
		self.CellSiz.setText("0.0")
		self.CellSiz.setFixedWidth(40)
		self.CellSiz.move(260, 835)

		self.StartT = QtGui.QLineEdit(self)
		self.StartT.setText("0")
		self.StartT.setFixedWidth(90)
		self.StartT.move(550, 65)
		self.LaunchVx = QtGui.QLineEdit(self)
		self.LaunchVx.setText("0.0")
		self.LaunchVx.setFixedWidth(40)
		self.LaunchVx.move(550, 155)
		self.LaunchVy = QtGui.QLineEdit(self)
		self.LaunchVy.setText("0.0")
		self.LaunchVy.setFixedWidth(40)
		self.LaunchVy.move(600, 155)
		self.LaunchVz = QtGui.QLineEdit(self)
		self.LaunchVz.setText("0.0")
		self.LaunchVz.setFixedWidth(40)
		self.LaunchVz.move(650,155)
		self.LaunchAVx = QtGui.QLineEdit(self)
		self.LaunchAVx.setText("0.0")
		self.LaunchAVx.setFixedWidth(40)
		self.LaunchAVx.move(550, 185)
		self.LaunchAVy = QtGui.QLineEdit(self)
		self.LaunchAVy.setText("0.0")
		self.LaunchAVy.setFixedWidth(40)
		self.LaunchAVy.move(600, 185)
		self.LaunchAVz = QtGui.QLineEdit(self)
		self.LaunchAVz.setText("0.0")
		self.LaunchAVz.setFixedWidth(40)
		self.LaunchAVz.move(650, 185)
		self.SpawnSx = QtGui.QLineEdit(self)
		self.SpawnSx.setText("0.0")
		self.SpawnSx.setFixedWidth(40)
		self.SpawnSx.move(550, 215)
		self.SpawnSy = QtGui.QLineEdit(self)
		self.SpawnSy.setText("0.0")
		self.SpawnSy.setFixedWidth(40)
		self.SpawnSy.move(600, 215)
		self.SpawnSz = QtGui.QLineEdit(self)
		self.SpawnSz.setText("0.0")
		self.SpawnSz.setFixedWidth(40)
		self.SpawnSz.move(650, 215)
		self.SpawnEx = QtGui.QLineEdit(self)
		self.SpawnEx.setText("0.0")
		self.SpawnEx.setFixedWidth(40)
		self.SpawnEx.move(550, 245)
		self.SpawnEy = QtGui.QLineEdit(self)
		self.SpawnEy.setText("0.0")
		self.SpawnEy.setFixedWidth(40)
		self.SpawnEy.move(600, 245)
		self.SpawnEz = QtGui.QLineEdit(self)
		self.SpawnEz.setText("0.0")
		self.SpawnEz.setFixedWidth(40)
		self.SpawnEz.move(650, 245)

		self.Type1 = QtGui.QLineEdit(self)
		self.Type1.setText("0")
		self.Type1.setFixedWidth(40)
		self.Type1.move(670, 305)
		self.Bin = QtGui.QLineEdit(self)
		self.Bin.setText("0.0")
		self.Bin.setFixedWidth(40)
		self.Bin.move(750,305)
		self.View = QtGui.QLineEdit(self)
		self.View.setText("0")
		self.View.setFixedWidth(40)
		self.View.move(550, 335)
		self.FPS = QtGui.QLineEdit(self)
		self.FPS.setText("100")
		self.FPS.setFixedWidth(40)
		self.FPS.move(550,395)
		self.GLDebug = QtGui.QLineEdit(self)
		self.GLDebug.setText("0.0")
		self.GLDebug.setFixedWidth(40)
		self.GLDebug.move(550, 425)
		self.Type2 = QtGui.QLineEdit(self)
		self.Type2.setText("0")
		self.Type2.setFixedWidth(40)
		self.Type2.move(670, 365)
		self.Freq = QtGui.QLineEdit(self)
		self.Freq.setText("0.0")
		self.Freq.setFixedWidth(40)
		self.Freq.move(750,365)
		self.Freq2 = QtGui.QLineEdit(self)
		self.Freq2.setText("0.0")
		self.Freq2.setFixedWidth(40)
		self.Freq2.move(670,455)
		self.Detail1 = QtGui.QLineEdit(self)
		self.Detail1.setText("0.0")
		self.Detail1.setFixedWidth(40)
		self.Detail1.move(780,455)
		self.Freq3 = QtGui.QLineEdit(self)
		self.Freq3.setText("0.0")
		self.Freq3.setFixedWidth(40)
		self.Freq3.move(670,485)
		self.ColorT1 = QtGui.QLineEdit(self)
		self.ColorT1.setText("0.0")
		self.ColorT1.setFixedWidth(40)
		self.ColorT1.move(780,485)

		self.Type3 = QtGui.QLineEdit(self)
		self.Type3.setText("0")
		self.Type3.setFixedWidth(40)
		self.Type3.move(550, 665)

		self.Type4 = QtGui.QLineEdit(self)
		self.Type4.setText("0")
		self.Type4.setFixedWidth(40)
		self.Type4.move(550,785)
		self.LayerWidth = QtGui.QLineEdit(self)
		self.LayerWidth.setText("0")
		self.LayerWidth.setFixedWidth(40)
		self.LayerWidth.move(550,815)
		self.Directionx = QtGui.QLineEdit(self)
		self.Directionx.setText("0")
		self.Directionx.setFixedWidth(40)
		self.Directionx.move(550,845)
		self.Directiony = QtGui.QLineEdit(self)
		self.Directiony.setText("0")
		self.Directiony.setFixedWidth(40)
		self.Directiony.move(600,845)
		self.Directionz = QtGui.QLineEdit(self)
		self.Directionz.setText("0")
		self.Directionz.setFixedWidth(40)
		self.Directionz.move(650,845)

		self.LoadProfile = QtGui.QLineEdit(self)
		self.LoadProfile.setText("None")
		self.LoadProfile.setFixedWidth(100)
		self.LoadProfile.move(550,875)
		self.NumColor = QtGui.QLineEdit(self)
		self.NumColor.setText("0")
		self.NumColor.setFixedWidth(40)
		self.NumColor.move(660,725)

		#true or false
		listTF=["true","false"]
		self.popupItems4 = listTF

		#Set up pup up
		self.popup4 = QtGui.QComboBox(self)
		self.popup4.addItems(self.popupItems4)
		self.popup4.activated[str].connect(self.onPopup4)
		self.popup4.move(210,575)

		self.popup5 = QtGui.QComboBox(self)
		self.popup5.addItems(self.popupItems4)
		self.popup5.activated[str].connect(self.onPopup5)
		self.popup5.move(210,605)

		self.popup6 = QtGui.QComboBox(self)
		self.popup6.addItems(self.popupItems4)
		self.popup6.activated[str].connect(self.onPopup6)
		self.popup6.activated[str].connect(self.Vis9)
		self.popup6.move(210,635)

		# set up lists for pop-ups
		if App.ActiveDocument.Name == "Unnamed":
			ap=App.ActiveDocument.Name
			exec("""a1=App.getDocument("{}").getObject("Box")""".format(ap),globals())
		elif App.ActiveDocument.Name == "Sans_nom":
			ap=App.ActiveDocument.Name
			exec("""a1=App.getDocument("{}").getObject("Box")""".format(ap),globals())

		if App.ActiveDocument.Name == "Unnamed":
			ap=App.ActiveDocument.Name
			exec("""b1=App.getDocument("{}").getObject("Sphere")""".format(ap),globals())
		elif App.ActiveDocument.Name == "Sans_nom":
			ap=App.ActiveDocument.Name
			exec("""b1=App.getDocument("{}").getObject("Sphere")""".format(ap),globals())

		if App.ActiveDocument.Name == "Unnamed":
			ap=App.ActiveDocument.Name
			exec("""c1=App.getDocument("{}").getObject("Rect")""".format(ap),globals())
		elif App.ActiveDocument.Name == "Sans_nom":
			ap=App.ActiveDocument.Name
			exec("""c1=App.getDocument("{}").getObject("Rect")""".format(ap),globals())

		if App.ActiveDocument.Name == "Unnamed":
			ap=App.ActiveDocument.Name
			exec("""d1=App.getDocument("{}").getObject("Cylinder")""".format(ap),globals())
		elif App.ActiveDocument.Name == "Sans_nom":
			ap=App.ActiveDocument.Name
			exec("""d1=App.getDocument("{}").getObject("Cylinder")""".format(ap),globals())

		list=[]
		if a1==None:
			print("Box doesn't exist")
		elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Box")) == True:
			list.append(FreeCAD.ActiveDocument.Box.Label)
		j=0
		for j in range (0,100):
			n=str(j)
			ldic=locals()
			if j<10 and App.getDocument(ap).getObject("Box00"+n) == None:
				pass
			elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box00"+n)) == True:
				exec("list.append(FreeCAD.ActiveDocument.Box00{}.Label)".format(n),globals(),ldic)

			if j>10 and App.getDocument(ap).getObject("Box0"+n)==None:
				pass
			elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box0"+n)) == True:
				exec("list.append(FreeCAD.ActiveDocument.Box0{}.Label)".format(n),globals(),ldic)

		if b1==None:
			print("Sphere doesn't exist")
		elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere"))==True:
			list.append(FreeCAD.ActiveDocument.Sphere.Label)
		j=0
		for j in range (0,100):
			n=str(j)
			ldic=locals()
			if j<10 and App.getDocument(ap).getObject("Sphere00"+n)==None:
				pass
			elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere00"+n)) == True:
				exec("list.append(FreeCAD.ActiveDocument.Sphere00{}.Label)".format(n),globals(),ldic)

			if j>10 and App.getDocument(ap).getObject("Sphere0"+n)==None:
				pass
			elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere0"+n)) == True:
				exec("list.append(FreeCAD.ActiveDocument.Sphere0{}.Label)".format(n),globals(),ldic)

		if d1==None:
			print("Cynlinder doesn't exist")
		elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder"))==True:
			list.append(FreeCAD.ActiveDocument.Cylinder.Label)
		j=0
		for j in range (0,100):
			n=str(j)
			ldic=locals()
			if j<10 and App.getDocument(ap).getObject("Cylinder00"+n)==None:
				pass
			elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder00"+n)) == True:
				exec("list.append(FreeCAD.ActiveDocument.Cylinder00{}.Label)".format(n),globals(),ldic)

			if j>10 and App.getDocument(ap).getObject("Cylinder0"+n)==None:
				pass
			elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Cylinder0"+n)) == True:
				exec("list.append(FreeCAD.ActiveDocument.Cylinder0{}.Label)".format(n),globals(),ldic)

		if c1==None:
			print("Rect doesn't exist")
		elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Rect"))==True:
			list.append(FreeCAD.ActiveDocument.Rect.Label)
		j=0
		for j in range (0,100):
			n=str(j)
			ldic=locals()
			if j<10 and App.getDocument(ap).getObject("Rect00"+n)==None:
				pass
			elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Rect00"+n)) == True:
				exec("list.append(FreeCAD.ActiveDocument.Rect00{}.Label)".format(n),globals(),ldic)

			if j>10 and App.getDocument(ap).getObject("Rect0"+n)==None:
				pass
			elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Rect0"+n)) == True:
				exec("list.append(FreeCAD.ActiveDocument.Rect0{}.Label)".format(n),globals(),ldic)

		self.popupItems1 = list

		#List POBJ
		list1=[]
		if a1==None:
			print("Box doesn't exist")
		elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Box")) == True:
			list1.append(FreeCAD.ActiveDocument.Box.Label)
		j=0
		for j in range (0,100):
			n=str(j)
			ldic=locals()
			if j<10 and App.getDocument(ap).getObject("Box00"+n)==None:
				pass
			elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box00"+n)) == True:
				exec("list1.append(FreeCAD.ActiveDocument.Box00{}.Label)".format(n),globals(),ldic)

			if j>10 and App.getDocument(ap).getObject("Box0"+n)==None:
				pass
			elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Box0"+n)) == True:
				exec("list1.append(FreeCAD.ActiveDocument.Box0{}.Label)".format(n),globals(),ldic)

		if b1==None:
			print("Sphere doesn't exist")
		elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere"))==True:
			list1.append(FreeCAD.ActiveDocument.Sphere.Label)
		j=0
		for j in range (0,100):
			n=str(j)
			ldic=locals()
			if j<10 and App.getDocument(ap).getObject("Sphere00"+n)==None:
				pass
			elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere00"+n)) == True:
				exec("list1.append(FreeCAD.ActiveDocument.Sphere00{}.Label)".format(n),globals(),ldic)

			if j>10 and App.getDocument(ap).getObject("Sphere0"+n)==None:
				pass
			elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Sphere0"+n)) == True:
				exec("list1.append(FreeCAD.ActiveDocument.Sphere0{}.Label)".format(n),globals(),ldic)

		self.popupItems2 = list1

		#List VOBJ
		list2=[]
		if App.ActiveDocument.Name == "Unnamed":
			ap=App.ActiveDocument.Name
			exec("""e1=App.getDocument("{}").getObject("Extrude")""".format(ap),globals())
		elif App.ActiveDocument.Name == "Sans_nom":
			ap=App.ActiveDocument.Name
			exec("""e1=App.getDocument("{}").getObject("Extrude")""".format(ap),globals())

		if e1==None:
			pass
		elif Gui.Selection.isSelected(App.getDocument(ap).getObject("Extrude"))==True:
			list2.append(FreeCAD.ActiveDocument.Extrude.Label)
		j=0
		for j in range (0,100):
			n=str(j)
			ldic=locals()
			if j<10 and App.getDocument(ap).getObject("Extrude00"+n)==None:
				pass
			elif j<10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Extrude00"+n))==True:
				exec("list2.append(FreeCAD.ActiveDocument.Extrude00{}.Label)".format(n),globals(),ldic)

			if j>10 and App.getDocument(ap).getObject("Extrude0"+n)==None:
				pass
			elif j>10 and Gui.Selection.isSelected(App.getDocument(ap).getObject("Extrude0"+n))==True:
				exec("list2.append(FreeCAD.ActiveDocument.Extrude0{}.Label)".format(n),globals(),ldic)

		self.popupItems3 = list2

		#Cancel button
		cancelButton = QtGui.QPushButton('Cancel', self)
		cancelButton.clicked.connect(self.onCancel)
		cancelButton.setAutoDefault(True)
		cancelButton.move(500, 950)

		# OK button
		okButton = QtGui.QPushButton('OK', self)
		okButton.clicked.connect(self.onOk)
		okButton.clicked.connect(self.OpenFile)
		okButton.move(600, 950)

		#Reset button
		resetButton = QtGui.QPushButton("Reset WOBJ", self)
		resetButton.clicked.connect(self.onReset1)
		resetButton.move(300 , 25)

		# set up pop-up menu
		self.popup1 = QtGui.QComboBox(self)
		self.popup1.addItems(self.popupItems1)
		self.popup1.activated[str].connect(self.onPopup1)
		self.popup1.move(210,25)

		self.popup2 = QtGui.QComboBox(self)
		self.popup2.addItems(self.popupItems2)
		self.popup2.activated[str].connect(self.onPopup2)
		self.popup2.move(210,225)

		self.popup3 = QtGui.QComboBox(self)
		self.popup3.addItems(self.popupItems3)
		self.popup3.activated[str].connect(self.onPopup3)
		self.popup3.move(210,325)

		self.popup7 = QtGui.QComboBox(self)
		self.popup7.addItems(self.popupItems4)
		self.popup7.activated[str].connect(self.onPopup7)
		self.popup7.move(210,715)

		self.popup8 = QtGui.QComboBox(self)
		self.popup8.addItems(self.popupItems4)
		self.popup8.activated[str].connect(self.Vis8)
		self.popup8.activated[str].connect(self.onPopup8)
		self.popup8.move(210,745)

		self.popup9 = QtGui.QComboBox(self)
		self.popup9.addItems(self.popupItems4)
		self.popup9.setCurrentIndex(self.popupItems4.index("false"))
		self.popup9.activated[str].connect(self.Vis1)
		self.popup9.activated[str].connect(self.onPopup9)
		self.popup9.move(550,35)

		self.popup10 = QtGui.QComboBox(self)
		self.popup10.addItems(self.popupItems4)
		self.popup10.activated[str].connect(self.onPopup10)
		self.popup10.move(550,95)

		self.popup11 = QtGui.QComboBox(self)
		self.popup11.addItems(self.popupItems4)
		self.popup11.activated[str].connect(self.onPopup11)
		self.popup11.move(550,125)

		self.popup12 = QtGui.QComboBox(self)
		self.popup12.addItems(self.popupItems4)
		self.popup12.activated[str].connect(self.Vis3)
		self.popup12.activated[str].connect(self.onPopup12)
		self.popup12.move(550,305)

		self.popup13 = QtGui.QComboBox(self)
		self.popup13.addItems(self.popupItems4)
		self.popup13.activated[str].connect(self.onPopup13)
		self.popup13.activated[str].connect(self.Vis4)
		self.popup13.move(550,365)

		self.popup14= QtGui.QComboBox(self)
		self.popup14.addItems(self.popupItems4)
		self.popup14.activated[str].connect(self.Vis5)
		self.popup14.activated[str].connect(self.onPopup14)
		self.popup14.move(550,455)

		self.popup15 = QtGui.QComboBox(self)
		self.popup15.addItems(self.popupItems4)
		self.popup15.activated[str].connect(self.Vis6)
		self.popup15.activated[str].connect(self.onPopup15)
		self.popup15.move(550,485)

		self.popup16 = QtGui.QComboBox(self)
		self.popup16.addItems(self.popupItems4)
		self.popup16.activated[str].connect(self.onPopup16)
		self.popup16.move(550,515)

		self.popup17 = QtGui.QComboBox(self)
		self.popup17.addItems(self.popupItems4)
		self.popup17.activated[str].connect(self.onPopup17)
		self.popup17.move(550,545)

		self.popup18 = QtGui.QComboBox(self)
		self.popup18.addItems(self.popupItems4)
		self.popup18.activated[str].connect(self.onPopup18)
		self.popup18.move(550,575)

		self.popup19 = QtGui.QComboBox(self)
		self.popup19.addItems(self.popupItems4)
		self.popup19.activated[str].connect(self.onPopup19)
		self.popup19.move(550,605)

		self.popup20 = QtGui.QComboBox(self)
		self.popup20.addItems(self.popupItems4)
		self.popup20.activated[str].connect(self.Vis7)
		self.popup20.activated[str].connect(self.onPopup20)
		self.popup20.move(550,725)

		self.popup21 = QtGui.QComboBox(self)
		self.popup21.addItems(self.popupItems4)
		self.popup21.setCurrentIndex(self.popupItems4.index("true"))
		self.popup21.activated[str].connect(self.Vis2)
		self.popup21.activated[str].connect(self.onPopup21)
		self.popup21.move(550,755)

		self.popup22 = QtGui.QComboBox(self)
		self.popup22.addItems(self.popupItems4)
		self.popup22.activated[str].connect(self.onPopup22)
		self.popup22.move(900,305)


	def onPopup1(self, selectedText):
		if self.label2.text().isspace():
			self.label2.setText(selectedText)
			listWOBJ.append(selectedText)
		else:
			self.label2.setText(self.label2.text()+","+selectedText)
			listWOBJ.append(selectedText)

	def onPopup2(self, selectedText):
		if self.label20.text().isspace():
			self.label20.setText(selectedText)
			list9.append(selectedText)
		else:
			self.label20.setText(self.label20.text()+","+selectedText)
			list9.append(selectedText)

	def onPopup3(self, selectedText):
		if self.label23.text().isspace():
			self.label23.setText(selectedText)
			nbextrude.append(selectedText)
		else:
			self.label23.setText(self.label23.text()+","+selectedText)
			nbextrude.append(selectedText)

	def onPopup4(self,selectedText):
		self.label36.setText(selectedText)

	def onPopup5(self,selectedText):
		self.label37.setText(selectedText)

	def onPopup6(self,selectedText):
		self.label38.setText(selectedText)

	def onPopup7(self,selectedText):
		self.label45.setText(selectedText)

	def onPopup8(self,selectedText):
		self.label46.setText(selectedText)

	def onPopup9(self,selectedText):
		self.label56.setText(selectedText)

	def onPopup10(self,selectedText):
		self.label57.setText(selectedText)

	def onPopup11(self,selectedText):
		self.label58.setText(selectedText)

	def onPopup12(self,selectedText):
		self.label73.setText(selectedText)

	def onPopup13(self,selectedText):
		self.label75.setText(selectedText)

	def onPopup14(self,selectedText):
		self.label76.setText(selectedText)

	def onPopup15(self,selectedText):
		self.label77.setText(selectedText)

	def onPopup16(self,selectedText):
		self.label78.setText(selectedText)

	def onPopup17(self,selectedText):
		self.label81.setText(selectedText)

	def onPopup18(self,selectedText):
		self.label82.setText(selectedText)

	def onPopup19(self,selectedText):
		self.label83.setText(selectedText)

	def onPopup20(self,selectedText):
		self.label89.setText(selectedText)

	def onPopup21(self,selectedText):
		self.label90.setText(selectedText)

	def onPopup22(self,selectedText):
		self.label1209.setText(selectedText)

	def Vis1(self):
		if self.popup9.currentText()=="false":
			self.label49.show()
			self.label50.show()
			self.label51.show()
			self.label52.show()
			self.label53.show()
			self.label54.show()
			self.label55.show()
			self.label56.show()
			self.label57.show()
			self.label58.show()
			self.StartT.show()
			self.LaunchVx.show()
			self.LaunchVy.show()
			self.LaunchVz.show()
			self.LaunchAVx.show()
			self.LaunchAVy.show()
			self.LaunchAVz.show()
			self.SpawnSx.show()
			self.SpawnSy.show()
			self.SpawnSz.show()
			self.SpawnEx.show()
			self.SpawnEy.show()
			self.SpawnEz.show()
			self.popup10.show()
			self.popup11.show()
		elif self.popup9.currentText()=="true":
			self.label49.hide()
			self.label50.hide()
			self.label51.hide()
			self.label52.hide()
			self.label53.hide()
			self.label54.hide()
			self.label55.hide()
			self.label56.hide()
			self.label57.hide()
			self.label58.hide()
			self.StartT.hide()
			self.LaunchVx.hide()
			self.LaunchVy.hide()
			self.LaunchVz.hide()
			self.LaunchAVx.hide()
			self.LaunchAVy.hide()
			self.LaunchAVz.hide()
			self.SpawnSx.hide()
			self.SpawnSy.hide()
			self.SpawnSz.hide()
			self.SpawnEx.hide()
			self.SpawnEy.hide()
			self.SpawnEz.hide()
			self.popup10.hide()
			self.popup11.hide()

	def Vis2(self):
		if self.popup21.currentText()=="true":
			self.Type4.show()
			self.LayerWidth.show()
			self.Directionx.show()
			self.Directiony.show()
			self.Directionz.show()
			self.label91.show()
			self.label92.show()
			self.label93.show()
		elif self.popup21.currentText()=="false":
			self.Type4.hide()
			self.LayerWidth.hide()
			self.Directionx.hide()
			self.Directiony.hide()
			self.Directionz.hide()
			self.label91.hide()
			self.label92.hide()
			self.label93.hide()
	def Vis3(self):
		if self.popup12.currentText()=="true":
			self.Type1.show()
			self.Bin.show()
			self.label72.show()
			self.label74.show()
		elif self.popup12.currentText()=="false":
			self.Type1.hide()
			self.Bin.hide()
			self.label72.hide()
			self.label74.hide()

	def Vis4(self):
		if self.popup13.currentText()=="true":
			self.Type2.show()
			self.Freq.show()
			self.label79.show()
			self.label80.show()
		elif self.popup13.currentText()=="false":
			self.Type2.hide()
			self.Freq.hide()
			self.label79.hide()
			self.label80.hide()

	def Vis5(self):
		if self.popup14.currentText()=="true":
			self.Detail1.show()
			self.Freq2.show()
			self.label130.show()
			self.label131.show()
		elif self.popup14.currentText()=="false":
			self.Detail1.hide()
			self.Freq2.hide()
			self.label130.hide()
			self.label131.hide()

	def Vis6(self):
		if self.popup15.currentText()=="true":
			self.ColorT1.show()
			self.Freq3.show()
			self.label132.show()
			self.label133.show()
		elif self.popup15.currentText()=="false":
			self.ColorT1.hide()
			self.Freq3.hide()
			self.label132.hide()
			self.label133.hide()

	def Vis7(self):
		if self.popup20.currentText()=="true":
			self.NumColor.show()
			self.label2000.show()
		elif self.popup20.currentText()=="false":
			self.NumColor.hide()
			self.label2000.hide()

	def Vis8(self):
		if self.popup8.currentText()=="true":
			self.Originx.show()
			self.Originy.show()
			self.Originz.show()
			self.label42.show()
			self.label43.show()
			self.label44.show()
			self.WorldSx.show()
			self.WorldSy.show()
			self.WorldSz.show()
			self.CellSix.show()
			self.CellSiy.show()
			self.CellSiz.show()
		elif self.popup8.currentText()=="false":
			self.Originx.hide()
			self.Originy.hide()
			self.Originz.hide()
			self.label42.hide()
			self.label43.hide()
			self.label44.hide()
			self.WorldSx.hide()
			self.WorldSy.hide()
			self.WorldSz.hide()
			self.CellSix.hide()
			self.CellSiy.hide()
			self.CellSiz.hide()

	def Vis9(self):
		if self.popup6.currentText()=="true":
			self.n1.show()
			self.n2.show()
			self.n3.show()
			self.n4.show()
			self.n5.show()
			self.n6.show()
		elif self.popup6.currentText()=="false":
			self.n1.hide()
			self.n2.hide()
			self.n3.hide()
			self.n4.hide()
			self.n5.hide()
			self.n6.hide()

	def OpenFile(self):
		self.name=""
		if self.popup9.currentText()=="true":
			self.name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
		else:
			pass

	def onCancel(self):
		self.result			= userCancelled
		self.close()

	def onReset1(self):
		self.result         = userReset1
		self.label2.setText("                                                                                                                  ", self)
		print(listWOBJ)
		listWOBJ.clear()
		print(listWOBJ)


	def onOk(self):
		self.result			= userOK
		self.close()
		a=len(list9)
		b=len(list9)
		b=str(b)
		for n in range (0,a):
			reply = QtGui.QInputDialog.getText(None, "Warning!","Enter the number of "+list9[n]+":")
			if reply[1]:
				nombre.append(reply)
			else:
				self.close()
			n+=1


userCancelled= "Cancelled"
userOK= "OK"
userReset1 = "Reset"

form = Test()
form.exec_()

class FluidSimu(QtGui.QDialog):
	def __init__(self):
		super(FluidSimu, self).__init__()
		self.initUI()
	def initUI(self):
		#Set up GUI
		# define window	xLoc,yLoc,xDim,yDim
		self.setGeometry(600, 400, 400, 300)
		a=form.Type3.text()
		n=0
		self.setWindowTitle("Fluid Coupling")
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.label24 = QtGui.QLabel("Type",self)
		self.label24.move(50,50)
		self.label25 = QtGui.QLabel("Dimention",self)
		self.label25.move(50,80)
		self.label26 = QtGui.QLabel("Value",self)
		self.label26.move(50,110)
		self.label27 = QtGui.QLabel("Direction",self)
		self.label27.move(50,140)
		self.label28 = QtGui.QLabel("Sign",self)
		self.label28.move(50,170)
		self.label29 = QtGui.QLabel("Freq",self)
		self.label29.move(50,200)

		self.Type1 = QtGui.QLineEdit(self)
		self.Type1.setText("0")
		self.Type1.setFixedWidth(90)
		self.Type1.move(210,45)
		self.Dimention = QtGui.QLineEdit(self)
		self.Dimention.setText("0")
		self.Dimention.setFixedWidth(90)
		self.Dimention.move(210,75)
		self.Value =  QtGui.QLineEdit(self)
		self.Value.setText("0")
		self.Value.setFixedWidth(90)
		self.Value.move(210,105)
		self.Direction = QtGui.QLineEdit(self)
		self.Direction.setText("Y")
		self.Direction.setFixedWidth(90)
		self.Direction.move(210,135)
		self.Sign = QtGui.QLineEdit(self)
		self.Sign.setText("1")
		self.Sign.setFixedWidth(90)
		self.Sign.move(210,165)
		self.Freq = QtGui.QLineEdit(self)
		self.Freq.setText("0.0")
		self.Freq.setFixedWidth(90)
		self.Freq.move(210,195)

		#Cancel button
		cancelButton = QtGui.QPushButton('Cancel', self)
		cancelButton.clicked.connect(self.onCancel)
		cancelButton.setAutoDefault(True)
		cancelButton.move(150, 250)
		# OK button

		okButton = QtGui.QPushButton('OK', self)
		okButton.clicked.connect(self.onOk)
		okButton.move(260, 250)


	def onCancel(self):
		self.result			= userCancelled
		self.close()

	def onOk(self):
		self.result			= userOK
		self.close()

userCancelled= "Cancelled"
userOK= "OK"


#Tallies
if form.Type3.text()=="0":
	pass
else:
	por=form.Type3.text()
	por=int(por)
	i=0
	for i in range (0,por):
		exec("TalliesL{}=[]".format(i))
		i+=1
	i=0
	for i in range (0,por):
		exec("""class Tallies{}(QtGui.QDialog):
		def __init__(self):
			super(Tallies{}, self).__init__()
			self.initUI()
		def initUI(self):
			#Set up GUI
			# define window	xLoc,yLoc,xDim,yDim
			self.setGeometry(600, 400, 400, 300)
			a=form.Type3.text()
			n=0
			self.setWindowTitle("Option for Tallies {}")
			self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
			self.label24 = QtGui.QLabel("Type",self)
			self.label24.move(50,50)
			self.label25 = QtGui.QLabel("Dimention",self)
			self.label25.move(50,80)
			self.label26 = QtGui.QLabel("Value",self)
			self.label26.move(50,110)
			self.label27 = QtGui.QLabel("Direction",self)
			self.label27.move(50,140)
			self.label28 = QtGui.QLabel("Sign",self)
			self.label28.move(50,170)
			self.label29 = QtGui.QLabel("Freq",self)
			self.label29.move(50,200)

			self.Type1 = QtGui.QLineEdit(self)
			self.Type1.setText("0")
			self.Type1.setFixedWidth(90)
			self.Type1.move(210,45)
			self.Dimention = QtGui.QLineEdit(self)
			self.Dimention.setText("0")
			self.Dimention.setFixedWidth(90)
			self.Dimention.move(210,75)
			self.Value =  QtGui.QLineEdit(self)
			self.Value.setText("0")
			self.Value.setFixedWidth(90)
			self.Value.move(210,105)
			self.Direction = QtGui.QLineEdit(self)
			self.Direction.setText("Y")
			self.Direction.setFixedWidth(90)
			self.Direction.move(210,135)
			self.Sign = QtGui.QLineEdit(self)
			self.Sign.setText("1")
			self.Sign.setFixedWidth(90)
			self.Sign.move(210,165)
			self.Freq = QtGui.QLineEdit(self)
			self.Freq.setText("0.0")
			self.Freq.setFixedWidth(90)
			self.Freq.move(210,195)

			#Cancel button
			cancelButton = QtGui.QPushButton('Cancel', self)
			cancelButton.clicked.connect(self.onCancel)
			cancelButton.setAutoDefault(True)
			cancelButton.move(150, 250)
			# OK button
			okButton = QtGui.QPushButton('OK', self)
			okButton.clicked.connect(self.onOk)
			okButton.move(260, 250)

		def onCancel(self):
			self.result			= userCancelled
			self.close()

		def onOk(self):
			self.result			= userOK
			self.close()

userCancelled= "Cancelled"
userOK= "OK"

alpha= Tallies{}()
alpha.exec_()
if alpha.result==userCancelled:
	pass # steps to handle user clicking Cancel
else:
	TalliesL{}.append(alpha.Type1.text())
	TalliesL{}.append(alpha.Dimention.text())
	TalliesL{}.append(alpha.Value.text())
	TalliesL{}.append(alpha.Direction.text())
	TalliesL{}.append(alpha.Sign.text())
	TalliesL{}.append(alpha.Freq.text())""".format(i,i,i,i,i,i,i,i,i,i))
		i+=1

	por=form.Type3.text()
	por=int(por)
	lm=0
	for lm in range (0,por):
		ratata=lm+1
		ratata=str(ratata)
		lm=str(lm)
		exec("pro2{}=[]".format(lm))
		exec("tr1{}=TalliesL{}[0]".format(lm,lm))
		exec("tr2{}=TalliesL{}[1]".format(lm,lm))
		exec("tr3{}=TalliesL{}[2]".format(lm,lm))
		exec("tr4{}=TalliesL{}[3]".format(lm,lm))
		exec("tr5{}=TalliesL{}[4]".format(lm,lm))
		exec("tr6{}=TalliesL{}[5]".format(lm,lm))
		exec("""pro2{}.append(ratata +" Type: "+tr1{}+" Dimension: "+tr2{}+" Value: "+tr3{}+"  Dir: "+tr4{}+" Sign: "+tr5{}+" Ferq: "+tr6{})""".format(lm,lm,lm,lm,lm,lm,lm,lm))
		lm=float(lm)
		lm+=1

#NumColor
if form.NumColor.text()=="0":
	pass
else:
	por=form.NumColor.text()
	por=int(por)
	i=0
	for i in range (0,por):
		exec("NumColor{}=[]".format(i))
		i+=1
	i=0
	for i in range (0,por):
		exec("""class onNumColor{}(QtGui.QDialog):
		def __init__(self):
			super(onNumColor{}, self).__init__()
			self.initUI()
		def initUI(self):
			#Set up GUI
			# define window	xLoc,yLoc,xDim,yDim
			self.setGeometry(600, 400, 400, 300)
			a=form.NumColor.text()
			n=0
			self.setWindowTitle("Option for NumColor {}")
			self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
			self.label24 = QtGui.QLabel("X",self)
			self.label24.move(50,50)
			self.label25 = QtGui.QLabel("Y",self)
			self.label25.move(50,80)
			self.label26 = QtGui.QLabel("Z",self)
			self.label26.move(50,110)

			self.X = QtGui.QLineEdit(self)
			self.X.setText("0")
			self.X.setFixedWidth(90)
			self.X.move(210,45)
			self.Y = QtGui.QLineEdit(self)
			self.Y.setText("0")
			self.Y.setFixedWidth(90)
			self.Y.move(210,75)
			self.Z =  QtGui.QLineEdit(self)
			self.Z.setText("0")
			self.Z.setFixedWidth(90)
			self.Z.move(210,105)

			#Cancel button
			cancelButton = QtGui.QPushButton('Cancel', self)
			cancelButton.clicked.connect(self.onCancel)
			cancelButton.setAutoDefault(True)
			cancelButton.move(150, 250)
			# OK button
			okButton = QtGui.QPushButton('OK', self)
			okButton.clicked.connect(self.onOk)
			okButton.move(260, 250)

		def onCancel(self):
			self.result			= userCancelled
			self.close()

		def onOk(self):
			self.result			= userOK
			self.close()

userCancelled= "Cancelled"
userOK= "OK"

alpha= onNumColor{}()
alpha.exec_()
if alpha.result==userCancelled:
	pass # steps to handle user clicking Cancel
else:
	NumColor{}.append(alpha.X.text())
	NumColor{}.append(alpha.Y.text())
	NumColor{}.append(alpha.Z.text())""".format(i,i,i,i,i,i,i))
		i+=1

	por=form.NumColor.text()
	por=int(por)
	lm=0
	for lm in range (0,por):
		ratata=lm+1
		ratata=str(ratata)
		lm=str(lm)
		exec("pro3{}=[]".format(lm))
		exec("tr1{}=NumColor{}[0]".format(lm,lm))
		exec("tr2{}=NumColor{}[1]".format(lm,lm))
		exec("tr3{}=NumColor{}[2]".format(lm,lm))
		exec("""pro3{}.append(tr1{}+" "+tr2{}+" "+tr3{})""".format(lm,lm,lm,lm))
		exec("print(pro3{})".format(lm))
		lm=float(lm)
		lm+=1

a=len(list9)
n=0
for n in range (0,a):
	n=int(n)
	b=nombre[n][0]
	c=list9[n]
	b=str(b)
	n=str(n)
	list10.append("""Index: 1 Name: """ + c + """ Number: """+b)
	n=float(n)
	n+=1
a=str(a)


def trueWorld():
	alpha=len(listWOBJ)
	alpha=str(alpha)
	por=len(nbextrude)
	por=str(por)
	a=len(list9)
	a=str(a)
	if form.label73.text()=="true":
		apoi="""Type:"""+form.Type4.text()+""" LayerWidth: """+form.LayerWidth.text()+""" Direction: """+form.Directionx.text()+""" """+form.Directiony.text()+""" """+form.Directionz.text()
	else:
		apoi=""
	if form.label90.text()=="true":
		apo="""Type: """+form.Type1.text()
	elif form.Type1.text() == "1" or form.Type1.text()=="2":
		apo="""Type: """+form.Type1.text()+""" Bin: """+form.Bin.text()
	else:
		apo=" "
	if form.popup13.currentText()=="true":
		apop="""Type: """+form.Type2.text()+""" Freq: """+form.Freq.text()
	else:
		apop=""
	if form.popup14.currentText()=="true":
		apoph="""Freq """+form.Freq2.text()+""" Detail """+form.Detail1.text()
	else:
		apoph=""
	if form.popup15.currentText()=="true":
		apophi="""Freq: """+form.Freq3.text()+""" ColorType: """+form.ColorT1.text()
	else:
		apophi=""
	if form.popup8.currentText()=="true":
		apophis="""Origin:  """+form.Originx.text()+"""   """+form.Originy.text()+"""    """+form.Originz.text()+"""
WorldSize: """+form.WorldSx.text()+"""   """+form.WorldSy.text()+"""   """+form.WorldSz.text()+"""
Cell_Size: """+form.CellSix.text()+""" """+form.CellSiy.text()+""" """+form.CellSiz.text()+""" """
	else:
		apophis=""
	if form.popup6.currentText()=="true":
		shunkan=form.n1.text()+" "+form.n2.text()+" "+form.n3.text()+" "+form.n4.text()+" "+form.n5.text()+" "+form.n6.text()
	else:
		shunkan=""

	if os.path.isfile(filename+".World")==True:
		test=os.remove(filename+".World")
	a=str(a)
	text="""VER: 1.1

=================================================
_BEGIN_MODELSECTION_

NormalContactModel:   """+form.NCM.text()+"""
TangetContactModel:   """+form.TCM.text()+"""
RollingContactModel:  """+form.RCM.text()+"""
CohesionContactModel: """+form.CCM.text()+"""

_END_MODELSECTION_

ParticleType:           """+form.ParticleType.text()+"""
TimeStep: """+form.TimeStep.text()+"""

=================================================

=================================================
             1_Geometrical-Information


---------------------------------------
 1.1_World_Objects
---------------------------------------

Number: """+alpha

	VOBJ=open("Project1.txt", "w")
	VOBJ.write(text)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		n=0
		b=len(listWOBJ)
		for n in range (0,b):
			file.write("""
Index: 1 Name: """ + listWOBJ[n])
			n=n+1

	rip="""
---------------------------------------
 1.2_Particle_Objects_(index__name)
---------------------------------------

Number: """+a+"""

"""


	VOBJ=open("Project1.txt", "a")
	VOBJ.write(rip)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		n=0
		a=len(list9)
		for n in range (0,a):
			file.write(list10[n]+"\n")
			n=n+1

	tell="""
---------------------------------------
1.3_Volume_Objects_(index__name)
---------------------------------------

Number: """+por+"""

"""
	VOBJ=open("Project1.txt", "a")
	VOBJ.write(tell)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		i=0
		por=len(nbextrude)
		for i in range (0,por):
			exec("""file.write("Index: 1 Name: "+nbextrude[{}]
+'\\n')""".format(i))
			i+=1

	gnee="""

=================================================

=================================================
              2_Simulation_Setup

Total_Time:  """+form.TotalT.text()+"""
ForceField(cm/s): """+form.ForceFx.text()+""" """+form.ForceFy.text()+""" """+form.ForceFz.text()+"""
ParticleRotation: """+form.label36.text()+"""
VelLimit: """+form.label37.text()+"""
ValidZone: """+form.label38.text()+""" """+shunkan+"""
=================================================


=================================================
             3_BroadPhase-(Boxing)

GridPerSize: """+form.label45.text()+"""
OverRide:    """+form.label46.text()+"""
"""+apophis+"""

=================================================


=================================================
              4_Inital_Particle-Setup

ReadFromFile:                     """+form.label56.text()+"""
StartType:     """+form.StartT.text()+"""
RandomOrient:         """+form.label57.text()+"""
RandomStartVel: """+form.label58.text()+"""
launchVel(cm/s):  """+form.LaunchVx.text()+""" """+form.LaunchVy.text()+""" """+form.LaunchVz.text()+"""
launchAVel: """+form.LaunchAVx.text()+""" """+form.LaunchAVy.text()+""" """+form.LaunchAVz.text()+"""
SpawnStart: """+form.SpawnSx.text()+""" """+form.SpawnSy.text()+""" """+form.SpawnSz.text()+"""
SpawnEnd    """+form.SpawnEx.text()+""" """+form.SpawnEy.text()+""" """+form.SpawnEz.text()+"""

=================================================


=================================================
              5_OutputOptions

Display(0=type,1=vel(binsize),2=pen(binsize)):	"""+form.label73.text()+""" """+apo+"""
View: """+form.View.text()+"""
Cut """+form.label75.text()+""" """+apop+"""
FPS: """+form.FPS.text()+"""
GLDebug: """+form.GLDebug.text()+"""
FileWrite: """+form.label76.text()+""" """+apoph+"""
SnapShotWrite: """+form.label77.text()+""" """+apophi+"""
EnergyDiss """+form.label78.text()+"""
EnergySpectra """+form.label81.text()+"""
ContactInfo """+form.label82.text()+"""
VolCellInfo: """+form.label83.text()+"""

=================================================


=================================================
              6_Tallies

Num_tallies: """+form.Type3.text()+"""
"""

	VOBJ=open("Project1.txt", "a")
	VOBJ.write(gnee)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		i=0
		por=form.Type3.text()
		por=int(por)
		for i in range (0,por):
			exec("""
file.write(pro2{}[0]
+'\\n')""".format(i))
			i+=1

	trololo="""=================================================


=================================================
              7_Color_Options

Custom_Color:       """+form.label89.text()+"""
"""

	VOBJ=open("Project1.txt", "a")
	VOBJ.write(trololo)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		i=0
		por=form.NumColor.text()
		por=int(por)
		for i in range (0,por):
			exec("""
file.write(pro3{}[0]
+'\\n')""".format(i))

	xD="""Manual_Layer_Colors: """+form.label90.text()+""" """+apoi+"""
=================================================

LOADPROFILE: """+form.LoadProfile.text()+"""
"""

	VOBJ=open("Project1.txt", "a")
	VOBJ.write(xD)
	VOBJ.close()
	os.rename(dir_+"/Project1.txt",dir_+"/"+filename+".World")

def falseWorld():
	alpha=len(listWOBJ)
	alpha=str(alpha)
	por=len(nbextrude)
	por=str(por)
	a=len(list9)
	a=str(a)
	if form.label72.text()=="true":
		apoi="""Type:"""+form.Type4.text()+""" LayerWidth: """+form.LayerWidth.text()+""" Direction: """+form.Directionx.text()+""" """+form.Directiony.text()+""" """+form.Directionz.text()
	else:
		apoi=""
	if form.label90.text()=="true":
		apo="""Type:"""+form.Type1.text()
		if form.Type1.text() == "1" or form.Type1.text()=="2":
			apo="""Type:"""+form.Type1.text()+""" Bin: """+form.Bin.text()
	else:
		apo=""
	if form.popup13.currentText()=="true":
		apop="""Type:"""+form.Type2.text()+""" Freq:"""+form.Freq.text()
	else:
		apop=""
	if form.popup14.currentText()=="true":
		apoph="""Freq:"""+form.Freq2.text()+""" Detail:"""+form.Detail1.text()
	else:
		apoph=""
	if form.popup15.currentText()=="true":
		apophi="""Freq:"""+form.Freq3.text()+""" ColorType:"""+form.ColorT1.text()
	else:
		apophi=""
	if form.popup8.currentText()=="true":
		apophis="""Origin:  """+form.Originx.text()+"""   """+form.Originy.text()+"""    """+form.Originz.text()+"""
WorldSize: """+form.WorldSx.text()+"""   """+form.WorldSy.text()+"""   """+form.WorldSz.text()+"""
Cell_Size: """+form.CellSix.text()+""" """+form.CellSiy.text()+""" """+form.CellSiz.text()+""" """
	else:
		apophis=""
	if form.popup6.currentText()=="true":
		shunkan=form.n1.text()+" "+form.n2.text()+" "+form.n3.text()+" "+form.n4.text()+" "+form.n5.text()+" "+form.n6.text()
	else:
		shunkan=""

	if os.path.isfile("Project1.World")==True:
		test=os.remove("Project1.World")
	a=str(a)
	text="""VER: 1.1

=================================================
_BEGIN_MODELSECTION_

NormalContactModel:   """+form.NCM.text()+"""
TangetContactModel:   """+form.TCM.text()+"""
RollingContactModel:  """+form.RCM.text()+"""
CohesionContactModel: """+form.CCM.text()+"""

_END_MODELSECTION_

ParticleType:           """+form.ParticleType.text()+"""
TimeStep: """+form.TimeStep.text()+"""

=================================================

=================================================
             1_Geometrical-Information


---------------------------------------
 1.1_World_Objects
---------------------------------------

Number: """+alpha

	VOBJ=open("Project1.txt", "w")
	VOBJ.write(text)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		n=0
		b=len(listWOBJ)
		for n in range (0,b):
			file.write("""
Index: 1 Name: """ + listWOBJ[n]+"""
""")
			n=n+1

	rip="""
---------------------------------------
 1.2_Particle_Objects_(index__name)
---------------------------------------

Number: """+a+"""

"""


	VOBJ=open("Project1.txt", "a")
	VOBJ.write(rip)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		n=0
		a=len(list9)
		for n in range (0,a):
			file.write(list10[n]+"\n")
			n=n+1

	tell="""
---------------------------------------
1.3_Volume_Objects_(index__name)
---------------------------------------

Number: """+por+"""

"""
	VOBJ=open("Project1.txt", "a")
	VOBJ.write(tell)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		i=0
		por=len(nbextrude)
		for i in range (0,por):
			exec("""file.write(pro{}[0]
+'\\n')""".format(i))
			i+=1

	gnee="""

=================================================

=================================================
              2_Simulation_Setup

Total_Time:  """+form.TotalT.text()+"""
ForceField(cm/s): """+form.ForceFx.text()+""" """+form.ForceFy.text()+""" """+form.ForceFz.text()+"""
ParticleRotation: """+form.label36.text()+"""
VelLimit: """+form.label37.text()+"""
ValidZone: """+form.label38.text()+""" """+shunkan+"""
=================================================


=================================================
             3_BroadPhase-(Boxing)

GridPerSize: """+form.label45.text()+"""
OverRide:    """+form.label46.text()+"""
"""+apophis+"""

=================================================


=================================================
              4_Inital_Particle-Setup

ReadFromFile:                     """+form.label56.text()+"""

Path: """+name+"""

=================================================


=================================================
              5_OutputOptions

Display(0=type,1=vel(binsize),2=pen(binsize)):	"""+form.label73.text()+""" """+apo+"""
View: """+form.View.text()+"""
Cut """+form.label75.text()+""" """+apop+"""
FPS: """+form.FPS.text()+"""
GLDebug: """+form.GLDebug.text()+"""
FileWrite: """+form.label76.text()+""" """+apoph+"""
SnapShotWrite: """+form.label77.text()+""" """+apophi+"""
EnergyDiss """+form.label78.text()+"""
EnergySpectra """+form.label81.text()+"""
ContactInfo """+form.label82.text()+"""
VolCellInfo: """+form.label83.text()+"""

=================================================


=================================================
              6_Tallies

Num_tallies: """+form.Type3.text()+"""
"""

	VOBJ=open("Project1.txt", "a")
	VOBJ.write(gnee)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		i=0
		por=form.Type3.text()
		por=int(por)
		for i in range (0,por):
			exec("""
file.write(pro2{}[0]
+'\\n')""".format(i))
			i+=1

	trololo="""=================================================


=================================================
              7_Color_Options

Custom_Color:       """+form.label89.text()+"""
"""

	VOBJ=open("Project1.txt", "a")
	VOBJ.write(trololo)
	VOBJ.close()

	with open("Project1.txt","a") as file:
		i=0
		por=form.NumColor.text()
		por=int(por)
		for i in range (0,por):
			exec("""
file.write(pro3{}[0]
+'\\n')""".format(i))

	xD="""Manual_Layer_Colors: """+form.label90.text()+""" """+apoi+"""
=================================================

LOADPROFILE: """+form.LoadProfile.text()+"""
"""

	VOBJ=open("Project1.txt", "a")
	VOBJ.write(xD)
	VOBJ.close()
	os.rename(dir_+"/Project1.txt",dir_+"/"+filename+".World")

if form.popup9.currentText()=="false":
	Tr=trueWorld()
else:
	Tr=falseWorld()

Tr.exec_()