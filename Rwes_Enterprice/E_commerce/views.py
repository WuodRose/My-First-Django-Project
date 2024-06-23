from django.shortcuts import render
from django.http import HttpResponse

def E_commerce(request):
    return HttpResponse("""
    <html>
    <head>
        <title>mike Django project</title>
        <style>
            body {
                background-color: purple;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }
            h1 {
                font-family: Arial;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Rwes Enterprice Website</h1>
    </body>
    </html>
    """)
