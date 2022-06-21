from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import os
import subprocess



# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def demoPost(request):
    res = ""
    if request.method == 'POST': 
        title = request.POST.get('title')
        # list_files = os.system("javac C:/Users/TEJAS/Desktop/Demo/Main.java")
        # output = os.system(r"java -classpath C:\Users\TEJAS\Desktop\Demo Main")
        # res = output


        className = title.split('public class', maxsplit=1)[-1]\
               .split(maxsplit=1)[0]

        # old_file = r"C:/Users/TEJAS/Desktop/tutorials/django-tutorial/rest-api/demo/java/" + oldfile
        # os.rename(old_file, new_file)
        # os.remove(old_file)

        # new_file = r"C:/Users/TEJAS/Desktop/tutorials/django-tutorial/rest-api/demo/java/" + className + ".java"
        new_file = r"/app/java/" + className + ".java"

        java_file = open(new_file, "w")
        java_file.write(title)
        java_file.close()


        compile_java = subprocess.getoutput(r"javac " + new_file)
        res = compile_java

        if(compile_java == ""):
            # run_java = subprocess.getoutput(r"java -classpath C:/Users/TEJAS/Desktop/tutorials/django-tutorial/rest-api/demo/java/ " + className)
            run_java = subprocess.getoutput(r"java -classpath /app/java/ " + className)
            new_file = open("/app/java/main.txt", "w")
            new_file.write(run_java)
            new_file.close()
            print(run_java)
            
            res = run_java

            working_directory = r"/app/java"
            retain_file = [className + ".java", className + ".class"]
            os.chdir(working_directory)
            for item in os.listdir(os.getcwd()):
                if item not in retain_file:
                    os.remove(item)


        
    return JsonResponse({"Result": res})

