from devol import DE

def sphere(vector):
    return sum([x**2 for x in vector])

def main():
    de_sphere = DE(50, 100, sphere, lb=[-5, -5], ub=[5, 5])
    result = de_sphere.optimize()

    print(result)

if __name__ == '__main__':
    main()
