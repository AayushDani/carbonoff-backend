from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import CarbonFootprint

from .serializers import CarbonFootprintSerializer


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def create_footprint(request):

    if request.method == "POST":
        serializer = CarbonFootprintSerializer(data=request.data)

        if serializer.is_valid():
            carbon_footprint = serializer.save()

            data = {
                "response": "This carbon footprint was successfully logged."
            }
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_footprints(request):

    user = request.user

    footprints = CarbonFootprint.objects.filter(
        user=user).order_by('-created_at')
    data = []

    for footprint in footprints:
        footprint_data = {
            "footprint_id": footprint.pk,
            "carbon_footprint": footprint.carbon_footprint,
            "get_started_section_score": footprint.get_started_section_score,
            "travel_section_score": footprint.travel_section_score,
            "home_section_score": footprint.home_section_score,
            "food_section_score": footprint.food_section_score,
            "shopping_section_score": footprint.shopping_section_score,
            "created_at": footprint.created_at
        }

        data.append(footprint_data)

    data = {
        "response": data
    }

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_footprint(request, footprint_id):

    footprint = CarbonFootprint.objects.get(pk=footprint_id)

    footprint_data = {
        "footprint_id": footprint.pk,
        "carbon_footprint": footprint.carbon_footprint,
        "get_started_section_score": footprint.get_started_section_score,
        "travel_section_score": footprint.travel_section_score,
        "home_section_score": footprint.home_section_score,
        "food_section_score": footprint.food_section_score,
        "shopping_section_score": footprint.shopping_section_score,
        "created_at": footprint.created_at
    }

    data = {
        "response": footprint_data
    }

    return Response(data=data, status=status.HTTP_200_OK)
