from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', RedirectView.as_view(url='/admin/')),
	(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('ore.views',
	(r'^dipendenti/', 'list_dipendenti'),
	)