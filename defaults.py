# -*- coding: utf-8 -*-
u"""Variáveis padrões pada o projeto."""

BG = "#cbfbf3"

WIDTH_COLUNM = 31

CHOOSE_BUTTONS = {
    "background": BG,
    "foreground": "#000000",
    "activebackground": BG,
    "activeforeground": "#000000",
    "relief": "solid",
    "disabledforeground": "#000000"
}

LABEL_BUTTON = {
    "background": [('disabled','#d9d9d9'), ('active','#d9d9d9')],
    "foreground": [('disabled','#a3a3a3')],
    "relief": [('pressed', 'disabled', 'sunken')],
}

STYLE_COMBOBOX = {
    "insertbackground": "#000000",
    "foreground": "#000000",
}

CHOOSE_COMBOBOX = {
    "background": BG,
    "foreground": "#000000",
    "justify": "center",
    "width": 56,
    "state": "readonly",
}

ENTRY_TEXT = {
    "background": BG,
    "foreground": "#000000",
    "justify": "left",
    "width": 129,
}

BORDA = {
    "bd": 2,
    "background": BG,
}

LABEL = {
    #"background": BG,
    #"foreground": "#000000",
    "width": 15,
    "relief": "solid",
    "justify": "center",
}

FRAME = {
    "bd": 4,
    "background": BG,
    "relief": "ridge"
}

BUTTON = {
    "width": 10,
}

COLUN_LIST = {
    "justify": "center",
    "background": BG,
    "bd": 2,
    "selectmode": "extended",
    "foreground": "#000000"
}

COMBOBOX = {
    "width": 4,
    "justify": "center",
    "state": "readonly"
}

COLUNM_TABLE_HEADER = {
    "width": 31,
    "justify": "center",
    "relief": "ridge"
}


bg_widget = "#000000"
ATENDIMENTOS = ["Cortesia", "Particular", "Amil", "Cafaz", "Cassi", "Geap", "Saúde_Caixa", "Unimed"]
