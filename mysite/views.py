from django.http import HttpResponse
from django.shortcuts import render, resolve_url

def index(request):
    return render(request, "index.html")
    # return HttpResponse("<h1>YOUR DADDY COMES HERE TO LEARN DJANGO , WILL MAKE UN UNPAID QUIKLY !</h1>")


def analyze(request):
    djutils = request.POST.get("text","default")
    analyze = request.POST.get("analyze" , "off")
    
    
    if (analyze == "Capitalizized"):
       
        analyzestr = djutils.upper()
        
        return render(request , "analyze.html" , {"RemovePunctuation":"Capitalized" , "djutils": analyzestr})
    
    elif analyze == "removepunctuation":
        puncuation = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        analyzestr = ""
        for char in djutils:
            if char not in puncuation:
                analyzestr = analyzestr + char
        return render(request , "analyze.html" , {"RemovePunctuation":"Remove Punctuation" , "djutils": analyzestr})
    
    elif analyze == "newlineremover":
        analyzestr = ""
        
        for char in djutils:
            if (char != "\n" and char!= "\r"):
                analyzestr = analyzestr + char
                
        
        return render(request , "analyze.html" , {"RemovePunctuation":"New line remover" , "djutils": analyzestr})
    
    elif analyze == "Spaceremover":
        analyzestr = ""
        for i,char in enumerate(djutils):
            if (char == " " and djutils[i+1]== " "):
                continue
            else :
                analyzestr = analyzestr + char
                

    
        return render(request , "analyze.html" , {"RemovePunctuation":"Space remover" , "djutils": analyzestr})

    elif analyze == "CharacterCount":
        analyzestr = len(djutils)
        return render(request , "analyze.html" , {"RemovePunctuation":"Character Count" , "djutils": analyzestr})
    else:
        return HttpResponse("Please Choose One Option")