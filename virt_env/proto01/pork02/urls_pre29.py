"""
URLs just for the 'pork02' app of the 'proto01' project
	r'^$'

	'r' => it's a regular epression!
	'^' => The beginning
	'$' => The end

"""

from django.conf.urls import url
from . import views

#Define the name space 'pork02'
app_name = 'pork02'

urlpatterns = [
	#/pork02/
	#calls "index" method in views.py
    #url(r'^$', views.index, name='index'), #The function views.py approach
    url(r'^$', views.IndexView.as_view(), name='index'), #the class views.py approach

	#/pork02/81030/
	#calls "supplier_detail" method in views.py passing numeric <supplier_id> as the argument (?P<>)
	#url(r'^(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'), #The function views.py approach
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='product_detail'), #the class views.py approach

	#/pork02/81030/favorite
	#passes the product_id to the "favorite" URL
	url(r'^(?P<product_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
