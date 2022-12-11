from functools import wraps
from django.core.exceptions import PermissionDenied
from urlparse import urlparse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import logout


def check_group(group_list):
	def _check_group(view_func):
		@wraps(view_func)
		def wrapper(request,*args,**kwargs):

			try:
				user_type = request.user.user_type
			except:
				user_type = None

			if request.user.is_superuser:

				user_type = 'admin'
			print user_type
			print group_list
			if user_type in group_list:

				return view_func(request, *args, **kwargs)

			else:
				raise PermissionDenied

		return wrapper
		
	return _check_group


def check_user(url_value,user_value):
	def _check_user(view_func):
		@wraps(view_func)
		def wrapper(request,*args,**kwargs):
			try:
				url = urlparse(request.META.get('HTTP_REFERER')).path

			except:

				url = None

			try:
				user_type = request.user.user_type
			except:
				user_type = None

			if request.user.is_superuser:
				user_type ='admin'

			print url
			print url_value
			print user_type
			print user_value

			if not user_type == user_value:
				if url == url_value:
					logout(request)
					return HttpResponseRedirect(url+'?error=error')

				else:
					return view_func(request, *args, **kwargs)
			else:
				return view_func(request, *args, **kwargs)

		return wrapper
		
	return _check_user