from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.student_dashboard),
    path('log_out', views.log_out),
    path('all_proposals', views.page_all_proposals),
    # CREATe  and update Project:
    path('new_create_proposal_page', views.new_create_proposal_page),
    path('new_proposal_created', views.new_proposal_created),
    path('create_wireframe_page/<int:proposal_id>', views.create_wireframe_page),
    path('create_wireframe_page/create_wireframe/prop/<int:proposal_id>', views.create_wireframe),
    path('create_wireframe_page/details/proposal/<int:proposal_id>', views.details_proposal),
    path('create_wireframe_page/details/proposal/send_to_instr/<int:proposal_id>', views.send_proposal),
    # Old:
    # path('create_proposal_page', views.create_prop_1),
    # path('create_proposal', views.create__sect_1),
    # path('update_s4_proposal/<int:proposal_id>', views.update_lastproposal_s4),
    # path('update_s5_proposal/<int:proposal_id>', views.update_lastproposal_s5),
    # Proposal Details:
    path('details/proposal/<int:proposal_id>', views.details_proposal),
    path('details/proposal/send_to_instr/<int:proposal_id>', views.send_proposal),
    # Create Feature:
    # path('create_feature', views.create_feature),
    # Delete buttons:
    path('delete/proposal/<int:proposal_id>', views.delete_proposal),
    path('delete/feature/<int:feature_id>', views.delete_feature),
    # Reviews:
    path('all_reviews', views.all_reviews),
    path('details/review/<reviews_id>', views.review_details),
    # Manage:
    path('manage', views.manage),
    # OLD
    # path('assign', views.assign),

    # New:
    path('help', views.help),
    path('projects', views.projects_page),


    # From SHERRY:
    path('assignfea/assign', views.assign),
    path('choose', views.choose_proj),
    path('assignfea/<int:id>', views.assign_feature),
    path('todo', views.todo),
    path('complete/<int:f_id>',views.compl_feature),

    # FROM MAX:
    path("remove/<int:id>", views.remove_logic)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)