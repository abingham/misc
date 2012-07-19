import baker
import numpy
import tables

@baker.command
def build(x=1000, y=1000, z=1000):
    atom = tables.UInt8Atom()
    filters = tables.Filters(complevel=5, complib='zlib')
    
    h5f = tables.openFile('cube_data.h5', 'w')
    ca = h5f.createCArray(h5f.root, 
                          'carray', 
                          atom=tables.Float64Atom(), 
                          shape=(x, y, z, 3),
                          filters=tables.Filters(complevel=5, complib='zlib'))

    # Fill a hyperslab in ``ca``.
    #ca[:, :, 0] = numpy.ones((1000,))
    h5f.close()

@baker.command
def build_uncompressed(x=100, y=1000, z=1000):
    h5f = tables.openFile('cube_data.h5', 'w')
    data = numpy.zeros((int(x), int(y), int(z)), numpy.float64)
    ca = h5f.createArray(h5f.root, 
                         'array', 
                         data,
                         'a bunch of data')

    h5f.close()

@baker.command
def populate_table():
    h5f = tables.openFile('cube_data.h5', 'a')
    ca = h5f.root.array
    print('shape: {}'.format(ca.shape))

    for x in range(ca.shape[0]):
        print(x)
        for y in range(ca.shape[1]):
            ca[x, y] = numpy.linspace(x, y, ca.shape[2])

    h5f.close()

if __name__ == '__main__':
    baker.run()