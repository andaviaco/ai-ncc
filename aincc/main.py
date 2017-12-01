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
    template_im = Image.open('img/test_01.bmp').convert("L")

    target_matrix = np.asarray(target_im)
    template_matrix = np.asarray(template_im)
    lower_bounds = (0, 0)
    upper_bounds = [bound - template_matrix.shape[i] for i, bound in enumerate(target_matrix.shape)]

    objetive_fn = ncc(target_matrix, template_matrix)
    de_sphere = DE(100, 100, objetive_fn, lb=lower_bounds, ub=upper_bounds, optimization='max')
    result = de_sphere.optimize()
    y, x = np.rint(result).astype('int_')

    print(f'NCC: {objetive_fn(result)}')
    print(f'x ≃ {x}')
    print(f'y ≃ {y}')

if __name__ == '__main__':
    main()
