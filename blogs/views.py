from django.http import HttpResponse
 
 
def index(request):
    return HttpResponse("Home")
 
 
def detail(request, pk):
    return HttpResponse("Post %s" % pk)
 
 
def create(request):
    return HttpResponse("Add New Post")
 
 
def update(request, pk):
    return HttpResponse("Edit Post %s" % pk)
 
 
def delete(request, pk):
    return HttpResponse("Delete Post %s" % pk)
