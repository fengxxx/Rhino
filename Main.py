import wx
import Scene
from Define import*
class mainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'fengxEngine', size=MAIN_WINDOW_SIZE,style=wx.DEFAULT_FRAME_STYLE)
        #---------------main Window settings----->>>>
        self.SetBackgroundColour((225,225,225))#MAIN_BG_COLOR)
        self.icon = wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.CreateStatusBar()
        #self.SetStatusText("fengxEngine: tartPos: "+str(TARGET_POS)+"eyePos: "+str(EYE_POS) )

        self.scene=Scene.mainGlCanvas(self)


mainApp = wx.PySimpleApp()
newFrame = mainFrame(parent=None, id=-1)
newFrame.Show()
newFrame.SetBackgroundColour((120,120,120))
mainApp.MainLoop()
