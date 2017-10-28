# -*- coding: utf-8 -*-
# PROJECT INITITATED BY : VASANTHA KUMAR
# E-MAIL                : VASANTHFRIEND.RAJU@GMAIL.COM

# imports necessary packages
from Tkinter import *
from ScrolledText import ScrolledText
from tkFileDialog import askopenfilename, asksaveasfile
from ttk import *
from tkMessageBox import *

import ctypes
import Tkinter as tki
import tkMessageBox

# imports developer library
from UnicodeMaps import *

# assigns default data
REF_ROW_COUNT = 1080.0
REF_COL_COUNT = 1920.0
FIRST_COL_X = 50.0
FIRST_COL_Y = 70.0
COL_INC = 350
ROW_INC = 50

# function creates a pop up
def messageShow(title, msg):
    tkMessageBox.showinfo(title, msg)
    return None

def ShowUnicodeHelp(langFlag, textout):    
    if langFlag not in [TAMIL_FLAG, MALAYALAM_FLAG]:
        textout.delete('1.0', END)
        textout.insert(INSERT, "Please choose the language.")
    else:
        messageShow('Unicode Help', unicode_help[langFlag])

    return None
        
# function to design GUI tab
def Design_Tab():

    textExecutionInput = Label(tab,text="English Text",font=("Arial", 10, "bold"))
    textExecutionInput.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(0*ROW_INC))/REF_ROW_COUNT)*b)

    textExecutionOutput = Label(tab,text="Unicode",font=("Arial", 10, "bold"))
    textExecutionOutput.place(x=((FIRST_COL_Y+(2.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(0*ROW_INC))/REF_ROW_COUNT)*b)

    buttonHelp = Button(tab, text='Unicode Help', width="15",command=lambda: ShowUnicodeHelp(ChosenLanguage.get(), textOutputSection))
    buttonHelp.place(x=((FIRST_COL_Y+(1*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(0*ROW_INC))/REF_ROW_COUNT)*b)
    
    ChosenLanguage = IntVar()

    rbTamil = Radiobutton(tab, text="Tamil",  variable=ChosenLanguage, value=TAMIL_FLAG,)
                          #command=lambda: ChangeTab(TAMIL_FLAG))
    rbTamil.place(x=((FIRST_COL_Y+(1.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(0*ROW_INC))/REF_ROW_COUNT)*b)

    rbMalayalam = Radiobutton(tab, text="Malayalam", variable=ChosenLanguage, value=MALAYALAM_FLAG,)
                            #command=lambda: ChangeTab(MALAYALAM_FLAG))
    rbMalayalam.place(x=((FIRST_COL_Y+(2.0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(0*ROW_INC))/REF_ROW_COUNT)*b)

    ChosenLanguage.set(-1)

    buttonSaveCodeasKal = Button(tab, text='Save English text as .txt file', width="25",command=lambda: SaveInputasText(textCommandSection))
    buttonSaveCodeasKal.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)

    buttonConvertToUnicode = Button(tab, text='Convert Code to Unicode', width="25",command=lambda: ConvertToUnicode(textCommandSection,
                                                                                                                     ChosenLanguage.get(), textOutputSection ))
    buttonConvertToUnicode.place(x=((FIRST_COL_Y+(1*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)
    
    buttonClear = Button(tab, text='Clear', width="6",command=lambda: ClearCommands(textCommandSection, textOutputSection))
    buttonClear.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)

    buttonOutputasTxt = Button(tab, text='Save Unicode text as .txt file', width="25",command=lambda: SaveOutputasText(textOutputSection))
    buttonOutputasTxt.place(x=((FIRST_COL_Y+(2.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)

    
    textCommandSection = ScrolledText(tab, undo=True, width=a/21, height=b/30)
    textCommandSection['font'] = ('consolas', '12')
    textCommandSection.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(2*ROW_INC))/REF_ROW_COUNT)*b)

    textOutputSection = ScrolledText(tab, undo=True, width=a/21, height=b/30)
    textOutputSection['font'] = ('consolas', '12')
    textOutputSection.place(x=((FIRST_COL_Y+(2.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(2*ROW_INC))/REF_ROW_COUNT)*b)

    buttonAbout = Button(tab, text='About', width="10",command=lambda: messageShow('Info', 'vasanthfriend.raju@gmail.com'))
    buttonAbout.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(16*ROW_INC))/REF_ROW_COUNT)*b)

    textCommandSection.focus()
    
    return None

# function to save english text as .txt file
def SaveInputasText(textCommand):
    
    f = asksaveasfile(mode='w', title='Save English Text as...', initialfile='english_text.txt', filetypes=[('Save as', '.txt')])
    
    if f is None: 
        return None

    text2save = textCommand.get(1.0, END)
    f.write(text2save.encode('utf-8'))
    f.close()     

    return None

# function to save unicode text as .txt file
def SaveOutputasText(textOutput):
    
    f = asksaveasfile(mode='w', title='Save Unicode Text as...', initialfile='unicode_text.txt', filetypes=[('Save as', '.txt')])
    
    if f is None: 
        return None

    text2save = textOutput.get(1.0, END)
    f.write(text2save.encode('utf-8'))
    f.close()
    
    return None

# function to be called convert english text to unicode
# and fills the corresponding text box
def ConvertToUnicode(textval, langFlag, textout):
    if langFlag not in [TAMIL_FLAG, MALAYALAM_FLAG]:
        textout.delete('1.0', END)
        textout.insert(INSERT, "Please choose the language.")
        return None

    UserCode = textval.get(1.0, END)
    textout.delete('1.0', END)
    
    fin = open('usercodeEnglish.txt', 'w')
    fin.write(UserCode.encode('utf8'))
    fin.close()

    unicLines = []
    with open('usercodeEnglish.txt', 'r') as fin:
        for lineE in fin:
            unicLine = unicodeConversion(lineE, langFlag)
            unicLines.append(unicLine)

    fin = open('usercode_0.txt', 'w')
    for line in unicLines:        
        fin.write(line.encode('utf8'))        
    fin.close()

    with open('usercode_0.txt', 'r') as fin:
        for line in fin:            
            textout.insert(INSERT, line)

    return None              

# function to separate letters and non-letters
# in each line of English text
# and finds matched Unicode letters and returns
def unicodeConversion(line , langFlag):
    origline = line
    
    if line[0] in letters:
        first_letter = 1
    else:
        first_letter = 0
        
    total_read = 0
    initial_length = len(line)

    stringl = []
    othersl = []
    elecount = 0
    line = list(line)
    dict1 = {}

    while total_read < initial_length:    
        element = line[0]
        if element in letters:
            if len(othersl) != 0:
                others = "".join(othersl)
                dict1[elecount] = others
                elecount += 1
                othersl = []
            
            stringl.append(line[0])
            total_read += 1
        else:
            if len(stringl) != 0:
                string = "".join(stringl)
                dict1[elecount] = string
                elecount += 1
                stringl = []
            
            othersl.append(line[0])
            total_read += 1

        del line[0]

    if len(stringl) != 0:
        string = "".join(stringl)
        dict1[elecount] = string
        elecount += 1

    if len(othersl) != 0:
        others = "".join(othersl)
        dict1[elecount] = others
        elecount += 1

    if first_letter == 1:
        words = [i for i in dict1.keys() if i%2 == 0]
        nonwords = [i for i in dict1.keys() if i%2 != 0]
    else:
        nonwords = [i for i in dict1.keys() if i%2 == 0]
        words = [i for i in dict1.keys() if i%2 != 0]

    linelist = []
    nonwordElementsCount = len(nonwords)
    nonwordsAppendCount = 0

    for index in words:
        passstring = dict1[index]    
        unicw = unicodefind(passstring, langFlag)
        if first_letter == 1:
            linelist.append(unicw)
            if nonwordsAppendCount < nonwordElementsCount:
                linelist.append(dict1[nonwords[nonwordsAppendCount]])
                nonwordsAppendCount += 1
        else:
            if nonwordsAppendCount < nonwordElementsCount:
                linelist.append(dict1[nonwords[nonwordsAppendCount]])
                nonwordsAppendCount += 1
            linelist.append(unicw)        
    
    if nonwordsAppendCount < len(nonwords):
        linelist.append(dict1[nonwords[-1]])

    unicline = "".join(linelist)

    return unicline

# function to find matched unicode string for a string
def unicodefind(stringo, langFlag):
    origstring = stringo
    removedCharCount = 0
    processedCharCount = 0
    unicl = []
    unknownString = -1
    modstring = stringo

    while processedCharCount < len(origstring):
        if stringo in unicode_map[langFlag].keys():            
            unknownString = 0            
        else:
            if removedCharCount == len(modstring):
                unknownString = 1                
            else:
                strl = list(stringo)
                del strl[-1]
                stringo = "".join(strl)
                removedCharCount += 1

        if unknownString == 1:
            unicl.append(modstring)
            unknownString = -1
            processedCharCount = len(origstring)
            
            
        elif unknownString == 0:
            unicl.append(unicode_map[langFlag][stringo])
            unknownString = -1
            processedCharCount += len(stringo)
            removedCharCount = 0

            strl = list(origstring)
            del strl[0:processedCharCount]
            stringo = "".join(strl)
            modstring = stringo
    
    unic = "".join(unicl)

    return unic        

# function to clear the texts
def ClearCommands(textval, textout):    
    textval.delete('1.0', END)
    textout.delete('1.0', END)
    
    return None


# main call
if __name__ == "__main__":

    root = Tk('ProjectUnicodeWriter')

    user32 = ctypes.windll.user32
    a, b = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        
    note = Notebook(root,width=a,height=b)

    tab = Frame(note)    
    note.add(tab, text = "English -> Tamil, Malayalam Unicode Writer :: RollupStudios")
    
    Tab_Data = Design_Tab()

    note.pack()
    root.mainloop()


# END OF UNICODEWRITER.PY FILE
