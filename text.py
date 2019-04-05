def textAction(textF):
    textF = textF.lower().split()
    i=0
    j=0
    wordCount = len(textF)
    while i<wordCount:
        print(textF[i])
        if textF[i] == "search" or textF[i]=="check":
            i=i+1
            if(textF[i]=="for"):
                i=i+1
            forming = []
            while i<wordCount and textF[i]!="amigo":
                forming.append(textF[i])
                forming.append(" ")
                i=i+1
            print(''.join(forming)) #GOOGLE SEARCH
        elif textF[i]=="play":
            i=i+1
            forming1 = []
            while i<wordCount and textF[i]!="amigo":
                forming1.append(textF[i])
                forming1.append(" ")
                i=i+1
            print(''.join(forming1)) #PLAY
        elif textF[i] =="switch":
            i=i+1
            if(textF[i]=="to"):
                i=i+1
            forming2 =[]
            while i<wordCount and textF[i]!="amigo":
                forming2.append(textF[i])
                forming2.append(" ")
                i=i+1
            print(''.join(forming2)) #SWITCH
        i=i+1
textAction("check for machine learning amigo check for weather")