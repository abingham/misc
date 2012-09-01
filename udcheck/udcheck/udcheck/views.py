from pyramid.renderers import render_to_response
from pyramid.view import view_config

@view_config(route_name='home',
             renderer='templates/start_page.pt')
def start_page(request):
    sess = request.session

    # Bootstrap the score if necessary
    if 'total' not in sess:
        sess['total'] = 0
        sess['correct'] = 0

    # set up next question
    sess['definition'] = 'A funny name for a bear.'
    sess['term1'] = 'Baloo'
    sess['term2'] = 'Yonker'
    sess['correct_term'] = 'term1'

    return {'project':'udcheck'}

@view_config(route_name='respond')
def respond(request):
    sess = request.session

    try:
        if request.POST['selection'] == request.session['correct_term']:
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
