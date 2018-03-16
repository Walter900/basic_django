from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect


# Create your views here.

def index(request):
    return render(request,'booktest/index.html')

def getTest1(request):
    return render(request,'booktest/get1.html')

def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {
               'a': a1,
               'b': b1,
               'c': c1
    }
    return render(request,'booktest/get2.html',context)

def post1(request):
    return render(request, 'booktest/post1.html')

def post2(request):
    uname  = request.POST['uname']
    message = request.POST['message']
    context = {
            "username" : uname,
            "message"   : message
    }
    return render(request,'booktest/post2.html',context)

def cookietest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])

    #response.set_cookie('t1','abd')
    return response

def redTest1(request):
    return HttpResponseRedirect('/booktest/redTest2')
def redTest2(request):
    return HttpResponse('RedirectPage')

def session1(request):
    uname = request.session.get('username','None')
    context = {'uname':uname}
    return render(request, 'booktest/session1.html',context)

def session2(request):
    return render(request,'booktest/session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    request.session['username'] = uname
    return redirect('/booktest/session1/')

def session3(request):
    del request.session['username']
    return redirect('/booktest/session1/')



def verifycode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random

    #background
    bgColor = (random.randrange(50,100),random.randrange(50,100),random.randrange(50,100))

    #hight and length
    width = 100
    height = 25

    #create a canvas
    image = Image.new('RGB',(width,height),bgColor)

    #
    #font = ImageFont.truetype('FreeMono.ttf',24)
    #create a pen
    draw = ImageDraw.Draw(image)

    #create a text content
    text = '0123'
    global textTemp
    textTemp = ''
    #create char
    for i in range(4):
        textTemp1 = text[random.randrange(0, len(text))]
        textTemp += textTemp1
        draw.text((i*25,0) ,
                  #text[random.randrange(0,len(text))]
                  textTemp1 ,
                  (255,255,255),
                  )
    request.session['code']=textTemp
    #draw.text((0,0),text,(255,255,255))

    #save
    from io import BytesIO as StringIO
    buf = StringIO()
    image.save(buf,'png')

    #output to clinet

    return HttpResponse(buf.getvalue(),'image/png')


def verifyTest1(request):
    return render(request, 'booktest/verifyTest1.html')

def verifyTest2(request):
       code = request.POST['code']
       if( code == textTemp ):
           return HttpResponse('You got it')
       return HttpResponse('False')


