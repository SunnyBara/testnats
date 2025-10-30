from django.http import HttpResponse
from django.template import loader
from test_app.models import Dummy


def handler(request):
    if request.method == "POST":
        name_value = request.POST.get("name")

        if name_value:
            name = Dummy.objects.create(name=name_value)
            name.save()

    template = loader.get_template("template.html")
    return HttpResponse(template.render({}, request))
