from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Placeholder to later display all the list of blogs..."
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blogs."
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response = "Placeholder to display blog {}.".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "Placeholder to edit blog {}.".format(number)
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')