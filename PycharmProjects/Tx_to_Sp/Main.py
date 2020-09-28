import pyttsx3
import PyPDF2
from tkinter import filedialog
from tkinter import *


root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("pdf files", "*.pdf"),("all files", "*.*")))
print(root.filename)


book = open(root.filename, "rb")
pdfReader = PyPDF2.PdfFileReader(book)
speaker = pyttsx3.init()

page_location = int(input("Enter page number: "))

page = pdfReader.getPage(page_location)
text = page.extractText()
new_rate = 125
speaker.setProperty("rate", new_rate)
speaker.say(text)
speaker.runAndWait()