from django.views.generic import TemplateView, FormView
from main.forms import OrderForm, OrderDishFormSet
from main.models import OrderDish, Order


class MainPageView(TemplateView):
    template_name = 'main.html'


class CreateOrderView(FormView):
    template_name = 'create-order.html'
    form_class = OrderForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OrderDishFormSet(self.request.POST)
        else:
            context['formset'] = OrderDishFormSet()
        return context

    def form_valid(self, form):
        order = form.save()
        formset = OrderDishFormSet(self.request.POST)
        if formset.is_valid():
            for order_dish_form in formset:
                dish = order_dish_form.cleaned_data.get('dish')
                if dish:
                    OrderDish.objects.create(order=order, dish=dish)
        return super().form_valid(form)


class HistoryOrderView(TemplateView):
    template_name = 'history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_dict = {}
        for order in Order.objects.all().order_by('-date').select_related('worker'):
            dishes = [str(dish) for dish in order.dish.all()]
            order_id, name, date = order.id, order.worker.name, order.date.strftime("%H:%M %d-%m")
            order_dict[f'{order_id} order by {name} from {date}'] = dishes
        context['order_dict'] = order_dict
        return context
