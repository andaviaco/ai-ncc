import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from devol import DE

def  plotresults(image, template, result):
    im = np.array(image, dtype=np.uint8)
    t_width, t_height = template.size
    y, x = result

    fig, ax = plt.subplots(1)

    ax.imshow(im)

    # Create a Rectangle patch
    rect = patches.Rectangle((x, y), t_width, t_height, linewidth=1, edgecolor='r', facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

    plt.show()

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

def main(img, template):
    target_im = Image.open(img)
    template_im = Image.open(template)

    target_matrix = np.asarray(target_im.convert("L"))
    template_matrix = np.asarray(template_im.convert("L"))
    lower_bounds = (0, 0)
    upper_bounds = [bound - template_matrix.shape[i] for i, bound in enumerate(target_matrix.shape)]

    objetive_fn = ncc(target_matrix, template_matrix)
    de_sphere = DE(100, 100, objetive_fn, lb=lower_bounds, ub=upper_bounds, optimization='max')
    result = de_sphere.optimize()
    y, x = np.rint(result).astype('int_')

    print(f'NCC: {objetive_fn(result)}')
    print(f'x ≃ {x}')
    print(f'y ≃ {y}')

    plotresults(target_im, template_im, result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="Target image.")
    parser.add_argument("template", help="Template image.")
    args = parser.parse_args()

    main(args.image, args.template)
