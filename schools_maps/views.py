from django.shortcuts import render
from .models import School
from django.http import JsonResponse
from .constants import REGION_COORDINATES

def index(request):
    """Renders the school index page."""
    schools = School.objects.all()  # Fetch all schools from the database
    return render(request, 'schools_maps/index.html', {'schools': schools})

def get_schools(request):
    """Fetches schools based on selected region and display type."""
    region = request.GET.get('region')  # Get selected region
    display_type = request.GET.get('displayType')  # Get display type (Point or Heatmap)

    if region == "全国":
        schools = School.objects.all().values(
            'name', 'category', 'deviation', 'address', 'url', 'latitude', 'longitude', 'region'
        )
    else:
        # For point map, return specific region schools or fall back to default (東京都)
        schools = School.objects.filter(region=region).values(
            'name', 'category', 'deviation', 'address', 'url', 'latitude', 'longitude', 'region'
        ) if region else School.objects.filter(region="東京都").values(
            'name', 'category', 'deviation', 'address', 'url', 'latitude', 'longitude', 'region'
        )
    # Set region center based on coordinates
    region_center = REGION_COORDINATES.get(region, REGION_COORDINATES["東京都"])

    # Prepare response data
    response_data = {
        'schools': list(schools),
        'region_center': region_center
    }
    
    return JsonResponse(response_data, safe=False)
