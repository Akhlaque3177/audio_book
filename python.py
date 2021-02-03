import pyttsx3
import PyPDF2

data = open("Akhlaque.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(data)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()