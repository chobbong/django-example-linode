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
                '단지명': prop.단지명,
                '시군구': prop.시군구,
                '계약연월': prop.계약연월,
                '전용면적': prop.전용면적,
                '매매대금_평균': prop.매매대금_평균,
                '전세_평균': prop.전세_평균,
                '전세가율_90': prop.전세가율_90,
                '전세가율_80': prop.전세가율_80,
                '전세가율_70': prop.전세가율_70,
                '전세가율_60': prop.전세가율_60
            }
            locations.append(location_data)

    context = {
        'properties': properties,
        'locations': locations
    }

    return render(request, 'other/search.html', context)


