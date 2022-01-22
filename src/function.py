import screen
from render import RenderType
from math import (
    sqrt, exp, log, acos, asin, atan, cos, sin, tan,
    pi, e, tau, inf
)


class Function:

    ''' Classe para representar uma função matemática com uma incógnita x

    métodos
    -------
    findImage(x) -> float
        calcula a imagem de um ponto x na função especificada no
        atributo __function
    generate_graph(x_range, y_len, color)
        Gera e retorna o gráfico da função
    '''

    def __init__(self, function: str):

        '''
        atributos
        ---------
        __function
            função com uma incógnita x
        '''

        self.__function = function

    def findImage(self, x: float) -> float:

        ''' calcula a imagem de um ponto x na função especificada no
        atributo __function '''

        try:
            image = eval(self.__function)

        except NameError:
            raise NameError('Function contains unknown value(s)')

        except SyntaxError:
            raise SyntaxError('poorly formulated function')

        except ZeroDivisionError:
            raise ZeroDivisionError('Function contains division by zero')

        except ValueError:
            raise ValueError(
                'function contains math errors (Example: negative root)'
            )

        return image

    def generate_graph(
        self,
        x_range: 'tuple(int, int)' = (-50, 50),
        y_range: 'tuple(int, int)' = (-50, 50),
        x_increment: float = 0.1,
        point_color: str = 'blue',
        back_color: str = 'white',
        render_type: str = RenderType.IMAGE
    ):

        ''' Gera e retorna o gráfico da função

        parâmetros
        ----------
        x_range: 'tuple(int, int)'
            range dos valores de x no mapa cartesiano
        y_range: 'tuple(int, int)'
            range dos valores de y no mapa cartesiano
        x_increment: int
            quantidade em que o valor x será incrementado a cada ponto
        point_color: str
            cor da representação de um ponto preenchido no mapa
        back_color: str
            cor da representação de um ponto vazio no mapa
        render_type: str
            tipo de renderização do gráfico

        variáveis locais e constantes
        -----------------------------
        X_LEN: int
            tamanho do eixo x
        Y_LEN: int
            tamanho do eixo y
        cartesian_map: ScreenMap
            'ScreenMap' para representar um plano cartesiano
        points: list
            conjunto de pontos do plano cartesiano
        '''

        X_LEN = x_range[1] - x_range[0]
        Y_LEN = y_range[1] - y_range[0]

        cartesian_map = screen.ScreenMap(
            X_LEN, Y_LEN, default_color=back_color
        )
        points: 'screen.CartesianMapPoint' = []

        x = x_range[0]
        while x <= x_range[1]:

            y = self.findImage(x)
            point = screen.CartesianMapPoint(cartesian_map, x, y, point_color)

            points.append(point)
            x += x_increment

        cartesian_map.fill(points)

        return cartesian_map.render(render_type)


if __name__ == '__main__':

    ''' testando o módulo '''

    import os
    from PIL import Image

    os.system('color')

    func = Function('-tan(sqrt(abs(1-abs(x+(3/2)))))+2')

    img_render = func.generate_graph((-127, 128), (-127, 128), 0.01)
    img = Image.new('RGB', (255, 255), 'white')
    pixels = img.load()

    for i in range(img.size[1]):
        for j in range(img.size[0]):
            pixels[j, i] = img_render[i][j]

    img.show()
