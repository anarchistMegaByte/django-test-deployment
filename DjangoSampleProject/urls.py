"""DjangoSampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dmWebSite.views import saveUserInfo,saveUserEmail,saveContactUsInfo,saveProjectDetails, get_cancer_results, start_training, train_clev, predict_clev

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user_info/', saveUserInfo),
    url(r'^user_email/', saveUserEmail),
    url(r'^contact_us/', saveContactUsInfo),
    url(r'^submit_project_details/', saveProjectDetails),

    url(r'^get_cancer_results/', get_cancer_results),
    url(r'^start_training/', start_training),

    url(r'^train_clev/', train_clev),
    url(r'^pred_clev/', predict_clev)
]
