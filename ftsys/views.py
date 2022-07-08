from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def mainpage(request):
   if request.method == 'POST':
      Item.objects.create(sname=request.POST['Sname'],
         fname=request.POST['Fname'],
         mname=request.POST['Mname'],
         age=request.POST['Age'],
         add=request.POST['Address'],
         contact=request.POST['Contact'],
         disease=request.POST['Dropdown'],
         specifydisease=request.POST['Specify'],
         plan=request.POST['Dropdown2'],
         total=request.POST['Total'])
         
      return redirect ('/')
   storage=Item.objects.all()
   return render(request, 'mainpage.html',{'NewStorage':storage})

def page2 (request):
   if request.method == 'POST':
      ExercisePlan.objects.create(intensity=request.POST['intensity'],
         focus=request.POST['focus'])
   page2storage=ExercisePlan.objects.all()
   return render(request, 'page2.html',{'planstorage':page2storage})

def page3 (request):
   if request.method == 'POST':
      Program.objects.create(DietPlan=request.POST['diet'],
         Trainer=request.POST['trainer'],
         Duration=request.POST['date2'])
   page3storage=Program.objects.all()
   return render(request, 'page3.html',{'programstorage':page3storage})
   
def page4 (request):
   if request.method == 'POST':
      Products.objects.create(protein=request.POST['whey'],
         gymbags=request.POST['bag'],
         mat=request.POST['mat'],
         others=request.POST['RB'],
         Loss=request.POST['loss'],
         locker=request.POST['choice'])
   page4storage=Products.objects.all()
   return render(request, 'page4.html',{'productstorage':page4storage})

def page5 (request):
   storage=Products.objects.all()
   return render(request, 'page5.html',{'productstorage':storage})

def removepage (request, id):
   deleteentry=Products.objects.get(productID=id)
   deleteentry.delete()
   return render(request, 'mainpage.html',{'productstorage':deleteentry})

def edit(request, id):
	item = Item.objects.get(id=id)
	form = Item(instance=item)
	if request.method == 'POST':
		form = Item(request.POST, instance = item)
		if form.is_valid():
			form.save()
			return render(request, 'table.html')

	return render(request, 'edit.html', {'form':form})