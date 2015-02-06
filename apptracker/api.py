from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Project, Issue, Label
from .serializers import ProjectSerializer, ProjectIssuesListSerializer, IssueDetailSerializer, LabelSerializer


###############################
# Projects
###############################
class ProjectListView(APIView):
    permission_classes = [
            permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):
    permission_classes = [
            permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request, project_pk):
        project = get_object_or_404(Project, pk=project_pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, project_pk):
        project = get_object_or_404(Project, pk=project_pk)
        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, project_pk):
        project = get_object_or_404(Project, pk=project_pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###############################
# Labels
###############################
class ProjectLabelsView(APIView):

    def get(self, request, project_pk):
        project = get_object_or_404(Project, pk=project_pk)
        labels = project.labels
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)

    def post(self, request, project_pk):
        project = get_object_or_404(Project, pk=project_pk)
        serializer = LabelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(project=project)
            labels = LabelSerializer(project.labels, many=True)
            return Response(labels.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelsView(APIView):

    def get(self, request, project_pk, label_pk):
        label = get_object_or_404(Label, pk=label_pk)
        serializer = LabelSerializer(label)
        return Response(serializer.data)

    def put(self, request, project_pk, label_pk):
        project = get_object_or_404(Project, pk=project_pk)
        label = get_object_or_404(Label, pk=label_pk, project=project)
        serializer = LabelSerializer(label, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_pk, label_pk):
        label = get_object_or_404(Label, pk=label_pk)
        label.delete()
        return Response(status=status.HTTP_200_OK)


###############################
# Issues
###############################
class ProjectIssuesListView(APIView):

    def get(self, request, project_pk):
        project = get_object_or_404(Project, pk=project_pk)
        serializer = ProjectIssuesListSerializer(project)
        return Response(serializer.data)

    def post(self, request, project_pk):
        project = get_object_or_404(Project, pk=project_pk)
        serializer = IssueDetailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner = request.user, project=project, reference=project.total_issue)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueDetailView(APIView):

    def get(self, request, project_pk, issue_reference):
        project = get_object_or_404(Project, pk=project_pk)
        issue = get_object_or_404(Issue, reference=issue_reference, project=project)
        serializer = IssueDetailSerializer(issue)
        return Response(serializer.data)

    def put(self, request, project_pk, issue_reference):
        project = get_object_or_404(Project, pk=project_pk)
        issue = get_object_or_404(Issue, reference=issue_reference, project=project)
        serializer = IssueDetailSerializer(issue, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, project_pk, issue_reference):
        project = get_object_or_404(Project, pk=project_pk)
        issue = get_object_or_404(Issue, reference=issue_reference, project=project)
        serializer = IssueDetailSerializer(issue, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_pk, issue_reference):
        project = get_object_or_404(Project, pk=project_pk)
        issue = get_object_or_404(Issue, reference=issue_reference, project=project)
        issue.delete()

        return Response(status=status.HTTP_200_OK)