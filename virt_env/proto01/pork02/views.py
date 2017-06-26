"""#HttpResponse replaced by "render"
#Http404 replaced by "get_object_or_404"
from django.http import HttpResponse, Http404"""

'''#replaced by shortcuts.render
from django.template import loader'''
from django.shortcuts import render, get_object_or_404
from .models import Suppliers, Products

def index(request):
	#return HttpResponse("<h1>This is the Pork02 app Homepage.</h1>") #replaced by dynamic id approach

	all_suppliers = Suppliers.objects.all()
	all_products = Products.objects.all()
	#template = loader.get_template('pork02/index.html') #obsoleted by shortcuts.render
	#create dictionary
	context = {
		'all_suppliers': all_suppliers,
		'all_products': all_products
	}
	#return HttpResponse(template.render(context, request)) #obsoleted by shortcuts.render
	return render(request, 'pork02/index.html', context)
	'''
	#need to externalize the HTML portion to separate from python code
	html = ''
	for supp in all_suppliers:
		url = '/pork02/' + str(supp.id) + '/'
		html += '<a href="' + url + '">' + supp.supplier + '</a><br>'
	return HttpResponse(html)
	'''

def supplier_detail(request, supplier_id):
	#return HttpResponse("<h2>Details for supplier: " + str(supplier_id) + "</h2>")
	#Check the database if the ID exists or not first
	try:
		supp = Suppliers.objects.get(pk=supplier_id)
	except Suppliers.DoesNotExist:
		raise Http404("Supplier doe snot existo")
	#this calls details.html passing the "supp" variable
	return render(request, 'pork02/detail.html', {'supp':supp})

def product_detail(request, product_id):
	#Check the database if the ID exists or not first
	"""
	try:
		prod = Products.objects.get(pk=product_id)
	except Products.DoesNotExist:
		raise Http404("Product doe snot existo")
	"""
	prod = get_object_or_404 (Products, pk=product_id)
	#this calls details.html passing the "prod" variable
	return render(request, 'pork02/detail.html', {'prod':prod})

def favorite(request, product_id):
	#Get the specific Products object for the given product_id and assign to "prod"
	prod = get_object_or_404 (Products, pk=product_id)
	try:
		#Store the supplier prouct code that was selected by the user into "selected_prod" variable.
		#becaus ein my eversion that product ID was passed already I don't need to convert liek in the video.
		#selected_prod = prod.prod_code_supplier_set.get(pk=request.POST['prod_code_supplier'])
		selected_prod = prod.prod_code_supplier
	except(KeyError, Products.DoesNotExist):
		#If error then show the product detail page for this product along with the error.
		render(request, 'pork02/detail.html', {
			'prod':prod,
			'error_message': "You did not select a valid product."
		})
	else:
		#If no erro then update this specific product in the database and take the user back to the detail page
		prod.is_favorite = True
		prod.save()
		return render(request, 'pork02/detail.html', {'prod':prod})
