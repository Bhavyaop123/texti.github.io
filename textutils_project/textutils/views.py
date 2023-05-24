from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    num = 0

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)
    elif fullcaps == 'on':
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
            params = {'purpose': 'Changed To UPPERCASE', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)
    elif newlineremover == 'on':
        analyze = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyze = analyze + char
                params = {'purpose': 'Removed New Lines', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)
    elif extraspaceremover == 'on':
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyze = analyze + char
                params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)
    elif charactercounter == 'on':
        for char in djtext:
            num += 1
        analyze = f"Number of characters = {num}"
        params = {'purpose': 'Counted the number of Characters', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')