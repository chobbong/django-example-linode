from django.db.models import Q
from django.shortcuts import render
from .models import PropertyData

def search(request):
    query = request.GET.get('query', '')
    properties = []
    locations = []  # 구글 지도에 표시할 위치 정보를 저장할 리스트
    if query:
        properties = PropertyData.objects.filter(Q(시군구__icontains=query) | Q(단지명__icontains=query))
        print(properties.query)  # SQL 쿼리 출력
        
        for prop in properties:
            print(prop)  # 각 결과값을 출력
            location_data = {
                'lat': prop.lat,
                'lng': prop.lng,
                'name': str(prop)  # 단지명 또는 시군구 이름을 표시하기 위해 사용
            }
            locations.append(location_data)

    context = {
        'properties': properties,
        'locations': locations
    }

    return render(request, 'other/search.html', context)

