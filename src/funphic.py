import function
from render import RenderType, RenderException
from PIL import Image
from os import system
from sys import argv


'''
argv padrão
-----------
[1] function
[2] x_range_start
[3] x_range_end
[4] y_range_start
[5] y_range_end
[6] x_increment
[7] point_color
[8] back_color
[9] render_type
'''


def get_function() -> str:

    ''' trata a função fornecida no argv[1] '''

    try:
        return argv[1]

    except IndexError:
        return input('Enter a function: ')


def get_args() -> 'list':

    '''
    retorna lista organizada e formatada no formato do argv padrão,
    atribuindo valores padrão se nescessário
    '''

    main_args = [
        get_function(), '-50', '50', '-50',
        '50', '.1', 'blue', 'white', 'image'
    ]

    for i in range(len(argv[1:])):
        main_args[i] = argv[i + 1]

    format_args(main_args)

    return main_args


def format_args(args: list):

    ''' Converte cada arg para o seu tipo de dado específico '''

    args[1] = int(args[1])
    args[2] = int(args[2])
    args[3] = int(args[3])
    args[4] = int(args[4])
    args[5] = float(args[5])


def show_graph(
    function_str, x_range, y_range,
    x_inc, point_color,
    back_color, render_type
):

    ''' mostra o gráfico da função '''

    func = function.Function(function_str)

    graph = func.generate_graph(
        x_range,
        y_range,
        x_inc,
        point_color,
        back_color,
        render_type
    )

    if render_type == RenderType.IMAGE:
        show_graph_image(graph)

    elif render_type == RenderType.TERM:
        show_graph_term(graph)


def show_graph_image(graph):

    ''' mostra o gráfico como imagem '''

    X_LEN = len(graph)
    Y_LEN = len(graph[0])

    img = Image.new('RGB', (Y_LEN, X_LEN), 'white')
    pixels = img.load()

    for column in range(img.size[0]):
        for row in range(img.size[1]):
            pixels[column, row] = graph[row][column]

    img.show()


def show_graph_term(graph):

    ''' mostra o gráfico como caracteres no terminal '''

    # configurando terminal para renderizar cores
    system('color')

    for row in graph:
        for column in row:
            print(column, end='')
        print()


if __name__ == '__main__':

    try:
        ARGS = get_args()

        FUNCTION = ARGS[0]
        X_RANGE = (ARGS[1], ARGS[2])
        Y_RANGE = (ARGS[3], ARGS[4])
        X_INC = ARGS[5]
        POINT_COLOR = ARGS[6]
        BACK_COLOR = ARGS[7]
        RENDER_TYPE = ARGS[8]

    except ValueError as ve:
        print(f'Invalid argument: {ve.__str__().split(":")[1].strip()}')

    else:
        try:
            show_graph(
                FUNCTION,
                X_RANGE,
                Y_RANGE,
                X_INC,
                POINT_COLOR,
                BACK_COLOR,
                RENDER_TYPE
            )

        except NameError as ne:
            print(ne)

        except SyntaxError as se:
            print(se)

        except ZeroDivisionError as zde:
            print(zde)

        except ValueError as ve:
            print(ve)

        except RenderException as re:
            print(re)
