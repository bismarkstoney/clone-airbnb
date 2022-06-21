from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage
from rooms.models import Room
# Create your views here.
# def all_rooms(request):
#     page=request.GET.get('page',1)
#     room_list= Room.objects.all()
#     paginator=Paginator(room_list, 10, orphans=2)
#     try:
#         rooms=paginator.page(int(page))
#         return render(request, 'rooms/home.html', context={"page":rooms})
#     except EmptyPage:
#         return redirect('/')

class HomeView(ListView):
    """Home view Defination"""
    model =Room
    template_name='rooms/home.html'
    context_object_name= 'page'
    paginate_orphans=2
    paginate_by=6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now=timezone.now()
        context["now"] = now
        return context
    
def room_detail(request, pk):
    print(pk)
    return render(request, 'rooms/detail.html')
    
    
    
        
    
   
    
    