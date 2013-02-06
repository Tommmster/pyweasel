from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from pyweasel.views import interview, choose_interview

urlpatterns = patterns('',
	(r'^$',choose_interview),
	(r'^interviews/$',choose_interview),
	(r'^interview/(\w+)$',interview),
	(r'^interview/?$',interview),
    # Examples:
    # url(r'^$', 'pyweasel.views.home', name='home'),
    # url(r'^pyweasel/', include('pyweasel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
