import pyttsx3
import PyPDF2
print("Please make sure the book you want to read is in the same folder as this application")
print("Please answer the following")
usr = input("1. What's your name: ")
speaker = pyttsx3.init()
bookname=input("2. What book would you like me to read for you? enter the name and the extension \"eg: Study Guide.pdf\", enter your answer:  ")

book = open(bookname, 'rb')
speaker.say("Hi" + usr + "...Please listen carefully, as I am about to read" + bookname + "for you...")
Reading= PyPDF2.PdfFileReader(book)
pages = Reading.numPages # Reads the page numbers
for i in range(int(input("3. From what page would you like to read? "))-1,1+int(input("4. To what page would you like to read? "))):
    page = Reading.getPage(i)
    words = page.extractText()
    speaker.say(words) # Just testing the voice command that will be reading the book
    speaker.runAndWait()