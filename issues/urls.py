from django.urls import path
from . import views

urlpatterns = [
    path('', views.IssueListView.as_view(), name='issue_index'),
    path('issues/create/', views.IssueCreateView.as_view(), name='issue_create'),
    path('issues/<int:pk>/', views.IssueDetailView.as_view(), name='issue_detail'),
    path('issues/<int:pk>/update/', views.IssueUpdateView.as_view(), name='issue_update'),
    path('issues/<int:pk>/delete/', views.IssueDeleteView.as_view(), name='issue_delete'),
    path('issues/import-csv/', views.ImportIssueCSVView.as_view(), name='issue_import'),
]
