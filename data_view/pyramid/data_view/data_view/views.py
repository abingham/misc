import io
import os

import numpy
import png
from pyramid.response import Response
from pyramid.view import view_config


filename = 'cube_data.h5'
# h5f = tables.openFile(filename, 'r')
#arr = h5f.root.array

this_dir = os.path.split(os.path.abspath(__file__))[0]
arr = numpy.load(os.path.join(this_dir, '..', 'red_shaded.npy'))

#numpy.array(
#    numpy.random.rand(100, 1000, 1000) * 255,
#    dtype=numpy.uint8)

def get_slice(cube, axis, idx):
    if axis == 'x':
        return cube[idx, :, :]
    elif axis == 'y':
        return cube[:, idx, :]
    elif axis == 'z':
        return cube[:, :, idx]

@view_config(route_name='home',
             renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'data_view'}

@view_config(route_name='cube_info',
             request_method='GET',
             renderer='templates/info.pt')
def info(request):
    return {
        'filename': filename,
        'arr': arr
    }

@view_config(route_name='view_slice',
             request_method='GET')
def view_slice(request):
    try:
        index = request.matchdict['index'][0]
    except IndexError:
        index = 0

    # TODO: What if ['index'] is longer? We should report a 404 or something.

    return Response(
        '<html><img src="/image/{}/{}"/></html>'.format(
            request.matchdict['axis'],
            index))

@view_config(route_name='slice_image',
             request_method='GET')
def slice_image(request):
    axis = request.matchdict['axis']
    index = int(request.matchdict['index'])
    data = get_slice(arr, axis, index)

    w = png.Writer(data.shape[1],
                   data.shape[0],
                   palette=[(i, 0, 0) for i in range(255)],
                   bitdepth=8)

    buff = io.BytesIO()
    w.write(buff, data)
    buff.seek(0)
    return Response(
        body=buff.read(),
        content_type='image/png')
