from django.http import HttpResponse
from django.shortcuts import render


def hello( request ):

    return HttpResponse("こんにちは")


def test( request ):

    context = {
            'message' : '初めてのメッセージ',
            'content' : 'ようこそ、Djangoは楽しい！',
        }
    return render(request,'file.html',context)
    
def reg( request ):

    # breakpoint()
    print(request.GET["id"])
    print(request.GET["name"])
    return HttpResponse("登録します")
