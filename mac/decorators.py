
from django.shortcuts import HttpResponseRedirect

def chek_for_login(url):
    def decorator(func):
        def _is_login(request,*args,**kwargs):

            if request.user.is_authenticated:
                return HttpResponseRedirect(url)
            else:
                return func(request,*args,**kwargs)
        return _is_login
    return decorator
