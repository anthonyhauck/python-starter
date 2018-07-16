from hypar import glTF
import math

def handler(event, context):
    length = event.get('length')
    width = event.get('width')
    height = event.get('height')
    return box(length, width, height)

def box(length: float, width: float, height: float) -> dict:
    """Create a box.
    
    Arguments:
        args {object} -- A dictionary containing the 'length', 'width', and 'height'.

    Raises:
        Exception -- If the length is not provided, or is <= 0.
        Exception -- If the width is not provided, or is <= 0.
        Exception -- If the height is not provided or is <= 0.
    
    Returns:
        dictionary -- A dictionary containing a model and computed values.
    """

    if height <= 0.0: 
        raise Exception('The height must be greater than 0.')

    if length <= 0.0:
        raise Exception('The length must be greater than 0.')

    if width <= 0.0:
        raise Exception('The width must be greater than 0.')

    model = create_box(length, width, height)

    return {"model": model.save_base64(), "computed": {"volume": (height * length * width)}}

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c


def create_square_face(vertices, normals, indices, index, a, b, c, d):
    vertices.extend(a)
    vertices.extend(b)
    vertices.extend(c)
    vertices.extend(d)
    indices.append(index)
    indices.append(index+1)
    indices.append(index+2)
    indices.append(index)
    indices.append(index+2)
    indices.append(index+3)
    index = index + 4
    v1l = math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1],2) + math.pow(b[2] - a[2], 2))
    v2l = math.sqrt(math.pow(c[0] - b[0], 2) + math.pow(c[1] - b[1],2) + math.pow(c[2] - b[2], 2))
    v1 = [(b[0] - a[0])/v1l, (b[1] - a[1])/v1l, (b[2] - a[2])/v1l]
    v2 = [(c[0] - b[0])/v2l, (c[1] - b[1])/v2l, (c[2] - b[2])/v2l]
    n = cross(v1, v2)
    normals.extend(n)
    normals.extend(n)
    normals.extend(n)
    normals.extend(n)
    return index


def create_box(length, width, height):
    vertices = []
    normals = []
    indices = []

    # Create a model to hold the geometry.
    model = glTF()

    # Create a material to use in the model.
    model.add_material(0.0, 0.0, 1.0, 0.9, 1.0, "Blue")

    # bottom
    b1 = [0, 0, 0]
    b2 = [width, 0, 0]
    b3 = [width, length, 0]
    b4 = [0, length, 0]

    t1 = [0, 0, height]
    t2 = [width, 0, height]
    t3 = [width, length, height]
    t4 = [0, length, height]

    index = create_square_face(vertices, normals, indices, 0, b4, b3, b2, b1)
    index = create_square_face(vertices, normals, indices, index, t1, t2, t3, t4)
    index = create_square_face(vertices, normals, indices, index, b1, b2, t2, t1)
    index = create_square_face(vertices, normals, indices, index, b2, b3, t3, t2)
    index = create_square_face(vertices, normals, indices, index, b3, b4, t4, t3)
    index = create_square_face(vertices, normals, indices, index, b4, b1, t1, t4)

    model.add_triangle_mesh(vertices, normals, indices, 0)

    return model