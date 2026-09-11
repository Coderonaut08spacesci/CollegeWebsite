from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Notice, Event
from .forms import NoticeForm, ContactForm

# --- CLASS-BASED VIEWS (CRUD for Notices) ---

# READ (List)
class NoticeListView(ListView):
    model = Notice
    template_name = 'portal/notice_list.html'
    context_object_name = 'notices'

# READ (Detail - uses dynamic URL parameter <int:pk>)
class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'portal/notice_detail.html'

# CREATE
class NoticeCreateView(CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'portal/notice_form.html'

# UPDATE
class NoticeUpdateView(UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'portal/notice_form.html'

# DELETE
class NoticeDeleteView(DeleteView):
    model = Notice
    template_name = 'portal/notice_confirm_delete.html'
    success_url = reverse_lazy('notice-list')


# --- FUNCTION-BASED VIEWS (FBVs) ---

# FBV for Query Parameter Search (?q=...)
def search_view(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Notice.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'portal/search_results.html', {'results': results, 'query': query})

# FBV for Contact Form submission
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            return render(request, 'portal/contact_success.html', {'name': form.cleaned_data['name']})
    else:
        form = ContactForm()
    return render(request, 'portal/contact.html', {'form': form})
