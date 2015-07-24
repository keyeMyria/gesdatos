#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes
from Requests import Request

class Head(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self, parent)
		self.SetBackgroundColour("white")
		head = HeadLow.Head(self)
		sizerhead = wx.BoxSizer(wx.VERTICAL)
		sizerhead.Add(head,0,wx.EXPAND|wx.ALL,border=10)
		self.SetSizer(sizerhead)
##---------------------------------------------

## Body
##-----------------------------------------------------------
class Body(wx.Panel):
    
	def __init__(self,parent):
		wx.Panel.__init__(self,parent) # Inicializaci�n Panel Padre
		self.SetBackgroundColour("white")
		Component = Componentes.Component(self) # Instancia Clase Componente
                self.solicitud = Request()                             
                
  #----Creaci�n de un panel de TxtArea, e inclusi�n  del objeto TxtArea y su Label
		PanelComponentsTitulo = wx.Panel(self) #Creacion padre hijo
		self.labelTitulo = Component.CreateLabel(PanelComponentsTitulo,25,pos=(0,0),label="Registro de usuarios")
                
		                
#----Creaci�n de un panel de TxtArea, e inclusi�n  del objeto TxtArea y su Label
		PanelComponentsNombre = wx.Panel(self) #Creacion padre hijo
		self.labelNombre = Component.CreateLabel(PanelComponentsNombre,15,pos=(0,0),label="Nombre:        ")
		self.TxtAreaNombre = Component.CreateImputText(PanelComponentsNombre,pos=(0,0),size=(200,22))
		sizerPanelNombre = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tama�os
		sizerPanelNombre.Add(self.labelNombre , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelNombre.Add(self.TxtAreaNombre , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsNombre.SetSizer(sizerPanelNombre)
		PanelComponentsNombre.SetBackgroundColour("white") #Asignaci�n de Color de Fondo 
                                
#----Creaci�n de un panel de TxtArea, e inclusi�n  del objeto TxtArea y su Label
		PanelComponentsApellido = wx.Panel(self) #Creacion padre hijo
		self.labelApellido = Component.CreateLabel(PanelComponentsApellido,15,pos=(0,0),label="Apellido:        ")
		self.TxtAreaApellido = Component.CreateImputText(PanelComponentsApellido,pos=(0,0),size=(200,22))
		sizerPanelApellido = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tama�os
		sizerPanelApellido.Add(self.labelApellido , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelApellido.Add(self.TxtAreaApellido , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsApellido.SetSizer(sizerPanelApellido)
		PanelComponentsApellido.SetBackgroundColour("white") #Asignaci�n de Color de Fondo 
                
#----Creaci�n de un panel de TxtArea, e inclusi�n  del objeto TxtArea y su Label
		PanelComponentsDocumento = wx.Panel(self) #Creacion padre hijo
		self.labelDocumento = Component.CreateLabel(PanelComponentsDocumento,15,pos=(0,0),label="Documento:   ")
		self.TxtAreaDocumento = Component.CreateImputText(PanelComponentsDocumento,pos=(0,0),size=(200,22))
		sizerPanelDocumento = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tama�os
		sizerPanelDocumento.Add(self.labelDocumento , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelDocumento.Add(self.TxtAreaDocumento , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsDocumento.SetSizer(sizerPanelDocumento)
		PanelComponentsDocumento.SetBackgroundColour("white") #Asignaci�n de Color de Fondo 
                
#----Creaci�n de un panel de TxtArea, e inclusi�n  del objeto TxtArea y su Label
		PanelComponentsFechaNac = wx.Panel(self) #Creacion padre hijo
		self.labelFechaNac = Component.CreateLabel(PanelComponentsFechaNac,15,pos=(0,0),label="FechaNac:     ")
		self.TxtAreaFechaNac = Component.CreateImputText(PanelComponentsFechaNac,pos=(0,0),size=(200,22))
		sizerPanelFechaNac = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tama�os
		sizerPanelFechaNac.Add(self.labelFechaNac , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelFechaNac.Add(self.TxtAreaFechaNac , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsFechaNac.SetSizer(sizerPanelFechaNac)
		PanelComponentsFechaNac.SetBackgroundColour("white") #Asignaci�n de Color de Fondo 
                
               
#----Creaci�n de un panel de TxtArea, e inclusi�n  del objeto TxtArea y su Label
		PanelComponentsCorreo = wx.Panel(self) #Creacion padre hijo
		self.labelCorreo = Component.CreateLabel(PanelComponentsCorreo,15,pos=(0,0),label="Correo:         ")
		self.TxtAreaCorreo = Component.CreateImputText(PanelComponentsCorreo,pos=(0,0),size=(200,22))
		sizerPanelCorreo = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tama�os
		sizerPanelCorreo.Add(self.labelCorreo , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelCorreo.Add(self.TxtAreaCorreo , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCorreo.SetSizer(sizerPanelCorreo)
		PanelComponentsCorreo.SetBackgroundColour("white")
                
#----Creaci�n de un panel de TxtArea, e inclusi�n  del objeto TxtArea y su Label
		PanelComponentsCorreoUni = wx.Panel(self) #Creacion padre hijo
		self.labelCorreoUni = Component.CreateLabel(PanelComponentsCorreoUni,15,pos=(0,0),label="CorreoUni:     ")
		self.TxtAreaCorreoUni = Component.CreateImputText(PanelComponentsCorreoUni,pos=(0,0),size=(200,22))
		sizerPanelCorreoUni = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tama�os
		sizerPanelCorreoUni.Add(self.labelCorreoUni , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelCorreoUni.Add(self.TxtAreaCorreoUni , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCorreoUni.SetSizer(sizerPanelCorreoUni)
		PanelComponentsCorreoUni.SetBackgroundColour("white")
                
#----Creaci�n de un panel de TxtArea, e inclusi�n  del objeto TxtArea y su Label
		PanelComponentsUsuario = wx.Panel(self) #Creacion padre hijo
		self.labelUsuario = Component.CreateLabel(PanelComponentsUsuario,15,pos=(0,0),label="Usuario:        ")
		self.TxtAreaUsuario = Component.CreateImputText(PanelComponentsUsuario,pos=(0,0),size=(200,22))
		sizerPanelUsuario = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tama�os
		sizerPanelUsuario.Add(self.labelUsuario , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelUsuario.Add(self.TxtAreaUsuario , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsUsuario.SetSizer(sizerPanelUsuario)
		PanelComponentsUsuario.SetBackgroundColour("white") #Asignaci�n de Color de Fondo 
                
#----Creaci�n de un panel de ComboBox, e inclusi�n  del objeto ComboBox y su Label
		PanelComponentsCbxUniversidad = wx.Panel(self) #Creacion padre hijo
		self.labelCbxUniversidad = Component.CreateLabel(PanelComponentsCbxUniversidad,15,pos=(0,0),label="Universidad:   ")                
		self.CbUniversidad = Component.CreateComboBox(PanelComponentsCbxUniversidad,pos=(0,0),size=200,List=self.solicitud.verUniversidad())
		self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.CbUniversidad) #Creaci�n de Evento
		sizerPanelCbxUniversidad = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tama�os
		sizerPanelCbxUniversidad.Add(self.labelCbxUniversidad , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
		sizerPanelCbxUniversidad.Add(self.CbUniversidad , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCbxUniversidad.SetSizer(sizerPanelCbxUniversidad)
		PanelComponentsCbxUniversidad.SetBackgroundColour("white") #Asignaci�n de Color de Fondo 
                
                PanelComponentsRCategoria = wx.Panel(self) #Creacion padre hijo
		self.labelRadioBox = Component.CreateLabel(PanelComponentsRCategoria,15,pos=(0,0),label="Categoria:    ")
		ListaCategoria = ['Estudiante    ', 'Docente']
		self.RbCategoria = Component.CreateRadioBox(PanelComponentsRCategoria,"Tipo",ListaCategoria)
		self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.RbCategoria)#Creaci�n de Evento
		sizerPanelRadioBox = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tama�os
		sizerPanelRadioBox.Add(self.labelRadioBox , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelRadioBox.Add(self.RbCategoria , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsRCategoria.SetSizer(sizerPanelRadioBox)
		PanelComponentsRCategoria.SetBackgroundColour("white")
                
                
#----Creaci�n de un panel de Buttons, e inclusi�n  del objeto Buttons y su Label
		PanelComponentsBConfirmar = wx.Panel(self) #Creacion padre hijo		
		self.BConfirmar = Component.CreateButton(PanelComponentsBConfirmar,"Confirmar",(80,50))
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.BConfirmar)#Creaci�n de Evento
		sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tama�os
		sizerPanelButton.Add(self.BConfirmar , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsBConfirmar.SetSizer(sizerPanelButton) 
		PanelComponentsBConfirmar.SetBackgroundColour("white") #Asignaci�n de Color de Fondo 
                
                
                gs = wx.GridSizer(12, 1, 15, 15) #Creacion grilla de tama�o
      #--------------Adici�n de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tama�o de la pantalla
		gs.AddMany([(PanelComponentsTitulo,0,wx.ALIGN_CENTER), (PanelComponentsNombre,0,0),
                            (PanelComponentsApellido, 0, 0), (PanelComponentsDocumento, 0, 0),(PanelComponentsFechaNac, 0, 0),
                            (PanelComponentsCorreo, 0, 0),(PanelComponentsCorreoUni, 0, 0),(PanelComponentsUsuario, 0, 0),
                            (PanelComponentsCbxUniversidad,0,0),(PanelComponentsRCategoria,0,0),
                            (PanelComponentsBConfirmar, 0, wx.ALIGN_CENTER)])
                            
                #gs2 = wx.GridSizer(3, 1, 7, 7)
                #gs2.AddMany([(PanelComponentsTitulo,0,wx.ALIGN_CENTER,0,0),(gs)])
                #
                #gs3 = wx.GridSizer(1, 2, 7, 7)
                #gs3.AddMany([(PanelComponentsTitulo,0,wx.ALIGN_CENTER)])
     
		sizer = wx.BoxSizer(wx.VERTICAL) #Adici�n de la grilla de tama�os al panel padre
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)
                
        def EvtComboBox(self, event):
                cate = self.CbUniversidad.GetValue()
                print cate		
        
        def EvtRadioBox(self, event):
		self.TxtArea1.AppendText("Evento RabioBox")
                
        def OnClick(self,event):
		Nombre = self.TxtAreaNombre.GetValue()
                self.solicitud.registrarPersona(self.TxtAreaNombre.GetValue(),self.TxtAreaApellido.GetValue(),
                                                self.TxtAreaDocumento.GetValue(),self.TxtAreaFechaNac.GetValue(),
                                                self.TxtAreaCorreo.GetValue(),self.TxtAreaCorreoUni.GetValue(),
                                                self.CbUniversidad.GetValue(),self.TxtAreaUsuario.GetValue(),
                                                self.RbCategoria.GetSelection())
                print Nombre
               
##-----------------------------------------------------------
class Low(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		self.SetBackgroundColour("white")
		sizerlow = wx.BoxSizer(wx.VERTICAL)
		low = HeadLow.Low(self)
		sizerlow.Add(low,0,wx.EXPAND|wx.ALL,border=10)
		self.SetSizer(sizerlow)

##-----------------------------------------------------------


app=wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, 'Full display size', pos=(200, 0), size=(1000,900))
menubar = wx.MenuBar()
topPanel= scrolled.ScrolledPanel(frame)
topPanel.SetupScrolling(scroll_y=True)
topPanel.SetBackgroundColour("white")
sizertopPanel=wx.BoxSizer(wx.VERTICAL)
#sizertopPanel.Add(Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(Body(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
topPanel.SetSizer(sizertopPanel)
frame.Show()
app.MainLoop()