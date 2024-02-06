import csv
from typing import IO, Dict

from django.core.files.uploadhandler import StopUpload
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from app.csv_reader import read_csv_file
from app.models import TableMetadata


def file_upload(request: HttpRequest, table_id: int) -> HttpResponse:
    """
    Method is called at url="file-upload/<int:table_id>". The table_id comes from the
    url. The table_id is used fetch the table_metadata from the database.
    - On GET requests, the file-upload page is rendered.
    - On POST requests, a csv file is submitted from the user. This file is validated
    and column metadata is persisted for the table.

    Args:
        request: the http request from the user/browser
        table_id: the table_id based

    Returns:
    """

    if request.method == "POST":
        return handle_form_submit_with_file(request, table_id)

    return render_file_upload_page(request, table_id, "")


def handle_form_submit_with_file(request: HttpRequest,
                                 table_id: int) -> HttpResponse | HttpResponseRedirect:
    """
    The post request should contain a CSV file, which is validated in this method.
    The method have two scenarios:
    - If the validation is successful, then we persist the column metadata and redirect
    to the next page in the flow
    - If the validation fails, an exception is raised StopUpload. The page file-upload
    page is re-rendered with the error message
    Args:
        request: http request from the user/browser
        table_id: the id of the table we are using

    Returns: A HttpResponseRedirect when validation is successful or HttpResponse when
    validation fails

    """
    try:
        validate_csv_and_save_columns(table_id, request.FILES)
    except StopUpload as upload_error:
        return render_file_upload_page(request, table_id, upload_error.args[0])

    return redirect("/edit-table-columns/" + str(table_id))


def render_file_upload_page(request: HttpRequest, table_id: int,
                            upload_error: str) -> HttpResponse:
    """
    Render file-upload page with an error if there is any

    Args:
        request: The http request
        table_id: The id of the table
        upload_error: The error message if there is any

    Returns:
        HttpResponse: A html page based on the file-upload.html template
    """
    table_metadata = TableMetadata.objects.get(pk=table_id)
    file_upload_data = {"table_name": table_metadata.name, "upload_error": upload_error}
    return render(request, "file-upload.html", file_upload_data)


def validate_csv_and_save_columns(table_id: int, files: Dict[str, IO]) -> None:
    """
    Validate the csv and persist column metadata if valid

    Args:
        table_id: The id of the table
        files: A dictionary of files where the csv is in the key "uploaded_file"
    """
    uploaded_file = files.get("uploaded_file", None)

    if not uploaded_file.name.endswith(".csv"):
        error_msg = "Unsupported file format: ." + uploaded_file.name.split(".")[-1]
        raise StopUpload(error_msg)

    try:
        df = read_csv_file(uploaded_file)
        table_meta = TableMetadata.objects.get(pk=table_id)
        table_meta.save_file_name(uploaded_file)
        table_meta.create_columns(df)
    except csv.Error as e:
        raise StopUpload("Unable to parse CSV file: " + e.args[0])
