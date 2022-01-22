class ColorRGB:

    ''' Classe para armazenar valores de cores RGB

    métodos
    -------
    get_color(color_name)
        Recebe o nome de uma cor e retorna o seu valor RGB
    '''

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    GRAY_LIGHT = (160, 160, 160)
    GRAY_DARK = (64, 64, 64)
    RED_LIGHT = (255, 153, 153)
    GREEN_LIGHT = (153, 255, 153)
    YELLOW_LIGHT = (255, 255, 153)
    BLUE_LIGHT = (153, 204, 255)
    MAGENTA_LIGHT = (155, 153, 255)
    CYAN_LIGHT = (153, 255, 255)
    WHITE = (255, 255, 255)

    def get_color(color_name: str):

        color_name = color_name.upper()
        color_value = getattr(ColorRGB, color_name)

        return color_value
