# from .import views
# from django.urls import path

# urlpatterns = [
#     path ("",views.home, name="home")

# ]

from .views import *
from django.urls import path

urlpatterns = [
    path ("",home),
    path ("view/<int:prod_id>",viewfn),
    # path ("new/",newfn),
    path ("categories/<int:c_id>", categorypage),
    # path ("register/",Formfn),
    path ("result/",Resultfn),

    path ("reg/", regfn),
    path("login/",Logfn),
    path("log/",logoutfn),
    path("addcat/",addCategory),
    path("addproduct/",addProduct),
    path("editproduct/<int:p_id>",editProduct),
    path("delete/<int:p_id>",deleteProduct),
    path("addprofile/",addProfile),
    path("profilepage/",profile),


]