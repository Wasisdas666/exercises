from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse

def http_response_view(request):
    return HttpResponse('<p>This is an HttpResponse example.</p>')

def json_response_view(request):
    data = {'message': 'This is a JsonResponse example.'}
    return JsonResponse(data)