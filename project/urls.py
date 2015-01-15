from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

from project.blog.views import ArticleDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'project.blog.views.home', name="home"),
    url(r'^article/(?P<pk>\d)/$', ArticleDetail.as_view(), name="article-detail"),
    url(r'^question/(?P<pk>\d)/$', QuestionDetail.as_view(), name="question-detail"),
    url(r'^why-you-need-help/$', TemplateView.as_view(template_name='why.html'), name="why"),
    url(r'^ask-dr-jay/$', 'project.blog.views.ask', name="ask"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name="contact"),

    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )

    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
