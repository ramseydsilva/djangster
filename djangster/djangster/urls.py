from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'djangster.views.home', name='home'),
    url(r'^create-site/$', 'djangster.views.create_site', name='create_site'),
    url(r'^create-site/success/$', 'djangster.views.create_site_success', name='create_site_success'),
    url(r'^about/$', 'djangster.views.about', name='about'),
    url(r'^features/$', 'djangster.views.features', name='features'),
    url(r'^price-list/$', 'djangster.views.price_list', name='price_list'),
    url(r'^work/$', 'djangster.views.work', name='work'),

    # user views
    url(r'^logout/$', 'djangster.user_views.logout_view', name='logout'),
    url(r'^login/$', 'djangster.user_views.login_view', name='login'),
    url(r'^register/$', 'djangster.user_views.register_view', name='register'),
    url(r'^get_login_buttons/$', 'djangster.user_views.get_login_buttons', name='get_login_buttons'),

    # url(r'^djangster/', include('djangster.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
