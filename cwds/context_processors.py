def main_context(request):
	if request.user.is_authenticated:
		if request.user.user_type == 'agency':
			base_template = 'general/agency_dashboard.html'
		elif request.user.is_superuser:
			base_template = 'general/admin_dashboard.html'
		elif request.user.user_type == 'plant':
			base_template = 'general/plant_dashboard.html'
		else:
			base_template = 'general/user_dashboard.html'
	else:
		base_template = 'general/index.html'

	context ={
		'app_title':'CWDS',
		'base_template':base_template
	}
	return context