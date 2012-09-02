import random

from pyramid.renderers import render_to_response
from pyramid.view import view_config

import udcheck.dictionary

term_dict = udcheck.dictionary.create_dictionary()

@view_config(route_name='start',
             renderer='templates/start_page.pt')
def start_page(request):
    sess = request.session

    # Bootstrap the score
    sess['total'] = 0
    sess['correct'] = 0

    return {'project':'udcheck'}

@view_config(route_name='question',
             renderer='templates/question.pt')
def question(request):
    term1 = term_dict.get_random_term()
    term2 = term_dict.get_random_term()
    while term2.name == term1.name:
        term2 = term_dict.get_random_term()

    correct_term = term1 if random.randint(0,1) else term2

    return {
        'project': 'udcheck',
        'term1': term1.name,
        'term2': term2.name,
        'correct_term': correct_term.name,
        'definition': correct_term.definitions[
            random.randint(
                0,
                len(correct_term.definitions) - 1)],
    }

@view_config(route_name='respond')
def respond(request):
    sess = request.session

    try:
        if request.POST['selection'] == request.POST['correct']:
            sess['correct'] = sess['correct'] + 1
            template = 'correct_response.pt'
        else:
            template = 'incorrect_response.pt'

        sess['total'] = sess['total'] + 1

    except KeyError:
        template = 'start_page.pt'

    return render_to_response('templates/{}'.format(template),
                              {'project': 'udcheck'},
                              request=request)
