from PIL import Image

from devol import DE


def sphere(vector):
    return sum([x**2 for x in vector])

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
