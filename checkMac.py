import wx
import time

application = wx.App()
framework = wx.Frame(parent=None, title='MyFrame')
panel = wx.Panel(framework)                                     # create a panel as a child of the frame
button = wx.Button(panel, label='Click Me', style=wx.BU_LEFT)   # create a button as a child of the panel
sizer = wx.BoxSizer(wx.HORIZONTAL)                              # create a horizontal sizer
sizer.Add(button, 0, wx.ALL, 5)                                 # add the button to the sizer with some padding
panel.SetSizer(sizer)                                           # set the sizer for the panel

def on_button_click(event):
    open_dlg = wx.ProgressDialog("My Viewer", "Copying File...", maximum=10, parent=framework)
    for ctr in range(11):
        open_dlg.Update(ctr, "Copying File...{}".format(ctr))
        time.sleep(1)

button.Bind(wx.EVT_BUTTON, on_button_click)

framework.Show()
application.MainLoop()