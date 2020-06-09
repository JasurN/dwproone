from django.urls import path
from .views import RollsListView, RollDetailView, RollsConsumptionListView, PaperFormatListView

app_name = 'warehouse'

urlpatterns = [
    path('rolls/', RollsListView.as_view()),
    path('rolls/<int:roll_id>/', RollDetailView.as_view()),
]

urlpatterns += [
    path('rolls/consumption/', RollsConsumptionListView.as_view()),
]

urlpatterns += [
    path('papers/formats', PaperFormatListView.as_view()),
]
