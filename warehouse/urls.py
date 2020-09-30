from django.urls import path
from .views import RollsListCreateView, RollDetailView, RollsConsumptionListView, \
    PaperFormatListView, PaperFormatDetailView, PaperGrammageListView, PaperGrammageDetailView, RollsIncomeListView, \
    RollsReturnListView, RollProductionDetailView, PaperProducerListView, PaperProducerDetailView, PaperTypesListView, \
    PaperTypesDetailView, RollsProductionListView, RollTotalInfoListView, PaperListView

app_name = 'warehouse'
# api/warehouse/
urlpatterns = [
    path('rolls/all/', RollsListCreateView.as_view()),
    path('rolls/all/<int:roll_id>/', RollDetailView.as_view()),
]

urlpatterns += [
    path('rolls/total/', RollTotalInfoListView.as_view()),
]

urlpatterns += [
    path('rolls/consumption/', RollsConsumptionListView.as_view()),
    path('rolls/consumption/<int:pk>/', RollsConsumptionListView.as_view())

]

urlpatterns += [
    path('rolls/production/', RollsProductionListView.as_view()),
    path('rolls/production/<int:pk>/', RollProductionDetailView.as_view())

]

urlpatterns += [
    path('rolls/income/', RollsIncomeListView.as_view()),
]

urlpatterns += [
    path('rolls/return/', RollsReturnListView.as_view()),
]

urlpatterns += [
    path('papers/formats/', PaperFormatListView.as_view()),
    path('papers/formats/<int:pk>/', PaperFormatDetailView.as_view()),
]

urlpatterns += [
    path('papers/grammage/', PaperGrammageListView.as_view()),
    path('papers/grammage/<int:pk>/', PaperGrammageDetailView.as_view()),
]

urlpatterns += [
    path('papers/producers/', PaperProducerListView.as_view()),
    path('papers/producers/<int:pk>/', PaperProducerDetailView.as_view()),
]

urlpatterns += [
    path('papers/types/', PaperTypesListView.as_view()),
    path('papers/types/<int:pk>/', PaperTypesDetailView.as_view()),
]

urlpatterns += [
    path('papers/all/', PaperListView.as_view()),
]
