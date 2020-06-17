from django.urls import path
from .views import RollsListView, RollDetailView, RollsConsumptionListView, \
    PaperFormatListView, PaperFormatDetailView, PaperGrammageListView, PaperGrammageDetailView, RollsIncomeListView, \
    RollsReturnListView

app_name = 'warehouse'

urlpatterns = [
    path('rolls/all/', RollsListView.as_view()),
    path('rolls/all/<int:roll_id>/', RollDetailView.as_view()),
]

urlpatterns += [
    path('rolls/consumption/', RollsConsumptionListView.as_view()),
]

urlpatterns += [
    path('rolls/income/', RollsIncomeListView.as_view()),
]

urlpatterns += [
    path('rolls/return/', RollsReturnListView.as_view()),
]

urlpatterns += [
    path('papers/formats/', PaperFormatListView.as_view()),
    path('papers/formats/<int:format_id>/', PaperFormatDetailView.as_view()),
]

urlpatterns += [
    path('papers/grammage/', PaperGrammageListView.as_view()),
    path('papers/grammage/<int:format_id>/', PaperGrammageDetailView.as_view()),
]
