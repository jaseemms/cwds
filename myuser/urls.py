from django.conf.urls import url
import views

urlpatterns = [
	url(r'^edit-admin/(?P<pk>.*)/$', views.edit_admin, name='edit_admin'),
	url(r'^view-admin/(?P<pk>.*)/$', views.view_admin, name='view_admin'),

	url(r'^create-agency/$', views.create_agency, name='create_agency'),
	url(r'^edit-agency/(?P<pk>.*)/$', views.edit_agency, name='edit_agency'),
	url(r'^view-agency/(?P<pk>.*)/$', views.view_agency, name='view_agency'),
	url(r'^view-agencies/$', views.view_agencies, name='view_agencies'),

	url(r'^create-user/$', views.create_user, name='create_user'),
	url(r'^edit-user/(?P<pk>.*)/$', views.edit_user, name='edit_user'),
	url(r'^view-user/(?P<pk>.*)/$', views.view_user, name='view_user'),
	url(r'^view-users/$', views.view_users, name='view_users'),

	url(r'^create-plant/$', views.create_plant, name='create_plant'),
	url(r'^edit-plant/(?P<pk>.*)/$', views.edit_plant, name='edit_plant'),
	url(r'^view-plant/(?P<pk>.*)/$', views.view_plant, name='view_plant'),
	url(r'^view_plants/$', views.view_plants, name='view_plants'),

	url(r'^create-location/$', views.create_location, name='create_location'),
	url(r'^edit-location/(?P<pk>.*)/$', views.edit_location, name='edit_location'),
	url(r'^view-locations/$', views.view_locations, name='view_locations'),
	url(r'^delete-location/(?P<pk>.*)/$', views.delete_location, name='delete_location'),

	url(r'^verification/(?P<pk>.*)/$', views.verification, name='verification'),
	
	url(r'^agency-limit/(?P<pk>.*)/$', views.agency_limit, name='agency_limit'),
	url(r'^agency-limits/$', views.agency_limits, name='agency_limits'),
]