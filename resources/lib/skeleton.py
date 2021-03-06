# -*- coding: utf-8 -*-
"""
    Catch-up TV & More
    Copyright (C) 2016  SylvainCecchetto

    This file is part of Catch-up TV & More.

    Catch-up TV & More is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Catch-up TV & More is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with Catch-up TV & More; if not, write to the Free Software Foundation,
    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from resources.lib import common

'''
SKELETON dictionary corresponds to the architecture of each menu of the addon
(elt1, elt2) -->
    elt1: label
    elt2: next function to call
'''
SKELETON = {
    ('root', 'generic_menu'): {

        ('live_tv', 'generic_menu'): {

            ('fr', 'build_live_tv_menu'): [
                ('tf1', 'none'),
                ('france-2', 'none'),
                ('france-3', 'none'),
                ('france-5', 'none'),
                ('canalplus', 'none'),
                ('c8', 'none'),
                ('tmc', 'none'),
                ('tfx', 'none'),
                ('nrj12', 'none'),
                ('france-4', 'none'),
                ('bfmtv', 'none'),
                ('cnews', 'none'),
                ('cstar', 'none'),
                ('gulli', 'none'),
                ('france-o', 'none'),
                ('tf1-series-films', 'none'),
                ('lequipe', 'none'),
                ('numero23', 'none'),
                ('cherie25', 'none'),
                ('la_1ere', 'none'),
                ('franceinfo', 'none'),
                ('bfmbusiness', 'none'),
                ('rmc', 'none'),
                ('lci', 'none'),
                ('lcp', 'none'),
                ('rmcdecouverte', 'none'),
                ('publicsenat', 'none'),
                ('france3regions', 'none'),
                ('francetvsport', 'none'),
                ('gong', 'none'),
                ('bfmparis', 'none'),
                ('melodytv', 'none'),
                ('virginradiotv', 'none')
            ],

            ('be', 'build_live_tv_menu'): [
                ('rtc', 'none'),
                ('telemb', 'none'),
                ('een', 'none'),
                ('canvas', 'none'),
                ('ketnet', 'none'),
                ('auvio', 'none'),
                ('tvlux', 'none'),
                ('bx1', 'none')
            ],

            ('ca', 'build_live_tv_menu'): [
                ('telequebec', 'none'),
                ('yestv', 'none'),
                ('tva', 'none'),
                ('icitele', 'none')
            ],

            ('ch', 'build_live_tv_menu'): [
                ('rougetv', 'none'),
                ('rts', 'none'),
                ('rsi', 'none'),
                ('srf', 'none'),
                ('rtr', 'none')
            ],

            ('uk', 'build_live_tv_menu'): [
                ('blaze', 'none'),
                ('skynews', 'none'),
                ('stv', 'none'),
                ('stv2', 'none')
            ],

            ('wo', 'build_live_tv_menu'): [
                ('arirang', 'none'),
                ('arte', 'none'),
                ('bvn', 'none'),
                ('euronews', 'none'),
                ('france24', 'none'),
                ('icitelevision', 'none'),
                ('nhkworld', 'none'),
                ('dw', 'none'),
                ('tv5monde', 'none'),
                ('tivi5monde', 'none'),
                ('souvenirsfromearth', 'none'),
                ('qvc', 'none'),
                ('icirdi', 'none'),
                ('cgtn', 'none'),
                ('cgtndocumentary', 'none'),
                ('paramountchannel', 'none'),
                ('afriquemedia', 'none')
            ],

            ('us', 'build_live_tv_menu'): [
                ('cbsnews', 'none'),
                ('tbd', 'none'),
                ('abcnews', 'none')
            ],

            ('pl', 'build_live_tv_menu'): [
                ('tvp', 'none')
            ],

            ('es', 'build_live_tv_menu'): [
                ('telecinco', 'none'),
                ('cuatro', 'none'),
                ('fdf', 'none'),
                ('boing', 'none'),
                ('energy', 'none'),
                ('divinity', 'none'),
                ('bemad', 'none'),
                ('realmadridtv', 'none')
            ],

            ('jp', 'build_live_tv_menu'): [
                ('ntvnews24', 'none')
            ]
        },

        ('replay', 'generic_menu'): {

            ('be', 'generic_menu'): [
                ('auvio', 'replay_entry'),
                ('brf', 'replay_entry'),
                ('rtl_tvi', 'replay_entry'),
                ('plug_rtl', 'replay_entry'),
                ('club_rtl', 'replay_entry'),
                ('vrt', 'replay_entry'),
                ('telemb', 'replay_entry'),
                ('rtc', 'replay_entry'),
                ('tvlux', 'replay_entry'),
                ('rtl_info', 'replay_entry'),
                ('bel_rtl', 'replay_entry'),
                ('contact', 'replay_entry'),
                ('bx1', 'replay_entry')
            ],

            ('ca', 'generic_menu'): [
                ('tv5', 'replay_entry'),
                ('unis', 'replay_entry'),
                ('telequebec', 'replay_entry'),
                ('tva', 'replay_entry'),
                ('icitele', 'replay_entry')
            ],

            ('fr', 'generic_menu'): [
                ('tf1', 'replay_entry'),
                ('france-2', 'replay_entry'),
                ('france-3', 'replay_entry'),
                ('canalplus', 'replay_entry'),
                ('france-5', 'replay_entry'),
                ('m6', 'replay_entry'),
                ('c8', 'replay_entry'),
                ('w9', 'replay_entry'),
                ('tmc', 'replay_entry'),
                ('tfx', 'replay_entry'),
                ('nrj12', 'replay_entry'),
                ('france-4', 'replay_entry'),
                ('bfmtv', 'replay_entry'),
                ('cnews', 'replay_entry'),
                ('cstar', 'replay_entry'),
                ('gulli', 'replay_entry'),
                ('france-o', 'replay_entry'),
                ('tf1-series-films', 'replay_entry'),
                ('lequipe', 'replay_entry'),
                ('6ter', 'replay_entry'),
                ('numero23', 'replay_entry'),
                ('cherie25', 'replay_entry'),
                ('la_1ere', 'replay_entry'),
                ('franceinfo', 'replay_entry'),
                ('bfmbusiness', 'replay_entry'),
                ('rmc', 'replay_entry'),
                ('01net', 'replay_entry'),
                ('tfou', 'replay_entry'),
                ('xtra', 'replay_entry'),
                ('lci', 'replay_entry'),
                ('lcp', 'replay_entry'),
                ('rmcdecouverte', 'replay_entry'),
                ('stories', 'replay_entry'),
                ('bruce', 'replay_entry'),
                ('crazy_kitchen', 'replay_entry'),
                ('home', 'replay_entry'),
                ('styles', 'replay_entry'),
                ('comedy', 'replay_entry'),
                ('publicsenat', 'replay_entry'),
                ('histoire', 'replay_entry'),
                ('tvbreizh', 'replay_entry'),
                ('ushuaiatv', 'replay_entry'),
                ('studio-4', 'replay_entry'),
                ('irl', 'replay_entry'),
                ('seasons', 'replay_entry'),
                ('comedie', 'replay_entry'),
                ('les-chaines-planete', 'replay_entry'),
                ('golfplus', 'replay_entry'),
                ('cineplus', 'replay_entry'),
                ('infosportplus', 'replay_entry'),
                ('gameone', 'replay_entry'),
                ('francetveducation', 'replay_entry'),
                ('gong', 'replay_entry'),
                ('francetvsport', 'replay_entry'),
                ('onzeo', 'replay_entry'),
                ('fun_radio', 'replay_entry'),
                ('slash', 'replay_entry'),
                ('polar-plus', 'replay_entry'),
                ('france3regions', 'replay_entry'),
                ('culturebox', 'replay_entry')
            ],

            ('jp', 'generic_menu'): [
                ('nhknews', 'replay_entry'),
                ('nhklifestyle', 'replay_entry'),
                ('tbsnews', 'replay_entry'),
                ('ntv', 'replay_entry'),
                ('ex', 'replay_entry'),
                ('tbs', 'replay_entry'),
                ('tx', 'replay_entry'),
                # ('cx': 'replay_entry'), (Protected by DRM)
                ('mbs', 'replay_entry'),
                ('abc', 'replay_entry'),
                ('ytv', 'replay_entry')
            ],

            ('ch', 'generic_menu'): [
                ('rts', 'replay_entry'),
                ('rsi', 'replay_entry'),
                ('srf', 'replay_entry'),
                ('rtr', 'replay_entry'),
                ('swissinfo', 'replay_entry'),
                # ('rougetv', 'replay_entry'),
                ('tvm3', 'replay_entry'),
                ('becurioustv', 'replay_entry')
            ],

            ('uk', 'generic_menu'): [
                ('blaze', 'replay_entry'),
                ('dave', 'replay_entry'),
                ('really', 'replay_entry'),
                ('yesterday', 'replay_entry'),
                ('drama', 'replay_entry'),
                ('skynews', 'replay_entry'),
                ('skysports', 'replay_entry'),
                ('questtv', 'replay_entry')
            ],

            ('wo', 'generic_menu'): [
                ('tv5mondeafrique', 'replay_entry'),
                ('arte', 'replay_entry'),
                ('france24', 'replay_entry'),
                ('nhkworld', 'replay_entry'),
                ('tv5monde', 'replay_entry'),
                ('tivi5monde', 'replay_entry'),
                ('bvn', 'replay_entry'),
                ('icitelevision', 'replay_entry'),
                ('mtv', 'replay_entry'),
                ('arirang', 'replay_entry'),
                ('beinsports', 'replay_entry'),
                # ('paramountchannel', 'replay_entry'),
                ('afriquemedia', 'replay_entry')
            ],

            ('us', 'generic_menu'): [
                ('tbd', 'replay_entry'),
                ('nycmedia', 'replay_entry')
            ]
        },
        ('websites', 'generic_menu'): [
            ('allocine', 'website_entry'),
            ('tetesaclaques', 'website_entry'),
            ('taratata', 'website_entry'),
            ('noob', 'website_entry'),
            ('culturepub', 'website_entry'),
            ('autoplus', 'website_entry'),
            ('notrehistoirech', 'website_entry'),
            ('30millionsdamis', 'website_entry'),
            ('elle', 'website_entry'),
            ('nytimes', 'website_entry'),
            ('fosdem', 'website_entry'),
            ('ina', 'website_entry')
        ]

    }
}


'''
SKELETON dictionary is the bridge between
the item in Kodi and the real folder location on disk
'''
FOLDERS = {
    'live_tv': 'channels',
    'replay': 'channels'
}


'''
CHANNELS dictionary is the bridge between
the channel name and his corresponding python file
'''
CHANNELS = {
    'auvio': 'rtbf',
    'brf': 'brf',
    'rtl_tvi': 'rtlbe',
    'plug_rtl': 'rtlbe',
    'club_rtl': 'rtlbe',
    'rtl_info': 'rtlbe',
    'bel_rtl': 'rtlbe',
    'contact': 'rtlbe',
    'vrt': 'vrt',
    'telemb': 'telemb',
    'rtc': 'rtc',
    'tv5': 'tv5',
    'unis': 'tv5',
    'yestv': 'yestv',
    'telequebec': 'telequebec',
    'rts': 'srgssr',
    'rsi': 'srgssr',
    'srf': 'srgssr',
    'rtr': 'srgssr',
    'swissinfo': 'srgssr',
    'rougetv': 'rougetv',
    'tf1': 'tf1',
    'france-2': 'francetv',
    'france-3': 'francetv',
    'canalplus': 'mycanal',
    'france-5': 'francetv',
    'm6': '6play',
    'c8': 'mycanal',
    'w9': '6play',
    'tmc': 'tf1',
    'tfx': 'tf1',
    'nrj12': 'nrj',
    'france-4': 'francetv',
    'bfmtv': 'bfmtv',
    'bfmparis': 'bfmtv',
    'cnews': 'cnews',
    'cstar': 'mycanal',
    'gulli': 'gulli',
    'france-o': 'francetv',
    'tf1-series-films': 'tf1',
    'lequipe': 'lequipe',
    '6ter': '6play',
    'numero23': 'numero23',
    'cherie25': 'nrj',
    'la_1ere': 'la_1ere',
    'franceinfo': 'franceinfo',
    'bfmbusiness': 'bfmtv',
    'rmc': 'bfmtv',
    '01net': 'bfmtv',
    'tfou': 'tf1',
    'xtra': 'tf1',
    'lci': 'tf1',
    'lcp': 'lcp',
    'rmcdecouverte': 'bfmtv',
    'stories': '6play',
    'bruce': '6play',
    'crazy_kitchen': '6play',
    'home': '6play',
    'styles': '6play',
    'comedy': '6play',
    'fun_radio': '6play',
    'publicsenat': 'publicsenat',
    'france3regions': 'france3regions',
    'francetvsport': 'francetvsport',
    'histoire': 'tf1thematiques',
    'tvbreizh': 'tf1thematiques',
    'ushuaiatv': 'tf1thematiques',
    'studio-4': 'nouvellesecritures',
    'irl': 'nouvellesecritures',
    'seasons': 'mycanal',
    'comedie': 'mycanal',
    'les-chaines-planete': 'mycanal',
    'golfplus': 'mycanal',
    'cineplus': 'mycanal',
    'infosportplus': 'mycanal',
    'gameone': 'gameone',
    'francetveducation': 'francetveducation',
    'gong': 'gong',
    'nhknews': 'nhk',
    'nhklifestyle': 'nhk',
    'tbsnews': 'tbs',
    'blaze': 'blaze',
    'dave': 'uktvplay',
    'really': 'uktvplay',
    'yesterday': 'uktvplay',
    'drama': 'uktvplay',
    'skynews': 'sky',
    'skysports': 'sky',
    'tv5mondeafrique': 'tv5monde',
    'arte': 'arte',
    'euronews': 'euronews',
    'france24': 'france24',
    'nhkworld': 'nhkworld',
    'tv5monde': 'tv5monde',
    'tivi5monde': 'tv5monde',
    'bvn': 'bvn',
    'icitelevision': 'icitelevision',
    'mtv': 'mtv',
    'arirang': 'arirang',
    'dw': 'dw',
    'ntv': 'tver',
    'ex': 'tver',
    'tbs': 'tver',
    'tx': 'tver',
    # 'cx': 'tver', (Protected by DRM)
    'mbs': 'tver',
    'abc': 'tver',
    'ytv': 'tver',
    'tvm3': 'tvm3',
    'tva': 'tva',
    'tvlux': 'tvlux',
    'beinsports': 'beinsports',
    'stv': 'stv',
    'stv2': 'stv',
    'onzeo': 'onzeo',
    'souvenirsfromearth': 'souvenirsfromearth',
    'qvc': 'qvc',
    'cbsnews': 'cbsnews',
    'melodytv': 'melodytv',
    'bx1': 'bx1',
    'tvp': 'tvp',
    'slash': 'francetv',
    'telecinco': 'mitele',
    'cuatro': 'mitele',
    'fdf': 'mitele',
    'boing': 'mitele',
    'energy': 'mitele',
    'divinity': 'mitele',
    'bemad': 'mitele',
    'icirdi': 'icirdi',
    'icitele': 'icitele',
    'polar-plus': 'mycanal',
    'virginradiotv': 'virginradiotv',
    'tbd': 'tbd',
    'nycmedia': 'nycmedia',
    'cgtn': 'cgtn',
    'cgtndocumentary': 'cgtn',
    'culturebox': 'culturebox',
    'ntvnews24': 'ntvnews24',
    'paramountchannel': 'paramountchannel',
    'questtv': 'questtv',
    'realmadridtv': 'realmadridtv',
    'afriquemedia': 'afriquemedia',
    'becurioustv': 'becurioustv',
    'een': 'vrt',
    'canvas': 'vrt',
    'ketnet': 'vrt',
    'abcnews': 'abcnews'
}

'''
LABELS dict is only used to retrieve correct element in english strings.po
'''
LABELS = {

    # root
    'live_tv': 'Live TV',
    'replay': 'Catch-up TV',
    'websites': 'Websites',

    # Countries
    'be': 'Belgium',
    'fr': 'France',
    'jp': 'Japan',
    'ch': 'Switzerland',
    'uk': 'United Kingdom',
    'wo': 'International',
    'ca': 'Canada',
    'us': 'United State of America',
    'pl': 'Poland',
    'es': 'Spain',

    # Belgium channels / live TV
    'auvio': 'RTBF Auvio (La Une, La deux, La Trois, ...)',
    'brf': 'BRF Mediathek',
    'rtl_tvi': 'RTL-TVI',
    'plug_rtl': 'PLUG RTL',
    'club_rtl': 'CLUB RTL',
    'vrt': 'VRT NU',
    'telemb': 'Télé MB',
    'rtc': 'RTC Télé Liège',
    'tvlux': 'TV Lux',
    'contact': 'Contact',
    'bel_rtl': 'BEL RTL',
    'rtl_info': 'RTL INFO',
    'bx1': 'BX1',
    'een': 'Eén',
    'canvas': 'Canvas',
    'ketnet': 'Ketnet',

    # Canadian channels / live TV
    'tv5': 'TV5',
    'unis': 'UNIS',
    'yestv': 'YES TV (' + common.PLUGIN.get_setting('yestv.region') + ')',
    'telequebec': 'Télé-Québec',
    'tva': 'TVA',
    'icitele': 'ICI Télé',

    # Switzerland channels / live TV
    'rts': 'RTS',
    'rsi': 'RSI',
    'srf': 'SRF',
    'rtr': 'RTR',
    'swissinfo': 'SWISSINFO',
    'rougetv': 'Rouge TV',
    'tvm3': 'TVM3',
    'becurioustv': 'BeCurious TV',

    # French channels / live TV
    'tf1': 'TF1',
    'france-2': 'France 2',
    'france-3': 'France 3',
    'canalplus': 'Canal +',
    'france-5': 'France 5',
    'm6': 'M6',
    'c8': 'C8',
    'w9': 'W9',
    'tmc': 'TMC',
    'tfx': 'TFX',
    'nrj12': 'NRJ 12',
    'france-4': 'France 4',
    'bfmtv': 'BFM TV',
    'bfmparis': 'BFM Paris',
    'cnews': 'CNews',
    'cstar': 'CStar',
    'gulli': 'Gulli',
    'france-o': 'France Ô',
    'tf1-series-films': 'TF1 Séries Films',
    'lequipe': 'L\'Équipe',
    '6ter': '6ter',
    'numero23': 'Numéro 23',
    'cherie25': 'Chérie 25',
    'la_1ere': 'La 1ère (' + common.PLUGIN.get_setting('la_1ere.region') + ')',
    'franceinfo': 'France Info',
    'bfmbusiness': 'BFM Business',
    'rmc': 'RMC',
    '01net': '01Net TV',
    'tfou': 'Tfou (MYTF1)',
    'xtra': 'Xtra (MYTF1)',
    'lci': 'LCI',
    'lcp': 'LCP Assemblée Nationale',
    'rmcdecouverte': 'RMC Découverte HD24',
    'stories': 'Stories (6play)',
    'bruce': 'Bruce (6play)',
    'crazy_kitchen': 'Crazy Kitchen (6play)',
    'home': 'Home Time (6play)',
    'styles': 'Sixième Style (6play)',
    'comedy': 'Comic (6play)',
    'fun_radio': 'Fun Radio',
    'publicsenat': 'Public Sénat',
    'france3regions': 'France 3 Régions (' + common.PLUGIN.get_setting('france3.region') + ')',
    'francetvsport': 'France TV Sport (francetv)',
    'histoire': 'Histoire',
    'tvbreizh': 'TV Breizh',
    'ushuaiatv': 'Ushuaïa TV',
    'studio-4': 'Studio 4 (francetv)',
    'irl': 'IRL (francetv)',
    'seasons': 'Seasons',
    'comedie': 'Comédie +',
    'les-chaines-planete': 'Les chaînes planètes +',
    'golfplus': 'Golf +',
    'cineplus': 'Ciné +',
    'infosportplus': 'INFOSPORT+',
    'gameone': 'Game One',
    'francetveducation': 'France TV Education (francetv)',
    'gong': 'Gong',
    'onzeo': 'Onzéo',
    'melodytv': 'Melody TV',
    'slash': 'France tv slash',
    'polar-plus': 'Polar+',
    'virginradiotv': 'Virgin Radio TV',
    'culturebox': 'Culturebox (francetv)',

    # Japan channels / live TV
    'nhknews': 'NHK ニュース',
    'nhklifestyle': 'NHKらいふ',
    'tbsnews': 'TBS ニュース',
    'ntv': '日テレ',
    'ex': 'テレビ朝日',
    'tbs': 'TBSテレビ',
    'tx': 'テレビ東京',
    # 'cx': 'フジテレビ', (Protected by DRM)
    'mbs': 'MBSテレビ',
    'abc': '朝日放送株式会社',
    'ytv': '読売テレビ',
    'ntvnews24': '日テレ News24',

    # United Kingdom channels / live TV
    'blaze': 'Blaze',
    'dave': 'Dave',
    'really': 'Really',
    'yesterday': 'Yesterday',
    'drama': 'Drama',
    'skynews': 'Sky News',
    'skysports': 'Sky Sports',
    'stv': 'STV',
    'stv2': 'STV 2',
    'questtv': 'Quest TV',

    # International channels / live TV
    'tv5mondeafrique': 'TV5Monde Afrique',
    'arte': 'Arte (' + common.PLUGIN.get_setting('arte.language') + ')',
    'euronews': 'Euronews (' + common.PLUGIN.get_setting('euronews.language') + ')',
    'france24': 'France 24 (' + common.PLUGIN.get_setting('france24.language') + ')',
    'nhkworld': 'NHK World (' + common.PLUGIN.get_setting('nhkworld.country') + ')',
    'tv5monde': 'TV5Monde',
    'tivi5monde': 'Tivi 5Monde',
    'bvn': 'BVN',
    'icitelevision': 'ICI Télévision',
    'mtv': 'MTV (' + common.PLUGIN.get_setting('mtv.language') + ')',
    'arirang': 'Arirang (아리랑)',
    'dw': 'DW (' + common.PLUGIN.get_setting('dw.language') + ')',
    'beinsports': 'Bein Sports (' + common.PLUGIN.get_setting('beinsports.language') + ')',
    'souvenirsfromearth': 'Souvenirs From Earth',
    'qvc': 'QVC (' + common.PLUGIN.get_setting('qvc.language') + ')',
    'icirdi': 'ICI RDI',
    'cgtn': 'CGTN (' + common.PLUGIN.get_setting('cgtn.language') + ')',
    'cgtndocumentary': 'CGTN Documentary',
    'paramountchannel': 'Paramount Channel (' + common.PLUGIN.get_setting('paramountchannel.language') + ')',
    'afriquemedia': 'Afrique Media',

    # United State of America channels / live TV
    'cbsnews': 'CBS News',
    'tbd': 'TBD',
    'nycmedia': 'NYC Media',
    'abcnews': 'ABC News',

    # Poland channels / live TV
    'tvp': 'TVP',

    # Spanish channels / live TV
    'telecinco': 'Telecinco',
    'cuatro': 'Cuatro',
    'fdf': 'Factoria de Ficcion',
    'boing': 'Boing',
    'energy': 'Energy TV',
    'divinity': 'Divinity',
    'bemad': 'Be Mad',
    'realmadridtv': 'Realmadrid TV (' + common.PLUGIN.get_setting('realmadridtv.language') + ')',

    # Websites
    'allocine': 'Allociné',
    'tetesaclaques': 'Au pays des Têtes à claques',
    'taratata': 'Taratata',
    'noob': 'Noob TV',
    'culturepub': 'Culturepub',
    'autoplus': 'Auto Plus',
    'notrehistoirech': 'Notre Histoire',
    '30millionsdamis': '30 Millions d\'Amis',
    'elle': 'Elle',
    'nytimes': 'New York Times',
    'fosdem': 'Fosdem',
    'ina': 'Ina'
}
