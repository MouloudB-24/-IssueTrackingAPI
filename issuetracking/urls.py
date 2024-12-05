"""
URL configuration for issuetracking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projects.views import ProjectIssuesView, ProjectIssueCommentsView, ProjectIssueCommentInstanceView, ProjectContributionsView, ProjectIssueInstanceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path("api/projects/<int:project_pk>/contributions/", ProjectContributionsView.as_view(), name="contributions"),
    path("api/projects/<int:project_pk>/contributions/<int:contribution_pk>/", ProjectContributionsView.as_view(), name="contribution-detail"),
    path("api/projects/<int:project_pk>/issues/", ProjectIssuesView.as_view(), name="issues"),
    path("api/projects/<int:project_pk>/issues/<int:issue_pk>/", ProjectIssueInstanceView.as_view(), name="issue-detail"),
    path("api/projects/<int:project_pk>/issues/<int:issue_pk>/comments/", ProjectIssueCommentsView.as_view(), name="comments"),
    path("api/projects/<int:project_pk>/issues/<int:issue_pk>/comments/<int:comment_pk>/", ProjectIssueCommentInstanceView.as_view(), name="comment-detail"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
