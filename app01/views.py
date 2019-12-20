from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import time
import app01.my_mian as my

# Create your views here.

def index(request):
    # L = ['第一部分', '第二部分', '第三部分', '第四部分']
    # L = ['aaaa', 'bbbb', 'cccc', 'dddd']
    file_basedir = r'H:\Users\swt\Desktop\file'
    L=my.get_son_dir(file_basedir)
    return render(request, 'test.html', {'data': L})


@csrf_exempt
def test_file_upload(request):
    t1 = time.time()
    if request.method == "POST":
        file_obj = request.FILES.get("file_up")
        a1 = os.path.abspath('.')
        a2 = os.path.join(a1, 'static')
        a2 = os.path.join(a2, 'up_file')

        d = os.path.join(a2, file_obj.name)

        with open(d, "wb") as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
            t = time.time() - t1
        return HttpResponse('上传完毕,用时%s秒' % t)
    return render(request, 'test_file_upload.html')
