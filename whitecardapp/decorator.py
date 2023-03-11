from django.shortcuts import redirect, HttpResponse


def Admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.all().exists():
            group = request.user.groups.all()[0].name
        
        if group == "system_admin":
            return redirect("system_admin")
        
        if group == "RTO":
            return redirect("rto")
        
        if group == "Ration":
            return redirect("ration")
        
        if group == "voter":
            return redirect("voter")
        
        if group == "IT_return":
            return redirect("it_return")

        else:
            return view_func(request,*args,**kwargs)
        
    return wrapper_func