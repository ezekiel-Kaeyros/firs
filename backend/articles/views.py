from django.shortcuts import render
from .forms import NewArticle

# Create your views here.


def new_article(request):
    if request.method == "POST":
        form = NewArticle(data=request.data)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            # return redirect("item:detail", pk=item.id)
    else:
        form = NewArticle()

    # return render(
    #     request,
    #     "item/form.html",
    #     {
    #         "form": form,
    #         "title": "New item",
    #     },
    # )
