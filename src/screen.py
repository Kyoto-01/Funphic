import render
from math import floor


class PointIsBiggerThanMapException(Exception):

    '''Lançada se o x e/ou o y de um 'MapPoint' exceder os limites de seu
    ScreenMap relacionado
    '''

    def __init__(self, msg: str = None):
        super().__init__(msg)


class MapPoint:

    ''' Os objetos desta classe representam pontos em um 'ScreenMap'

    métodos
    -------
    checkpoint()
        Faz verificações no objeto 'MapPoint'
    __getPointColor(color_name) -> str
        Recebe o nome de uma cor e retorna o seu valor ANSI
    '''

    def __init__(
        self,
        screen: 'ScreenMap',
        x: int,
        y: int,
        fill_color: str = 'WHITE'
    ):

        '''
        atributos
        ---------
        __screen: ScreenMap
            'ScreenMap' ao qual o 'MapPoint' está relacionado
        __x: int
            Posição x no 'ScreenMap'
        __y: int
            Posição y no 'ScreenMap'
        __fill_color: str
            Valor da cor de preenchimento do ponto no 'ScreenMap'
        '''

        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__fill_color = fill_color

    @property
    def screen(self):
        return self.__screen

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def fill_color(self):
        return self.__fill_color

    def checkPoint(self):

        ''' Faz verificações no objeto 'MapPoint'

        raises
        ------
        PointIsBiggerThanMapException
            Lançada se ao menos uma das condições de 'len_checker' for True
        '''

        len_checker = (
            self.__x >= self.__screen.x_len,
            self.__x < 0,
            self.__y >= self.__screen.y_len,
            self.__y < 0
        )

        if any(len_checker):
            raise PointIsBiggerThanMapException


class CartesianMapPoint(MapPoint):

    ''' Os objetos desta classe representam pontos em um 'ScreenMap'
    como se este fosse um mapa cartesiano

    métodos
    -------
    __adjust_point()
        ajusta o ponto para se comportar no 'ScreenMap' como se estivesse
        em um mapa cartesiano
    '''

    def __init__(
        self,
        screen: 'ScreenMap',
        x: float,
        y: float,
        fill_color: str = 'WHITE'
    ):
        super().__init__(screen, x, y, fill_color)
        self.__adjustPoint()

    def __adjustPoint(self):

        ''' ajusta o ponto para se comportar no 'ScreenMap' como se
        estivesse em um mapa cartesiano

        exemplos
        --------
        tamanho x do 'ScreenMap' = 5
        tamanho y do 'ScreenMap' = 5

        ( x = -1, y = 1 ) --> ( x = 1, y = 1 )
        ( x = 0, y = 0 ) --> ( x = 2, y = 2 )
        ( x = 2, y = -2 ) --> ( x = 4, y = 4)
        '''

        x_map_mid = floor(self.screen.x_len / 2)
        y_map_mid = floor(self.screen.y_len / 2)

        self.x = floor(x_map_mid + self.x)

        # subtrai de screen.y_len para inverter o gráfico, que por padrão
        # é exibido ao contrário
        self.y = floor(self.screen.y_len - (y_map_mid + self.y))


class ScreenMap:

    '''
    Classe para representar a estrutura de um gráfico no console

    ...

    métodos
    ----------------------
    fill(filled_fields)
        função para preencher o __map
    render()
        Função para retornar o conteúdo do map renderizado
    '''

    def __init__(self, x_len: int, y_len: int, default_color: str = None):

        '''
        atributos
        ---------
        __x_len: int
            Tamanho horizontal do 'ScreenMap'
        __y_len: int
            Tamanho vertical do 'ScreenMap'
        __default_color: str
            cor de preenchimento para espaços vazios
        __map: list[list['MapPoint']]
            Campos preenchiveis do 'ScreenMap'
        '''

        self.__x_len = x_len
        self.__y_len = y_len
        self.__default_color = default_color
        self.__map: 'list[list["MapPoint"]]' = [
            [None] * x_len for i in range(y_len)
        ]

    @property
    def x_len(self):
        return self.__x_len

    @property
    def y_len(self):
        return self.__y_len

    @property
    def default_color(self):
        return self.__default_color

    @property
    def map(self):
        return self.__map

    @default_color.setter
    def default_color(self, value):
        self.__default_color = value

    def fill(self, filled_fields: 'list[MapPoint]'):

        ''' função para preencher o __map '''

        for mp in filled_fields:
            try:
                mp.checkPoint()

                x = mp.x
                y = mp.y
                self.__map[y][x] = mp

            except PointIsBiggerThanMapException:
                del(mp)

        return self.__map

    def render(self, gui_type: str = render.RenderType.IMAGE):

        ''' Função para retornar o conteúdo do map renderizado '''

        return render.render(self, gui_type)


if __name__ == '__main__':

    ''' Testando o módulo '''

    import os
    from PIL import Image

    os.system('color')

    screen = ScreenMap(255, 255, 'blue')
    color = 'red'
    draw = [
        CartesianMapPoint(screen, 2, 0, color),
        CartesianMapPoint(screen, 3, 0, color),
        CartesianMapPoint(screen, 1, 1, color),
        CartesianMapPoint(screen, 2, 1, color),
        CartesianMapPoint(screen, 3, 1, color),
        CartesianMapPoint(screen, 4, 1, color),
        CartesianMapPoint(screen, 1, 2, color),
        CartesianMapPoint(screen, 2, 2, color),
        CartesianMapPoint(screen, 4, 2, color),
        CartesianMapPoint(screen, 1, 3, color),
        CartesianMapPoint(screen, 2, 3, color),
        CartesianMapPoint(screen, 3, 3, color),
        CartesianMapPoint(screen, 4, 3, color),
        CartesianMapPoint(screen, 1, 4, color),
        CartesianMapPoint(screen, 2, 4, color),
        CartesianMapPoint(screen, 1, 5, color),
        CartesianMapPoint(screen, 2, 5, color),
        CartesianMapPoint(screen, 3, 5, color),
        CartesianMapPoint(screen, 4, 5, color)
    ]

    screen.fill(draw)

    img_render = screen.render()
    img = Image.new('RGB', (255, 255), 'white')
    pixels = img.load()

    for i in range(img.size[1]):
        for j in range(img.size[0]):
            pixels[j, i] = img_render[i][j]

    img.show()
