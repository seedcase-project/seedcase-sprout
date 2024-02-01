from django.shortcuts import render

# Split views.py into multiple files is based on:
# https://simpleisbetterthancomplex.com/tutorial/2016/08/02/how-to-split-views-into-multiple-files.html
from .file_upload import file_upload
from .data_import import data_import


def home(request):
    return render(request, "home.html")
