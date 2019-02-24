# coding=utf-8

from __future__ import unicode_literals
from collections import OrderedDict

from .. import Provider as ColorProvider

localized = True


class Provider(ColorProvider):
    all_colors = OrderedDict((
        ("Açafrão", "#F4C430"),
        ("Água-marinha média", "#66CDAA"),
        ("Água-marinha", "#7FFFD4"),
        ("Água", "#00FFFF"),
        ("Alizarina", "#E32636"),
        ("Amarelo brasilis", "#ECDB00"),
        ("Amarelo claro", "#FFFFE0"),
        ("Amarelo creme", "#ECD690"),
        ("Amarelo escuro", "#F2B73F"),
        ("Amarelo esverdeado", "#9ACD32"),
        ("Amarelo esverdeado", "#ADFF2F"),
        ("Amarelo ouro claro", "#FAFAD2"),
        ("Amarelo queimado", "#EEAD2D"),
        ("Amarelo", "#FFFF00"),
        ("Âmbar", "#FFBF00"),
        ("Ameixa", "#DDA0DD"),
        ("Amêndoa", "#FFEBCD"),
        ("Ametista", "#9966CC"),
        ("Aspargo", "#7BA05B"),
        ("Azul aço claro", "#B0C4DE"),
        ("Azul aço", "#4682B4"),
        ("Azul alice", "#F0F8FF"),
        ("Azul ardósia claro", "#8470FF"),
        ("Azul ardósia escuro", "#483D8B"),
        ("Azul ardósia médio", "#7B68EE"),
        ("Azul ardósia", "#6A5ACD"),
        ("Azul areado", "#B8CAD4"),
        ("Azul brasilis brilhante", "#09ACDB"),
        ("Azul brasilis", "#00BDCE"),
        ("Azul cadete", "#5F9EA0"),
        ("Azul camarada", "#054F77"),
        ("Azul celeste brilhante", "#007FFF"),
        ("Azul celeste pernambucano", "#00A4CD"),
        ("Azul celeste", "#F0FFFF"),
        ("Azul céu claro", "#87CEFA"),
        ("Azul céu profundo", "#00BFFF"),
        ("Azul céu", "#87CEEB"),
        ("Azul claro", "#ADD8E6"),
        ("Azul cobalto", "#0047AB"),
        ("Azul escuro", "#00008B"),
        ("Azul flor de milho", "#6495ED"),
        ("Azul força aérea", "#5D8AA8"),
        ("Azul furtivo", "#1E90FF"),
        ("Azul manteiga", "#a6aa3e"),
        ("Azul marinho", "#120A8F"),
        ("Azul médio", "#0000CD"),
        ("Azul meia-noite", "#191970"),
        ("Azul petróleo", "#084D6E"),
        ("Azul pólvora", "#B0E0E6"),
        ("Azul real", "#0000DD"),
        ("Azul taparuere", "#248EFF"),
        ("Azul turquesa brilhante", "#00DDFF"),
        ("Azul turquesa", "#00CCEE"),
        ("Azul violeta", "#8A2BE2"),
        ("Azul", "#0000FF"),
        ("Bege", "#F5F5DC"),
        ("Bordô", "#800000"),
        ("Borgonha", "#900020"),
        ("Branco antigo", "#FAEBD7"),
        ("Branco fantasma", "#F8F8FF"),
        ("Branco floral", "#FFFAF0"),
        ("Branco fumaça", "#F5F5F5"),
        ("Branco navajo", "#FFDEAD"),
        ("Branco", "#FFFFFF"),
        ("Brasil", "#A7F432"),
        ("Bronze", "#CD7F32"),
        ("Caqui escuro", "#BDB76B"),
        ("Caqui", "#F0E68C"),
        ("Caramelo", "#8B5742"),
        ("Cardo", "#D8BFD8"),
        ("Carmesim", "#DC143C"),
        ("Carmim carnáceo", "#960018"),
        ("Carmim clássico", "#992244"),
        ("Carmim", "#712F26"),
        ("Castanho avermelhado", "#8B0000"),
        ("Castanho claro", "#D2B48C"),
        ("Cenoura", "#ED9121"),
        ("Cereja Hollywood", "#F400A1"),
        ("Cereja", "#DE3163"),
        ("Chocolate", "#D2691E"),
        ("Ciano claro", "#E0FFFF"),
        ("Ciano escuro", "#008B8B"),
        ("Ciano", "#00FFFF"),
        ("Cinza ardósia claro", "#778899"),
        ("Cinza ardósia escuro", "#2F4F4F"),
        ("Cinza ardósia", "#708090"),
        ("Cinza claro", "#D3D3D3"),
        ("Cinza escuro", "#A9A9A9"),
        ("Cinza fosco", "#696969"),
        ("Cinza médio", "#DCDCDC"),
        ("Cinza", "#808080"),
        ("Cobre", "#B87333"),
        ("Concha", "#FFF5EE"),
        ("Coral claro", "#F08080"),
        ("Coral", "#FF7F50"),
        ("Couro", "#F0DC82"),
        ("Creme de marisco", "#FFE4C4"),
        ("Creme de menta", "#F5FFFA"),
        ("Creme", "#FFFDD0"),
        ("Dourado escuro", "#B8860B"),
        ("Dourado pálido", "#EEE8AA"),
        ("Dourado", "#DAA520"),
        ("Ébano", "#555D50"),
        ("Eminência", "#6C3082"),
        ("Escarlate", "#FF2400"),
        ("Esmeralda", "#50C878"),
        ("Eucalipto", "#44D7A8"),
        ("Fandango", "#B53389"),
        ("Feldspato", "#FDD5B1"),
        ("Ferrugem", "#B7410E"),
        ("Flerte", "#A2006D"),
        ("Fúcsia", "#FF00FF"),
        ("Fuligem", "#3D2B1F"),
        ("Glicínia", "#C9A0DC"),
        ("Glitter", "#E6E8FA"),
        ("Grená", "#831D1C"),
        ("Heliotrópio", "#DF73FF"),
        ("Herbal", "#2E8B57"),
        ("Independência", "#4C516D"),
        ("Índigo", "#4B0082"),
        ("Iris", "#5A4FCF"),
        ("Jade", "#00A86B"),
        ("Jambo", "#FF4500"),
        ("Jasmine", "#F8DE7E"),
        ("Kiwi", "#8EE53F"),
        ("Laranja claro", "#FFB84D"),
        ("Laranja escuro", "#FF8C00"),
        ("Laranja", "#FFA500"),
        ("Lavanda avermelhada", "#FFF0F5"),
        ("Lavanda", "#E6E6FA"),
        ("Lilás", "#C8A2C8"),
        ("Lima", "#FDE910"),
        ("Limão", "#00FF00"),
        ("Linho", "#FAF0E6"),
        ("Madeira", "#DEB887"),
        ("Magenta escuro", "#8B008B"),
        ("Magenta", "#FF00FF"),
        ("Malva", "#E0B0FF"),
        ("Mamão batido", "#FFEFD5"),
        ("Maná", "#F0FFF0"),
        ("Marfim", "#FFFFF0"),
        ("Marrom amarelado", "#F4A460"),
        ("Marrom claro", "#A52A2A"),
        ("Marrom rosado", "#BC8F8F"),
        ("Marrom sela", "#8B4513"),
        ("Marrom", "#964b00"),
        ("Milho Claro", "#FFF8DC"),
        ("Milho", "#FBEC5D"),
        ("Mocassim", "#FFE4B5"),
        ("Mostarda", "#FFDB58"),
        ("Naval", "#000080"),
        ("Neve", "#FFFAFA"),
        ("Nyanza", "#E9FFDB"),
        ("Ocre", "#CC7722"),
        ("Oliva escura", "#556B2F"),
        ("Oliva parda", "#6B8E23"),
        ("Oliva", "#808000"),
        ("Orquídea escura", "#9932CC"),
        ("Orquídea média", "#BA55D3"),
        ("Orquídea", "#DA70D6"),
        ("Ouro", "#FFD700"),
        ("Pardo escuro", "#CC6600"),
        ("Pardo", "#CD853F"),
        ("Pêssego", "#FFDAB9"),
        ("Prata", "#C0C0C0"),
        ("Preto", "#000000"),
        ("Púrpura média", "#9370DB"),
        ("Púrpura", "#800080"),
        ("Quantum", "#111111"),
        ("Quartzo", "#51484F"),
        ("Renda antiga", "#FDF5E6"),
        ("Rosa amoroso", "#CD69CD"),
        ("Rosa brilhante", "#FF007F"),
        ("Rosa Choque", "#FC0FC0"),
        ("Rosa claro", "#FFB6C1"),
        ("Rosa danação", "#DA69A1"),
        ("Rosa embaçado", "#FFE4E1"),
        ("Rosa forte", "#FF69B4"),
        ("Rosa profundo", "#FF1493"),
        ("Rosa", "#FFCBDB"),
        ("Roxo brasilis", "#8A008A"),
        ("Roxo", "#993399"),
        ("Rútilo", "#6D351A"),
        ("Salmão claro", "#FFA07A"),
        ("Salmão escuro", "#E9967A"),
        ("Salmão", "#FA7F72"),
        ("Sépia", "#705714"),
        ("Siena", "#FF8247"),
        ("Tangerina", "#F28500"),
        ("Terracota", "#E2725B"),
        ("Tijolo refratário", "#B22222"),
        ("Tomate", "#FF6347"),
        ("Triássico", "#FF2401"),
        ("Trigo", "#F5DEB3"),
        ("Turquesa escura", "#00CED1"),
        ("Turquesa média", "#48D1CC"),
        ("Turquesa pálida", "#AFEEEE"),
        ("Turquesa", "#40E0D0"),
        ("Urucum", "#EC2300"),
        ("Verde amarelado", "#9ACD32"),
        ("Verde claro", "#90EE90"),
        ("Verde escuro", "#006400"),
        ("Verde espectro", "#00FF00"),
        ("Verde floresta", "#228B22"),
        ("Verde fluorescente", "#CCFF33"),
        ("Verde grama", "#7CFC00"),
        ("Verde lima", "#32CD32"),
        ("Verde mar claro", "#20B2AA"),
        ("Verde mar escuro", "#8FBC8F"),
        ("Verde mar médio", "#3CB371"),
        ("Verde militar", "#78866B"),
        ("Verde pálido", "#98FB98"),
        ("Verde Paris", "#7FFF00"),
        ("Verde primavera médio", "#00FA9A"),
        ("Verde primavera", "#00FF7F"),
        ("Verde-azulado", "#008080"),
        ("Verde", "#008000"),
        ("Vermelho enegrecido", "#550000"),
        ("Vermelho escuro", "#8B0000"),
        ("Vermelho indiano", "#CD5C5C"),
        ("Vermelho violeta médio", "#C71585"),
        ("Vermelho violeta pálido", "#DB7093"),
        ("Vermelho violeta", "#D02090"),
        ("Vermelho", "#FF0000"),
        ("Violeta claro", "#F8CBF8"),
        ("Violeta escuro", "#9400D3"),
        ("Violeta", "#EE82EE"),
        ("Zinco", "#E2DDF0"),
    ))

    safe_colors = (
        'preto', 'marrom', 'verde', 'azul escuro', 'verde escuro',
        'roxo', 'laranja', 'verde claro', 'azul', 'rosa', 'violeta',
        'cinza', 'amarelo', 'magenta', 'ciano', 'branco',
    )
