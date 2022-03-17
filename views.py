from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from .EgyptianNationalId import *


def index(request: HttpRequest, id: str) -> JsonResponse:
    """
    Handle the request to the index page.
    Args:
        request (HttpRequest): The request object.
        id (str): The Natioal ID

    Returns:
        JsonResponse: The response object.
    """
    try:
        id: EgyptianNationalId = EgyptianNationalId(id)
    except:
        return JsonResponse({"error": "Invalid ID"}, status=400)
    return JsonResponse(id.fields)
