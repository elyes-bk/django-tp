from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator

from .models import Site


def home(request):
    sites = Site.objects.all().order_by("nom")

    paginator = Paginator(sites, 12)  # 12 sites par page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "main/home.html", {
        "page_obj": page_obj
    })

def site_detail(request, pk):
    site = get_object_or_404(Site, pk=pk)

    return render(request, "main/site_detail.html", {
        "site": site
    })