import wx

app=wx.App()

class Window(wx.Frame):
	def __init__(self):
		super().__init__(parent=None,title='This is a button.')
		self.panel=wx.Panel(self)
		self.sizer=wx.BoxSizer(wx.VERTICAL)
		
		self.buttons={}
		self.buttons['one']=wx.Button(self, label='I am a button.',pos=(150,90))
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress1)
	def BtnPress1(self, event):

		self.buttons['one'].SetLabel('Whoa.')
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress2)
	def BtnPress2(self, event):

		self.buttons['one'].Hide()
		self.buttons['one'].Destroy()

		self.buttons['two']=wx.Button(self, label='What do you think you are doing?',pos=(95,90))
		self.buttons['two'].Bind(wx.EVT_BUTTON, self.BtnPress3)
	def BtnPress3(self, event):

		self.buttons['two'].Hide()
		self.buttons['two'].Destroy()

		self.buttons['three']=wx.Button(self, label='Are you seriously going to continue clicking me?',pos=(50,90))
		self.buttons['three'].Bind(wx.EVT_BUTTON, self.BtnPress4)
	def BtnPress4(self,event):

		self.buttons['three'].Hide()
		self.buttons['three'].Destroy()

		self.buttons['one']=wx.Button(self, label='How rude.',pos=(160,90))
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress5)
	def BtnPress5(self, event):

		self.buttons['one'].SetLabel('...')
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress6)
	def BtnPress6(self, event):

		self.buttons['one'].SetLabel('.....')
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress7)
	def BtnPress7(self, event):

		self.buttons['one'].Hide()
		self.buttons['one'].Destroy()

		self.buttons['two']=wx.Button(self, label='Will you stop?!',pos=(150,90))
		self.buttons['two'].Bind(wx.EVT_BUTTON, self.BtnPress8)
	def BtnPress8(self,event):

		self.buttons['two'].SetLabel('...')
		self.buttons['two'].Bind(wx.EVT_BUTTON, self.BtnPress9)
	def BtnPress9(self,event):

		self.buttons['two'].SetLabel('.....')
		self.buttons['two'].Bind(wx.EVT_BUTTON, self.BtnPress10)
	def BtnPress10(self,event):

		self.buttons['two'].SetLabel('...I guess not.')
		self.buttons['two'].Bind(wx.EVT_BUTTON, self.BtnPress11)
	def BtnPress11(self,event):

		self.buttons['two'].SetLabel('Fine.')
		self.buttons['two'].Bind(wx.EVT_BUTTON, self.BtnPress12)
	def BtnPress12(self, event):

		self.buttons['two'].Hide()
		self.buttons['two'].Destroy()

		self.buttons['three']=wx.Button(self, label='We will do it your way.',pos=(130,90))
		self.buttons['three'].Bind(wx.EVT_BUTTON, self.BtnPress13)
	def BtnPress13(self,event):

		self.buttons['three'].SetLabel('Try to catch me!')
		self.buttons['three'].Bind(wx.EVT_BUTTON, self.BtnPress14)
	def BtnPress14(self,event):

		self.buttons['three'].Hide()
		self.buttons['three'].Destroy()

		self.buttons['one']=wx.Button(self, label='HA!',pos=(20,20))
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress15)
	def BtnPress15(self,event):
		self.buttons['one'].Hide()
		self.buttons['one'].Destroy()

		self.buttons['one']=wx.Button(self, label='Didn\'t expect that, did you?',pos=(200,200))
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress16)
	def BtnPress16(self,event):

		self.buttons['one'].Hide()
		self.buttons['one'].Destroy()

		self.buttons['four']=wx.Button(self, label='Now there are two buttons!',pos=(140,60))
		self.buttons['four'].Bind(wx.EVT_BUTTON, self.BtnPress17)

		self.buttons['five']=wx.Button(self, label='What are you going to do now?',pos=(80,120))
		self.buttons['five'].Bind(wx.EVT_BUTTON, self.BtnPress17)
	def BtnPress17(self,event):
		self.buttons['four'].Hide()
		self.buttons['four'].Destroy()
		self.buttons['five'].Hide()
		self.buttons['five'].Destroy()

		self.buttons['six']=wx.Button(self, label='Muahahaha!',pos=(170,45))
		self.buttons['six'].Bind(wx.EVT_BUTTON, self.BtnPress18)

		self.buttons['seven']=wx.Button(self, label='Now there\'s even more of us!',pos=(40,100))
		self.buttons['seven'].Bind(wx.EVT_BUTTON, self.BtnPress18)

		self.buttons['eight']=wx.Button(self, label='More buttons!',pos=(225,155))
		self.buttons['eight'].Bind(wx.EVT_BUTTON, self.BtnPress18)
	def BtnPress18(self,event):

		self.buttons['six'].Hide()
		self.buttons['six'].Destroy()
		self.buttons['seven'].Hide()
		self.buttons['seven'].Destroy()
		self.buttons['eight'].Hide()
		self.buttons['eight'].Destroy()

		self.buttons['one']=wx.Button(self, label='Okay, I\'m tired now.',pos=(135,90))
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress19)
	def BtnPress19(self,event):
		self.buttons['one'].Hide()
		self.buttons['one'].Destroy()

		self.buttons['one']=wx.Button(self, label='You really have a knack for clicking buttons.',pos=(65,90))
		self.buttons['one'].Bind(wx.EVT_BUTTON, self.BtnPress20)
	def BtnPress20(self,event):
		self.buttons['one'].Hide()
		self.buttons['one'].Destroy()
		label = wx.StaticText(self, label = "The end!", pos = (175,90)) 




		self.panel.SetSizer(self.sizer)
		self.Show(True)
Window().Show(True)
app.MainLoop()
