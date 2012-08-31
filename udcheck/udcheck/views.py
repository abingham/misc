from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home',
             renderer='templates/start_page.pt')
def start_page(request):
    return {'project':'data_view'}

# @view_config(route_name='cube_info',
#              request_method='GET',
#              renderer='templates/info.pt')
# def info(request):
#     return {
#         'filename': filename,
#         'arr': arr
#     }

# @view_config(route_name='view_slice',
#              request_method='GET')
# def view_slice(request):
#     return Response(
#         '<html><img src="/image/{}/{}"/></html>'.format(
#             request.matchdict['axis'],
#             request.matchdict['index']))

# @view_config(route_name='slice_image',
#              request_method='GET')
# def slice_image(request):
#     axis = request.matchdict['axis']
#     index = int(request.matchdict['index'])
#     data = get_slice(arr, axis, index)

#     w = png.Writer(data.shape[1],
#                    data.shape[0],
#                    palette=[(i, 0, 0) for i in range(255)],
#                    bitdepth=8)

#     buff = io.BytesIO()
#     w.write(buff, data)
#     buff.seek(0)
#     return Response(
#         body=buff.read(),
#         content_type='image/png')
