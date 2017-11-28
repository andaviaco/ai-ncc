import numpy as np
from PIL import Image

from devol import DE


def ncc(img, template):
    ih, iw = img.shape
    th, tw = template.shape

    itemplate = template.astype('int_')
    iimg = img.astype('int_')

    t_sum = (itemplate ** 2).sum()

    def fn(vector):
        y, x = np.rint(vector).astype('int_')
        i_slice = iimg[y:y+th, x:x+tw]
        it_sum = (i_slice ** 2).sum()

        a = (i_slice * itemplate).sum()
        b = it_sum * t_sum
        result = a / np.sqrt(b)

        return result

    return fn

def main():
    target_im = Image.open('img/Image_1.bmp').convert("L")
    template_im = Image.open('img/Template.bmp').convert("L")

    print(target_im.format, target_im.size, target_im.mode)

    print(template_im.format, template_im.size, template_im.mode)

    print(dir(target_im))
    # de_sphere = DE(50, 100, sphere, lb=[-5, -5], ub=[5, 5])
    # result = de_sphere.optimize()

    # print(result)

if __name__ == '__main__':
    main()
