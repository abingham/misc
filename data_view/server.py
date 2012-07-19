import Image
import tables
import web

web.config.debug = True

filename = 'cube_data.h5'
h5f = tables.openFile(filename, 'r')
arr = h5f.root.array

render = web.template.render('templates/')

def get_slice(cube, axis, idx):
    if axis == 'x':
        return cube[idx, :, :]
    elif axis == 'y':
        return cube[:, idx, :]
    elif axis == 'z':
        return cube[:, :, idx]

class info:
    def GET(self):
        return render.info(filename,
                           arr)

class request:
    def GET(self, axis, index):
        #web.header('Content-type', 'text/html')
        #return '<html>requested {},{}</html>'.format(axis, index)
        return '<html><img src="/image/{}/{}/image.bmp"/></html>'.format(
            axis, index)

class image:
    def GET(self, axis, index):
        index = int(index)
        data = get_slice(arr, axis, index)
        im = Image.new('RGB', data.shape)
        for i in range(min(data.shape)):
            im.putpixel((i,i), (255, 0, 0))

        web.header('Content-type', 'image/raw')
        return im.tostring()

urls = (
    '/', info,
    '/request/([x-z])/(\d+)', request,
    '/image/([x-z])/(\d+)/image.bmp', image,
)

def run():
    app = web.application(urls, locals())
    app.run()

if __name__ == '__main__':
    run()