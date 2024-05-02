import urllib.request
import wx
import sys
import tempfile,os
from AppUpdations import __version__


FROZEN = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        panel = wx.Panel(self)
        label =wx.StaticText(panel,label= f"{__version__}",pos=(70,35))
        # self.text_ctrl = wx.TextCtrl(panel, pos=(50, 50), size=(200, -1))
        btn_checking = wx.Button(panel, label="Check for new version availability", pos=(50, 100))
        btn_checking.Bind(wx.EVT_BUTTON, self.on_button_click)

        btn_downloading = wx.Button(panel, label="Download new version", pos=(50, 20))
        btn_downloading.Bind(wx.EVT_BUTTON, self.on_button_click_dwnld)

        label  = wx.StaticText(panel,label= f"version is {__version__}",pos = (35,43))

    def on_button_click(self, event):
        update_url = 'http://127.0.0.1:5000/latest_version'
        response = urllib.request.urlopen(update_url)
        dt=response.read().decode('utf-8')
        print(response.read().decode('utf-8'))
        wx.MessageBox( f'{dt}','Info', wx.OK | wx.ICON_INFORMATION)

    def on_button_click_dwnld(self, event):
        # Ask user for confirmation
        dlg = wx.MessageDialog(self, "Do you want to download and install the new version?", "Confirmation", wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()

        if result == wx.ID_YES:
            print("Download and install operations")
            import AppUpdations as app
            # Function calling to the Client
            app.main()
        else:
            print("Download canceled by user")
        

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "Simple wxPython App")
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
