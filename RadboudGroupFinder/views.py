"""
views.py is for rendering html web pages
"""
from django.http import HttpResponse

HTML_STRING = """
<h1>Handled First URL route</h1>
"""

def home_view(request): 
    """
    Take in a request (Django sends requests by default)"
    Retrun HTML as a response (Chosen by us)
    """
    
    
    return HttpResponse(HTML_STRING)