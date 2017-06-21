"""
URLs just for the 'pork02' app of the 'proto01' project
	r'^$'

	'r' => it's a regular epression!
	'^' => The beginning
	'$' => The end

"""

from django.conf.urls import url
from . import views

urlpatterns = [
	#/pork02/
	#calls "index" method in views.py
    url(r'^$', views.index, name='index'),

	#/pork02/1/
	#calls "supplier_detail" method in views.py passing numeric <supplier_id> as the argument (?P<>)
	url(r'^(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'),
]
