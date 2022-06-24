from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from rooms.models import Room

from rooms.form import Form
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
    ordering='created_at'
    paginate_by=6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now=timezone.now()
        context["now"] = now
        return context
    
# def room_detail(request, pk):
#     try:
#         room= Room.objects.get(pk=pk)
#         return render(request, 'rooms/detail.html', context={'room': room})
#     except Room.DoesNotExist:
#         #return redirect(reverse('core:home'))
#         raise Http404()
    
class Room_Detail(DetailView):
    model= Room
    template_name= 'rooms/detail.html'
    

def search(request):
    country=request.GET.get('country')
    if country:
        form=Form(request.GET)
        if form.is_valid():
            city=form.cleaned_data.get('city')          
            country=form.cleaned_data.get('country', 'GH')
            room_type=form.cleaned_data.get('room_type')
            price=form.cleaned_data.get('price')
            beds=form.cleaned_data.get('beds')
            bath=form.cleaned_data.get('bath')
            bedrooms=form.cleaned_data.get('bedrooms')
            guest=form.cleaned_data.get('guest')
          
            amenties=form.cleaned_data.get('amenties')
            facilities=form.cleaned_data.get('facilities')
            
            filter_args={}
            if city != "Anywhere":
                filter_args['city__startswith']=str.capitalize(city)
            filter_args['country']=country
            if guest is not None:
                filter_args['guest']= guest
            if beds is not None:
                filter_args['beds']=beds
            if bath is not None:
                filter_args['bath']=bath
            if room_type is not None:
                filter_args['room_type']=room_type
            # if instaant is True:
            #     filter_args['instant']=instant
            for amenity in amenties:
                filter_args['amenities']=amenity
            for facility in facilities:
                filter_args['facility']=facility
            
            if price is not None:
                filter_args["price__lte"]=price
                
            qs = Room.objects.filter(**filter_args).order_by("-created_at")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            rooms = paginator.get_page(page)

                
            rooms=Room.objects.filter(**filter_args)
            return render(request, "rooms/search.html",{"form": form, 'rooms':rooms} )
            
    else:
        form= Form()
   
   
    
    return render(request, "rooms/search.html",{"form": form} )
        
    
    
    
    
        
    
   
    
    