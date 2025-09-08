from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406348433',
        'name': 'Naomyscha Attalie Maza',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)