from django.shortcuts import render
from core.models import Sentiment

def BootstrapFilterView(request):
    sentiments = Sentiment.objects.all()
    product_name_contains_query = request.GET.get('product_name_contains')

    if product_name_contains_query != '' and product_name_contains_query is not None:
        sentiments = sentiments.filter(
            Product_Name__icontains=product_name_contains_query)
    else:
        sentiments = None
    context = {
        'queryset': sentiments
    }
    return render(request, "bootstrap_form.html", context)


def search_products(request):
    if request.method == "POST":
        search_product_text = request.POST['search_product_text']
    else:
        search_product_text = ''

    sentiments = Sentiment.objects.filter(
        Product_Name__icontains=search_product_text)

    return render(request, 'ajax_search.html', {'sentiments': sentiments})
