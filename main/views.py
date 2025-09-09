from django.shortcuts import render

# Create your views here.
def show_main(request):
    data = {
        'Aplikasi' : 'Lilywhite Store',
        'Name': 'Khayru RafamandaPrananta',
        'class': 'PBP F'
    }

    return render(request, "main.html", data)