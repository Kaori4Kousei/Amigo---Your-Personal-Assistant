def textAction(text):
    newText = ""
    firstQuoteInd = text.index("quote")
    lastQuoteInd =  text.rindex("end quote")
    print(firstQuoteInd)
    print(lastQuoteInd)
    print(text)

    
commandText = "Open google and search quote motivational end quote quote and play quote motivational quote end quote on youtube"
textAction(commandText)