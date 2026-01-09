from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Site, Typologie, Denomination, Olympiade


def home(request):
    sites = Site.objects.all()

    query = request.GET.get("q")
    if query:
        sites = sites.filter(
            Q(nom__icontains=query) |
            Q(description__icontains=query) |
            Q(commune__icontains=query)
        )

    typologie_id = request.GET.get("typologie")
    if typologie_id:
        sites = sites.filter(typologies__id=typologie_id)

    denomination_id = request.GET.get("denomination")
    if denomination_id:
        sites = sites.filter(denominations__id=denomination_id)

    olympiade_id = request.GET.get("olympiade")
    if olympiade_id:
        sites = sites.filter(olympiade__id=olympiade_id)

    sites = sites.distinct()

    paginator = Paginator(sites, 12)  # 12 sites par page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "typologies": Typologie.objects.all(),
        "denominations": Denomination.objects.all(),
        "olympiades": Olympiade.objects.all(),
    }

    return render(request, "main/home.html",context)

def site_detail(request, pk):
    site = get_object_or_404(Site, pk=pk)

    return render(request, "main/site_detail.html", {
        "site": site
    })