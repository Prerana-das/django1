from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

def votes_index(request):

    fruits=['apple','banana','orange']
    names=[
            {'firstname':'Peru','lastname':'Das'},
            {'firstname': 'Megh', 'lastname': 'Megh'},
        ]  ##name er modde dictionary
    context = {
        'fruits': fruits,
        'names': names
    }
    #context ta dictionary ###obj

    #template = loader.get_template('index.html')
    #response = template.render(request=request, context=context)   ###shortcut of those three lines ## loader use kore
    #return HttpResponse(response)

    return render(request,'index.html',context)  ##reder use kore data view

    #return HttpResponse("<h1>This is the response coming from votes appliacation</h1>") #html file chara view
    #return HttpResponse(template.render(request=request))

def votes_next(request):
    return HttpResponse('hkj')
