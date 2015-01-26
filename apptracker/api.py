from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Project, Issue
from .serializers import ProjectSerializer, ProjectIssuesListSerializer, IssueItemSerializer, IssueDetailSerializer


class ProjectListView(APIView):

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):

    def get(self, request, pk, format=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class ProjectIssuesListView(APIView):

    def get(self, request, pk, format=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectIssuesListSerializer(project)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = IssueDetailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(project=project)
            project.total_issue += 1
            project.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueDetailView(APIView):

    def get(self, request, project_pk, issue_pk, format=None):
        project = get_object_or_404(Project, pk=project_pk)
        issue = get_object_or_404(Issue, pk=issue_pk)
        serializer = IssueDetailSerializer(issue)
        return Response(serializer.data)

    def put(self, request, project_pk, issue_pk, format=None):
        project = get_object_or_404(Project, pk=project_pk)
        issue = get_object_or_404(Issue, pk=issue_pk)
        serializer = IssueDetailSerializer(issue, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, project_pk, issue_pk, format=None):
        project = get_object_or_404(Project, pk=project_pk)
        issue = get_object_or_404(Issue, pk=issue_pk)
        serializer = IssueDetailSerializer(issue, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)