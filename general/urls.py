from django.conf.urls import url
import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^about/$', views.about, name='about'),
		url(r'^admin-dashboard/$', views.admin_dashboard, name='admin_dashboard'),
		url(r'^agency-dashboard/$', views.agency_dashboard, name='agency_dashboard'),
		url(r'^plant-dashboard/$', views.plant_dashboard, name='plant_dashboard'),
		url(r'^user-dashboard/$', views.user_dashboard, name='user_dashboard'),
		
		url(r'^agency-confirm/$', views.agency_confirm, name='agency_confirm'),
		url(r'^plant-confirm/$', views.plant_confirm, name='plant_confirm'),
		url(r'^user-confirm/$', views.user_confirm, name='user_confirm'),

		url(r'^mailbox/$', views.mailbox, name='mailbox'),
		url(r'^create-mail/$', views.create_mail, name='create_mail'),
		url(r'^sent-mail/$', views.sent_mail, name='sent_mail'),
		url(r'^received-mail/$', views.received_mail, name='received_mail'),
		url(r'^inbox-deleted/(?P<pk>.*)/$', views.inbox_deleted, name='inbox_deleted'),
		url(r'^sentitems_deleted/(?P<pk>.*)/$', views.sentitems_deleted, name='sentitems_deleted'),

		url(r'^create-product/$', views.create_product, name='create_product'),
		url(r'^edit-product/(?P<pk>.*)/$', views.edit_product, name='edit_product'),
		url(r'^view-product/(?P<pk>.*)/$', views.view_product, name='view_product'),
		url(r'^view-products/$', views.view_products, name='view_products'),
		url(r'^delete-product/(?P<pk>.*)/$', views.delete_product, name='delete_product'),

		url(r'^create-order/(?P<product_id>.*)/$', views.create_order, name='create_order'),
		url(r'^view-order/(?P<pk>.*)/$', views.view_order, name='view_order'),
		url(r'^view-orders/$', views.view_orders, name='view_orders'),
		url(r'^change-order-status/(?P<pk>.*)/$', views.change_order_status, name='change_order_status'),
		url(r'^delete-order/(?P<pk>.*)/$', views.delete_order, name='delete_order'),

		url(r'^create-contact/$', views.create_contact, name='create_contact'),
		url(r'^create-donation/$', views.create_donation, name='create_donation'),

		url(r'^view-plant-requests/$', views.view_plant_requests, name='view_plant_requests'),
		url(r'^complete-plant-request/(?P<pk>.*)/$', views.complete_plant_request, name='complete_plant_request'),
		url(r'^select-plant/(?P<plant_id>.*)/$', views.select_plant, name='select_plant'),
		url(r'^request-plant/$', views.request_plant, name='request_plant'),
		url(r'^request_plant_confirm/(?P<plant_id>.*)/$', views.request_plant_confirm, name='request_plant_confirm'),
		url(r'^remove-plant/(?P<pk>.*)/$', views.removeplant, name='removeplant'),

		url(r'^view-agency-request/$', views.view_agency_request, name='view_agency_request'),
		url(r'^conform-agency-user/(?P<pk>.*)/$', views.conform_agency_user, name='conform_agency_user'),
		url(r'^select-agency/(?P<agency_id>.*)/$', views.select_agency, name='select_agency'),
		url(r'^request-agency/$', views.request_agency, name='request_agency'),
		url(r'^request_agency_confirm/(?P<agency_id>.*)/$', views.request_agency_confirm, name='request_agency_confirm'),
		url(r'^remove-agency/(?P<pk>.*)/$', views.removeagency, name='removeagency'),
	]