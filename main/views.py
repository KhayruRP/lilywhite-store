from django.shortcuts import render

# Create your views here.
def show_main(request):
    data = {
        'Aplikasi' : 'Lilywhite Store',
        'Name': 'Khayru RafamandaPrananta',
        'class': 'PBP F',
        'NPM' : '2406495893'
    }

    return render(request, "main.html", data)