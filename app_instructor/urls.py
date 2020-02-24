from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.instructor_dashboard),
    path('all_proposals', views.all_proposals),
    path('proposal/<int:p_id>', views.details_prop),
    path('save_review/<int:proposal_id>', views.save_review),
    path('approved/<int:proposal_id>', views.prop_approved),
    path('not_approved/<int:proposal_id>', views.prop_not_approved),
    path('reviews', views.reviews_page),
    path('details/review/<int:reviews_id>', views.details_reviews),

    path('log_out', views.log_out),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)