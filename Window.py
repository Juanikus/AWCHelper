from tkinter import *
from DataFetcher import *
from Resources import *
from DataCache import DataCache


class Window:

    def __init__(self):
        self.initWindow()
        self.initComponents()
        self.ubicateComponents()

        self.dataFetcher = DataFetcher()
        self.dataCache = DataCache()
        self.retrieveUserName()

        self.rootWindow.mainloop()

    def retrieveUserName(self):
        name = self.dataCache.getSavedUserName()
        self.txtAnilistUserName.insert(0, name)

    def initWindow(self):
        self.rootWindow = Tk()
        self.rootWindow.title("Anilist Challenge Helper")
        self.rootWindow.geometry(WINDOWSIZE)
        self.rootWindow.resizable(False, False)

    def initComponents(self):
        self.lblAnilistUserName = CustomLabel(self.rootWindow, text="Anilist Username: ")
        self.txtAnilistUserName = Entry(self.rootWindow, width=ENTRYWIDTH)

        self.lblLink = CustomLabel(self.rootWindow, text="Anime Link: ")
        self.txtLink = Entry(self.rootWindow, width=ENTRYWIDTH)

        self.lblChallenge = CustomLabel(self.rootWindow, text="Challenge Text: ")
        self.txtChallenge = Entry(self.rootWindow, width=ENTRYWIDTH)

        self.actionPanel = Frame(self.rootWindow, width=RESULTWIDTH)

        self.btnBuild = Button(self.actionPanel, text="Generate Line", command=self.onGenerateClick, anchor=CENTER)
        self.txtResult = Text(self.actionPanel, width=50, height=10)
        self.txtResult.configure(state=DISABLED)

        self.rootWindow.iconbitmap(r'icon.ico')

    def ubicateComponents(self):
        self.lblAnilistUserName.grid(row=0, column=0)
        self.txtAnilistUserName.grid(row=0, column=1)
        self.lblLink.grid(row=1, column=0)
        self.txtLink.grid(row=1, column=1)
        self.lblChallenge.grid(row=2, column=0)
        self.txtChallenge.grid(row=2, column=1)
        self.actionPanel.grid(row=3, column=0, columnspan=2)

        self.btnBuild.grid(row=0, column=0, columnspan=2)
        self.txtResult.grid(row=1, column=0, columnspan=2)

    def onGenerateClick(self):
        resultado = ''
        try:
            userName = self.txtAnilistUserName.get()
            self.dataCache.saveUserName(userName)

            mediaURL = self.txtLink.get()
            mediaId = self.dataFetcher.getIdFromURL(mediaURL)

            challenge = self.txtChallenge.get()

            animeData = self.dataFetcher.runQuery(userName, mediaId)
            title = animeData[0]
            startDate = animeData[1]
            endDate = animeData[2]

            resultado = self.dataFetcher.getResponse(startDate, endDate, challenge, title, mediaURL)
        except Exception as e:
            resultado = e

        self.setResultText(resultado)

    def setResultText(self, text):
        self.txtResult.configure(state=NORMAL)

        self.txtResult.delete(1.0, END)
        self.txtResult.insert(END, text)

        self.txtResult.configure(state=DISABLED)


class CustomLabel(Label):

    def __init__(self, parent, text):
        Label.__init__(self, parent, text=text, width=LABELWIDTH, anchor=W, justify=LEFT)
