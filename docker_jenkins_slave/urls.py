from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'docker_jenkins_slave.views.home', name='home'),
    url(r'^generate$', 'docker_jenkins_slave.views.generate', name='generate'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
