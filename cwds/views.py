from django.shortcuts import render


def handler500(request):
    
    context = {
        'title' : "Error 500",
        "body_class":"inner error",
        "short_description" : "We're sorry! The server encountered an internal error!!!",
    }
    template = "errors/500.html"
    response = render(request,template,context)
    
    response.status_code = 500
    return response


def handler404(request):
    
    context = {
        'title' : "Error 404",
        "body_class":"inner error",
        "short_description" : "It seems we can't find what you're looking for!!!",
    }
    template = "errors/404.html"
    response = render(request,template,context)
    
    response.status_code = 404
    return response


def handler403(request):
    
    context = {
        'title' : "Error 403",
        "body_class":"inner error",
        "short_description" : "You're not authorized to view this page.",
    }
    template = "errors/403.html"
    response = render(request,template,context)
    
    response.status_code = 403
    return response


def handler400(request):
    
    context = {
        'title' : "Error 400",
        "body_class":"inner error",
        "short_description" : "Your browser sent a request that this server could not understand.",
    }
    template = "errors/400.html"
    response = render(request,template,context)
    
    response.status_code = 400
    return response
