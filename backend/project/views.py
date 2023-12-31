from .forms import NewProject
from rest_framework.response import Response
from django.http import JsonResponse
from .models import projetModel
from rest_framework.decorators import api_view
from rest_framework import status
import time

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
        # print(request.FILES)
        # time.sleep(2000)
        form = NewProject(request.POST, request.FILES)

    if form.is_valid():
        item = form.save(commit=False)
        # item.created_by = request.user

        item.save()
        projet = projetModel.objects.filter(title=request.data.get("title")).values()
        # return JsonResponse({"course": list(course)})
        return Response(projet[0])
        # return Response(
        #     {
        #         "new_project": f"{item}",
        #     },
        # )
    else:
        form = NewProject()


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
    # projet = projetModel.objects.get(id=request.data.get("id"))
    projet = projetModel.objects.get(id=_id)
    projet.title = request.data.get("title")
    projet.description = request.data.get("description")
    projet.link = request.data.get("link")
    projet.author = request.data.get("author")
    projet.save()
    # projetEdited = projetModel.objects.filter(title=request.data.get("id")).values()
    projetEdited = projetModel.objects.filter(id=_id).values()
    return Response(projetEdited[0])
    # return Response(
    #     {
    #         "info": "update",
    #     },
    #     status=status.HTTP_201_CREATED,
    # )
