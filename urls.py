from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Mostly_static_pages.views.home', name='home'),
    # url(r'^Mostly_static_pages/', include('Mostly_static_pages.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'Mostly_static_pages.Practica5.views.home'),
    url(r'^contact/', 'Mostly_static_pages.Practica5.views.contact'),
    url(r'^about/', 'Mostly_static_pages.Practica5.views.about'),

)
