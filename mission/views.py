from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from cat.models import Cat

from .models import Mission, Target
from .serializers import MissionSerializer, TargetSerializer


class MissionList(APIView):
    def get(self, request):
        missions = Mission.objects.all()
        serializer = MissionSerializer(missions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MissionDetails(APIView):
    def get(self, request, id):
        mission = get_object_or_404(Mission, pk=id)
        serializer = MissionSerializer(mission)
        return Response(serializer.data)

    def delete(self, request, id):
        mission = Mission.objects.get(pk=id)
        mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FindMissionByCatId(APIView):
    def post(self, request):
        missions = Mission.objects.filter(cat=request.data.get("cat_id"))
        serializer = MissionSerializer(missions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AssignCatToMission(APIView):
    def post(self, request):
        mission_id = request.data.get("mission_id")
        cat_id = request.data.get("cat_id")

        mission = get_object_or_404(Mission, pk=mission_id)
        cat = get_object_or_404(Cat, pk=cat_id)

        mission.cat = cat
        mission.save()

        serializer = MissionSerializer(mission)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompleteMission(APIView):
    def patch(self, request):
        mission_id = request.data.get("id")
        is_completed = request.data.get("is_completed")

        if mission_id is None or is_completed is None:
            return Response(
                {"error": "id and is_completed are required fields."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        mission = get_object_or_404(Mission, pk=mission_id)

        mission.is_completed = is_completed
        mission.save()

        serializer = MissionSerializer(mission)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateName(APIView):
    def patch(self, request, id):
        mission = get_object_or_404(Mission, pk=id)

        new_name = request.data.get("name")
        if new_name is None:
            return Response(
                {"error": "Name field is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        mission.name = new_name
        mission.save()

        serializer = MissionSerializer(mission)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddTarget(APIView):
    def patch(self, request):
        mission_id = request.data.get("mission_id")

        mission = get_object_or_404(Mission, pk=mission_id)

        if mission.is_completed:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data["mission"] = mission_id

        serializer = TargetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompleteTarget(APIView):
    def patch(self, request):
        target_id = request.data.get("id")
        mission_id = request.data.get("mission_id")
        is_completed = request.data.get("is_completed")

        if target_id is None or mission_id is None or is_completed is None:
            return Response(
                {"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST
            )

        target = get_object_or_404(Target, id=target_id, mission_id=mission_id)

        target.is_completed = is_completed
        target.save()

        serializer = TargetSerializer(target)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RemoveTarget(APIView):
    def delete(self, request):
        target_id = request.data.get("target_id")
        mission_id = request.data.get("mission_id")

        if target_id is None or mission_id is None:
            return Response(
                {"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST
            )

        target = get_object_or_404(Target, id=target_id, mission_id=mission_id)
        target.delete()

        return Response(
            {"message": "Target deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class UpdateTarget(APIView):
    def patch(self, request):
        id = request.data.get("id")
        target = get_object_or_404(Target, pk=id)
        serializer = TargetSerializer(target, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateNotes(APIView):
    def patch(self, request):
        target_id = request.data.get("id")
        mission_id = request.data.get("mission_id")
        notes = request.data.get("notes")

        if target_id is None or mission_id is None or notes is None:
            return Response(
                {"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST
            )

        target = get_object_or_404(Target, id=target_id, mission_id=mission_id)

        target.notes = notes
        target.save()

        serializer = TargetSerializer(target)
        return Response(serializer.data, status=status.HTTP_200_OK)
