from django.shortcuts import render

# Create your views here.
def lista_carrocel(request):
	carrocel = Carrocel.objects.all()
	return render(request, 'carrocel/lista_carrocel.html', {'carrocel': carrocel})