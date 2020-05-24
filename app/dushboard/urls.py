
from django.urls import path
from .views.base import Index
from .views.auth import Login,Logout,UpdateAdminStatus,AdminManage
from .views.video import ExternaVideo
urlpatterns = [
    path('', Index.as_view(),name='dushboard_index'),
    path('login', Login.as_view(), name='dushboard_login'),
    path('logout', Logout.as_view(), name='dushboard_logout'),
    path('admin', AdminManage.as_view(), name='dushboard_admin'),
    path('updateadminstatus', UpdateAdminStatus.as_view(), name='dushboard_updateadminstatus'),
    path('video/externa', ExternaVideo.as_view(), name='externa_video'),
]
