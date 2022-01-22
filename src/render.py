from abc import ABC, abstractmethod
from color import ColorRGB
from termcolor import colored


class RenderType:

    ''' classe para armazenar os nomes dos tipos de renderização '''

    IMAGE = 'image'
    TERM = 'term'


def render(map, gui_type: str = RenderType.IMAGE) -> str:

    ''' Função para retornar o conteúdo do map renderizado

    parâmetros
    ----------
    map: 'ScreenMap'
        'ScreenMap' chamador do renderizador
    gui_type: str
        Tipo de renderização (image, term)
    '''

    if gui_type == RenderType.IMAGE:
        return ImageMapRender(map).render()

    if gui_type == RenderType.TERM:
        return TermMapRender(map).render()


class RenderException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class MapRender(ABC):

    '''
    Classe abstrata para criação de renderizadores de objetos 'ScreenMap'

    métodos
    -------
    point_render(point)
        renderiza um ponto do 'ScreenMap'
    void_point_render()
        renderiza um ponto vazio do 'ScreenMap'
    render(): list[list]
        retorna as informações de renderização dos pontos do 'ScreenMap'
    '''

    def __init__(self, map):

        '''
        atributos
        ---------
        map: 'ScreenMap'
            O 'ScreenMap' que chamou o renderizador
        '''

        self.map = map

    @abstractmethod
    def point_render(self, point):

        '''
        renderiza um ponto do 'ScreenMap'

        parâmetros
        ----------
        point: 'MapPoint'
            Um objeto 'MapPoint' pertencente ao 'ScreenMap' chamador
            do renderizador
        '''

        pass

    @abstractmethod
    def void_point_render(self):

        ''' renderiza um ponto vazio do 'ScreenMap' '''

        pass

    def render(self) -> 'list[list]':

        '''
        retorna as informações de renderização dos pontos do 'ScreenMap'
        '''

        rendered_points = []

        for y in self.map.map:

            rendered_points.append([])
            len_rendered_points = len(rendered_points)

            for x in y:
                # x -> Valores do tipo 'MapPoint' ou 'None'

                point = self.point_render(x)
                rendered_points[len_rendered_points - 1].append(point)

        return rendered_points


class ImageMapRender(MapRender):

    '''
    Classe utilizada para renderização de objetos 'ScreenMap' no modo imagem

    métodos
    -------
    point_render(point)
        renderiza um ponto do 'ScreenMap' como uma cor RGB em uma
        tupla -> (R, G, B)
    void_point_render()
        renderiza um ponto vazio do 'ScreenMap' como uma cor RGB padrão para
        espaços vazios em uma tupla -> (R, G, B)
    '''

    def __init__(self, map):
        super().__init__(map)

    def point_render(self, point) -> 'tuple(int, int, int)':

        '''
        renderiza um ponto do 'ScreenMap' como uma cor RGB em uma
        tupla -> (R, G, B)
        '''

        try:
            if point:
                return ColorRGB.get_color(point.fill_color)

            return self.void_point_render()

        except AttributeError:
            raise RenderException('Color not accepted')

    def void_point_render(self):

        '''
        renderiza um ponto vazio do 'ScreenMap' como uma cor RGB padrão para
        espaços vazios em uma tupla -> (R, G, B)
        '''

        if self.map.default_color:
            return ColorRGB.get_color(self.map.default_color)

        return ColorRGB.WHITE


class TermMapRender(MapRender):

    '''
    Classe utilizada para renderização de objetos 'ScreenMap' no modo terminal

    atributos
    --------------------
    DISPLAY_FILL:str
        um caractere para representar campos preenchidos no terminal
    DISPLAY_VOID:str
        um caractere para representar campos vazios no terminal

    métodos
    -------
    point_render(point)
        renderiza um ponto do 'ScreenMap' como uma cor ANSI
    void_point_render()
        renderiza um ponto vazio do 'ScreenMap' como uma cor ANSI padrão se
        houver
    '''

    DISPLAY_FILL = ' '
    DISPLAY_VOID = ' '

    def __init__(self, map):
        super().__init__(map)

    def point_render(self, point) -> str:

        ''' renderiza um ponto do 'ScreenMap' como uma cor ANSI '''

        try:
            if point:
                return colored(
                            self.__class__.DISPLAY_FILL,
                            color=point.fill_color,
                            attrs=['reverse', 'blink'],
                        )

            return self.void_point_render()

        except KeyError:
            raise RenderException('Color not accepted')

    def void_point_render(self) -> str:

        '''
        renderiza um ponto vazio do 'ScreenMap' como uma cor ANSI padrão se
        houver
        '''

        if self.map.default_color:
            return colored(
                self.__class__.DISPLAY_VOID,
                color=self.map.default_color,
                attrs=['reverse', 'blink']
            )

        return self.__class__.DISPLAY_VOID
