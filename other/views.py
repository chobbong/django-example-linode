from django.shortcuts import render
from .models import PropertyData
from django.http import JsonResponse

# ######:8000/other/
# Create your views here.
def search_estate_data(request):
    context = {}
    if request.method == "POST":
        keyword = request.POST.get('search_point')
        results = PropertyData.objects.filter(시군구__icontains=keyword) | PropertyData.objects.filter(단지명__icontains=keyword)
        context['results'] = results
    return render(request, 'other/search.html', context)

def get_estate_data(request):
    keyword = request.GET.get('keyword')
    results = PropertyData.objects.filter(시군구__icontains=keyword) | PropertyData.objects.filter(단지명__icontains=keyword)
    
    data = []
    for result in results:
        data.append({
            "lat": result.lat,
            "lng": result.lng,
            "시군구": result.시군구,
            "단지명": result.단지명,
            # 필요한 다른 필드들도 추가할 수 있습니다.
        })

    return JsonResponse(data, safe=False)
