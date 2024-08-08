from django.urls import path
from .views import (
    AddTarget,
    MissionDetails,
    MissionList,
    AssignCatToMission,
    FindMissionByCatId,
    CompleteMission,
    UpdateName,
    CompleteTarget,
    RemoveTarget,
    UpdateNotes,
    UpdateTarget,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", MissionList.as_view()),
    path("<int:id>", MissionDetails.as_view()),
    path("assign", AssignCatToMission.as_view()),
    path("find_missions", FindMissionByCatId.as_view()),
    path("complete_mission", CompleteMission.as_view()),
    path("<int:id>/update_name", UpdateName.as_view()),
    
    path("add_target", AddTarget.as_view()),
    path("complete_target", CompleteTarget.as_view()),
    path("remove_target", RemoveTarget.as_view()),
    path("update_note", UpdateNotes.as_view()),
    path("update_target", UpdateTarget.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
