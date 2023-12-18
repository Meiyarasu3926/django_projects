from django.shortcuts import render
from wikipedia.exceptions import DisambiguationError
import wikipedia
# Create your views here.


def home(request):
    return render(request, 'home.html')

def word(request):
    query = request.GET.get('search')
    result = wikipedia.search(query)
    summ = ""

    try:
        # Attempt to get the summary of the first result
        summ = wikipedia.page(result[0]).summary
    except DisambiguationError as e:
        options = e.options
        context = {
            'result': result,
            'options': options,
            'error_message': f'The term "{query}" may refer to:',
        }
        return render(request, 'error.html', context)
    except wikipedia.exceptions.PageError:
        summ = "No Wikipedia page found for the query."

    context = {
        'result': result,
        'summary': summ,
    }
    return render(request, 'word.html', context)

