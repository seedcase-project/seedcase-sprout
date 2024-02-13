"""Module with all views."""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Split views.py into multiple files is based on:
# https://simpleisbetterthancomplex.com/tutorial/2016/08/02/how-to-split-views-into-multiple-files.html
from .data_import import data_import  # noqa: F401
from .file_upload import file_upload  # noqa: F401


def home(request: HttpRequest) -> HttpResponse:
    """Renders the frontpage based on home.html.

    Args:
        request: The HttpRequest from the user

    Returns:
        HttpResponse: The html content based on the home.html template
    """
    return render(request, "home.html")
