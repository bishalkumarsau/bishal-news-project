from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def moviesInfo(request):
    head_msg='Latest Movies information'
    msg1='Susanth Singh Rajput suside'
    msg2='Lockdown impact in Film industry'
    msg3='Savyachi now oliwood sonu soud'
    my_dict={'head_msg':head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsInfo(request):
    head_msg='Latest Sports information'
    msg1='IPL stop dut to covid-19'
    msg2='sachin is going to take bharatratna'
    msg3='Pack cricket plares tested covid positives'
    my_dict={'head_msg':head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def politicsInfo(request):
    head_msg='Latest politicss information'
    msg1='China atack in LOC'
    msg2='Lockdown impact in Film industr'
    msg3='Savyachi now oliwood sonu soud'
    my_dict={'head_msg':head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
