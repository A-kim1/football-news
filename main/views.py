from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406429563',
        'name': 'Amar Hakim',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
