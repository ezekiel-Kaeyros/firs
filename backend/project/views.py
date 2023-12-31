from .forms import NewProject
from rest_framework.response import Response
from django.http import JsonResponse
from .models import projetModel
from rest_framework.decorators import api_view
from rest_framework import status
import time
import os

# Create your views here.


def get_list(self):
    projects = list(projetModel.objects.all().values())
    return JsonResponse(
        {
            "projects": projects,
        },
    )


@api_view(["GET"])
def get(request, _id):
    if request.method == "GET":
        project = projetModel.objects.get(id=_id)
        return JsonResponse({
            "id": project.id,
            "title": project.title,
            "duration": project.duration,
            "description": project.description,
            "logoUrl": str(project.logoUrl),
            "photoUrl": str(project.photoUrl),
            "sponsorLogoUrl": str(project.sponsorLogoUrl),
            "createdAt": project.createdAt,
            "editeAt": project.editeAt
        })


@api_view(["POST"])
def create(request):
    if request.method == "POST":
        form = NewProject(request.POST, request.FILES)

    if form.is_valid():

        try:
            item = form.save(commit=False)
            item.save()
            projet = projetModel.objects.filter(
                title=request.data.get("title")).values()
            return Response(projet[0])
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def remove(request, _id):
    if request.method == "DELETE":
        # projetModel.filter(id=request.data.get("id")).delete()
        projetModel.objects.filter(id=_id).delete()

        return Response(
            {
                "info": "delete",
            },
            status=status.HTTP_201_CREATED,
        )


@api_view(["PUT"])
def updatecourse(request, _id):

    projet = projetModel.objects.get(id=_id)
    if len(request.FILES) != 0:

        if request.FILES.get('photoUrl'):
            # os.remove(projet.photoUrl.path)
            projet.photoUrl = request.FILES['photoUrl']
        if request.FILES.get('logoUrl'):
            # os.remove(projet.logoUrl.path)
            projet.logoUrl = request.FILES['logoUrl']
        if request.FILES.get('sponsorLogoUrl'):
            # os.remove(projet.sponsorLogoUrl.path)
            projet.sponsorLogoUrl = request.FILES['sponsorLogoUrl']
    projet.title = request.data.get("title")
    projet.description = request.data.get("description")
    projet.link = request.data.get("link")
    projet.author = request.data.get("author")
    projet.save()
    # projetEdited = projetModel.objects.filter(title=request.data.get("id")).values()
    projetEdited = projetModel.objects.filter(id=_id).values()
    return Response(projetEdited[0])
