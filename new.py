import wx
import wikipedia
import wolframalpha
import pyttsx3
from subprocess import call

######## Java  component execution ####

call(["java", "-jar", "another.jar"])

######## PYTHON CODE STARTS HERE #####

# class to handle the GUI

class myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,  # properties if the frame
                          pos=wx.DefaultPosition,
                          size=wx.Size(450, 150),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
                                wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="D.R.E.I.F")

        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)  # box sizer for wx vertical
        label = wx.StaticText(panel, label='Hello I am D.R.E.I.F the Python Digital Assistant. How may I help you?')
        # puts label on panel

        my_sizer.Add(label, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()  # focus the text
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)  # Bind code that we wrote in earlier tutorial.
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        user_input = self.txt.GetValue()
        user_input.lower()
        try:
            # wolramalpha
            app_id = "RQ9ATP-PPA9RH8EY2"

            client = wolframalpha.Client(app_id)
            result = client.query(user_input)
            answer = next(result.results).text
            engine = pyttsx3.init()
            engine.say(answer)
            engine.runAndWait()
            print(answer)
            print()
            print()

        except:
            # wikipedia

            split = user_input.split(' ')
            join = ' '.join(split[2:])
            print(wikipedia.summary(join, sentences=5))
            print()
            print()


if __name__ == '__main__':
    app = wx.App(True)
    frame = myframe()
    app.MainLoop()
