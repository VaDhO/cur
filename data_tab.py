import pandas as pd


class Model():
    tab1 = pd.DataFrame()
    tab3 = pd.DataFrame()
    tab4 = pd.DataFrame()
    tab5 = pd.DataFrame()
    tab6 = pd.DataFrame()

    def __init__(self):
        self.tab1 = pd.DataFrame(
            {'СХО': [707656.798, 11.4, "", 1882.82, "", 0.95, "", 1.4, "", "", "", 3921.0, "", "", "",
                     "", "", 6475387.3, "", "", "", "", 6667.94, 12051512.0, "", "", 3841.0, 8607.0,
                     300.0, 2941.0, "", "", "", "", "", "", "", "", "", ""],
             'ПП': ["", "", "", "", "", "", "", "", "", "", "", 7953306.4, "", 607.83, "", "", "", "",
                    "", "", "", "", 7187.6, "", "", "", "", 8948.0, 450.0, "", "", "", "", "", "", "",
                    "", "", "", ""],
             'Нормативы': ["", "", "", "", "", "", "", "", "", "", "", "", "", 0.12, "", "", "", "", "",
                           "", "", "", "", "", "", "", 1.4, 1.5, "", "", "", "", "", "", "", "", "", "",
                           "", ""],
             'МВР': ["", "", "", "", "", 0.95, "", 0.9, "", "", 0.8, "", "", "", "", "", 0.98, "", 0.1,
                     "", 0.1, "", "", "", "", "", 3841.0, "", "", "", "", "", "", "", "", "", "", "",
                     "", ""],
             'МЭ': ["", "", "", "", "", 0.92, "", 1.1, "", "", 0.75, "", "", "", "", "", 0.95, "", 0.2,
                    "", 0.25, "", "", "", "", "", "", "", 300.0, "", "", "", "", "", "", "", "", "", "",
                    ""],
             'МПСПДСН': ["", "", "", "", "", 0.99, "", 0.8, "", "", 0.55, "", 0.9, "", "", "", 0.98, "",
                         0.02, "", 0.05, "", "", "", "", 0.7, "", "", "", "", "", "", "", "", "", "",
                         "", "", "", ""],
             'МПСПОУ': ["", "", "", "", "", 0.98, "", 1.0, "", "", 0.54, "", 1.3, "", "", "", 0.98, "",
                        0.0, "", 0.1, "", "", "", "", 0.9, "", "", "", "", "", "", "", "", "", "", "",
                        "", "", ""],
             'МПСПВР': ["", "", "", "", "", 0.95, "", 1.0, 1882.82, "", 0.54, "", 1.0, "", "", "", 0.97,
                        "", 0.08, "", 0.1, "", "", "", "", 1.0, "", "", "", "", "", "", "", "", "", "",
                        "", "", "", ""],
             'МПСПЭ': ["", "", "", "", "", 0.92, "", 1.1, "", "", 0.53, "", 1.2, "", "", "", 0.96, "",
                       0.1, "", 0.25, "", "", "", "", 1.7, "", "", 450.0, "", "", "", "", "", "", "",
                       "", "", "", ""],
             'МПППВР': ["", "", "", "", "", 0.95, "", 0.9, "", "", 0.55, "", 0.9, "", "", "", 0.98, "",
                        0.1, "", 0.1, "", "", "", "", 1.0, "", "", "", "", "", "", "", "", "", "", "",
                        "", "", ""],
             'МПППЭ': ["", "", "", "", "", 0.92, "", 1.1, "", "", 0.54, "", 1.1, "", "", "", 0.96, "",
                       0.2, "", 0.25, "", "", "", "", 1.5, "", "", 450.0, "", "", "", "", "", "", "",
                       "", "", "", ""],
             'ИМ': ["", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "",
                    "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
             'ИМПСП': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                       "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
             'ИМППП': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                       "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
             'ИМПВР': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                       "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
             'ИМПЭ': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
             'ИВМП': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
             'ИММП': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
             'ИСХ': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]})

        self.tab5 = pd.DataFrame({'СХО': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                                     ,
                                  'ВРПМВР': ["", "", "", "", "", "", "", "", 0.6, 0.95, 0.9, 0.8, "", 0.98, 0.1, 0.1,
                                             ""]
                                     ,
                                  'ВРПМЭ': ["", "", "", "", "", "", 0.4, "", 0.4, 0.92, 1.1, 0.75, "", 0.95, 0.2, 0.25,
                                            ""]
                                     ,
                                  'ВРПМПСПСН': ["", "", "", "", "", "", "", "", 0.1, 0.99, 0.8, 0.55, 0.9, 0.98, 0.02,
                                                0.05,
                                                0.7]
                                     ,
                                  'ВРПМПСПОУ': ["", "", "", "", "", "", "", "", 0.3, 0.98, 1.0, 0.54, 1.3, 0.98, 0.0,
                                                0.1,
                                                0.9]
                                     ,
                                  'ВРПМПСПВР': ["", "", "", "", "", "", "", "", 0.4, 0.95, 1.0, 0.54, 1.0, 0.97, 0.08,
                                                0.1,
                                                1.0]
                                     ,
                                  'ВРПМПСПЭ': ["", "", "", "", "", "", "", 0.3, 0.2, 0.92, 1.1, 0.53, 1.2, 0.96, 0.1,
                                               0.25,
                                               1.7]
                                     ,
                                  'ВРПМПППВР': ["", "", "", "", "", "", "", "", 0.6, 0.95, 0.9, 0.55, 0.9, 0.98, 0.1,
                                                0.1,
                                                1.0]
                                     ,
                                  'ВРПМПППЭ': ["", "", "", "", "", "", 0.6, 0.7, 0.4, 0.92, 1.1, 0.54, 1.1, 0.96, 0.2,
                                               0.25,
                                               1.5]})

        self.tab6 = pd.DataFrame({'НСВМ': ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                                     , 'СХО': [1.0, 1.0, "", 1.0, 1.0, "", "", "", "", "", "", "", "", "", "", "", ""]
                                     ,
                                  'ВРПМВР': [1.0, "", 1.0, "", 1.0, "", "", "", 1.0, 1.0, 1.0, 1.0, "", 1.0, 1.0, 1.0,
                                             ""]
                                     ,
                                  'ВРПМЭ': [1.0, "", 1.0, "", 1.0, "", 1.0, "", 1.0, 1.0, 1.0, 1.0, "", 1.0, 1.0, 1.0,
                                            ""]
                                     ,
                                  'ВРПМПСПСН': [1.0, "", 1.0, "", 1.0, "", "", "", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                1.0,
                                                1.0]
                                     ,
                                  'ВРПМПСПОУ': [1.0, "", 1.0, "", 1.0, "", "", "", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                1.0,
                                                1.0]
                                     ,
                                  'ВРПМПСПВР': [1.0, "", 1.0, "", 1.0, "", "", "", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                1.0,
                                                1.0]
                                     ,
                                  'ВРПМПСПЭ': [1.0, "", 1.0, "", 1.0, "", "", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                               1.0,
                                               1.0]
                                     ,
                                  'ВРПМПППВР': [1.0, "", 1.0, "", 1.0, "", "", "", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                1.0,
                                                1.0]
                                     ,
                                  'ВРПМПППЭ': [1.0, "", 1.0, "", 1.0, "", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                               1.0,
                                               1.0]})
        self.tab3 = pd.DataFrame({'ед.изм': ['т', 'км', 'тыс.т км', 'тыс.руб', 'тыс.руб', 'тыс.руб', '', '', 'тыс.руб.',
                                             0.05, 0.04, 0.03, 'тыс.руб.', 'тыс.руб.', 'тыс.руб.', 'тыс.руб.']
                                     ,
                                  'ЭФиДГ1Э': [104.6, 50.0, '', 0.3031, 0.043, '', '', '', '', '', '', '', '', '', '',
                                              '']
                                     ,
                                  'ЭФиДГ1П': [104.6, 1340.0, '', 0.388, 22.543, '', '', '', '', '', '', '', '', '', '',
                                              '']
                                     ,
                                  'ЭФиДГ2РП': [44.8, 250.0, '', 0.388, 1.733, '', '', '', '', '', '', '', '', '', '',
                                               '']
                                     ,
                                  'ЭФиДГ2МП': [44.8, 1200.0, '', 0.671, 59.7, '', '', '', '', '', '', '', '', '', '',
                                               '']
                                     ,
                                  'ЭФиДГ2МПН': [44.8, 800.0, '', 0.671, 104.5, '', '', '', '', '', '', '', '', '', '',
                                                '']
                                     , 'ЭФиДГВЗЖД': [104.6, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
                                     , 'ЭФиДГВЗВТ': [44.8, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
                                     , 'В': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']})

        self.tab4 = pd.DataFrame({'ед.изм': ['т', 'км', 'тыс.т км', 'тыс.руб', 'тыс.руб', 'тыс.руб', '', '', 'тыс.руб.',
                                             0.05, 0.04, 0.03, 'тыс.руб.', 'тыс.руб.', 'тыс.руб.', 'тыс.руб.']
                                     ,
                                  'ЭФиДГ1Э': [106151.0, 50.0, '', 0.3031, 0.043, '', '', '', '', '', '', '', '', '', '',
                                              '']
                                     ,
                                  'ЭФиДГ1П': [106151.0, 1340.0, '', 0.388, 22.543, '', '', '', '', '', '', '', '', '', '',
                                              '']
                                     ,
                                  'ЭФиДГ2РП': [45493.0, 250.0, '', 0.388, 1.733, '', '', '', '', '', '', '', '', '', '',
                                               '']
                                     ,
                                  'ЭФиДГ2МП': [45493.0, 1200.0, '', 0.671, 59.7, '', '', '', '', '', '', '', '', '', '',
                                               '']
                                     ,
                                  'ЭФиДГ2МПН': [45493.0, 800.0, '', 0.671, 104.5, '', '', '', '', '', '', '', '', '', '',
                                                '']
                                     , 'ЭФиДГВЗЖД': [106151.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
                                     , 'ЭФиДГВЗВТ': [45493.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
                                     , 'В': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']})

    def cal_tab1(self):
        # Столбец 'СХО'
        self.tab1.loc[2, 'СХО'] = self.tab1.loc[0, 'СХО'] * self.tab1.loc[1, 'СХО']
        self.tab1.loc[4, 'СХО'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'СХО'] / 1000
        self.tab1.loc[13, 'СХО'] = self.tab1.loc[13, 'ПП'] * 2
        self.tab1.loc[16, 'СХО'] = (self.tab1.loc[17, 'СХО'] / self.tab1.loc[2, 'СХО']) * 100
        self.tab1.loc[24, 'СХО'] = self.tab1.loc[23, 'СХО'] / self.tab1.loc[17, 'СХО'] * 1000
        self.tab1.loc[30, 'СХО'] = (self.tab1.loc[17, 'СХО'] * self.tab1.loc[26, 'СХО']) / 1000
        self.tab1.loc[32, 'СХО'] = (self.tab1.loc[17, 'СХО'] * self.tab1.loc[27, 'СХО']) / 1000
        self.tab1.loc[34, 'СХО'] = self.tab1.loc[30, 'СХО'] - self.tab1.loc[23, 'СХО']
        self.tab1.loc[36, 'СХО'] = (self.tab1.loc[34, 'СХО'] / self.tab1.loc[23, 'СХО']) * 100

        # Столбец 'ПП'
        self.tab1.loc[8, 'ПП'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[7, 'СХО']

        # Столбец 'МВР'
        self.tab1.loc[0, 'МВР'] = self.tab1.loc[0, 'СХО'] * self.tab5.loc[8, 'ВРПМВР'] * self.tab5.loc[6, 'ВРПМЭ']
        self.tab1.loc[2, 'МВР'] = self.tab1.loc[2, 'СХО'] * self.tab5.loc[8, 'ВРПМВР'] * self.tab5.loc[6, 'ВРПМЭ'] * \
                                  self.tab1.loc[5, 'МВР']
        self.tab1.loc[4, 'МВР'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'МВР'] / 1000
        self.tab1.loc[6, 'МВР'] = self.tab1.loc[2, 'МВР'] * self.tab1.loc[5, 'МВР']
        self.tab1.loc[11, 'МВР'] = self.tab1.loc[6, 'МВР'] * self.tab1.loc[10, 'МВР']
        self.tab1.loc[13, 'МВР'] = (self.tab1.loc[3, 'СХО'] * self.tab1.loc[13, 'Нормативы'] * self.tab1.loc[7, 'МВР'])
        self.tab1.loc[14, 'МВР'] = self.tab1.loc[4, 'МВР'] + self.tab1.loc[13, 'МВР']
        self.tab1.loc[15, 'МВР'] = (self.tab1.loc[14, 'МВР'] / self.tab1.loc[11, 'МВР']) * 1000
        self.tab1.loc[17, 'МВР'] = self.tab1.loc[11, 'МВР'] * self.tab1.loc[16, 'МВР']
        self.tab1.loc[19, 'МВР'] = self.tab1.loc[14, 'МВР'] * self.tab1.loc[18, 'МВР']
        self.tab1.loc[21, 'МВР'] = self.tab1.loc[14, 'МВР'] * self.tab1.loc[20, 'МВР']
        self.tab1.loc[22, 'МВР'] = (self.tab1.loc[21, 'МВР'] / self.tab1.loc[17, 'МВР']) * 1000
        self.tab1.loc[23, 'МВР'] = self.tab1.loc[14, 'МВР'] + self.tab1.loc[19, 'МВР'] + self.tab1.loc[21, 'МВР']
        self.tab1.loc[24, 'МВР'] = self.tab1.loc[23, 'МВР'] / self.tab1.loc[17, 'МВР'] * 1000
        self.tab1.loc[29, 'МВР'] = self.tab1.loc[26, 'СХО']
        self.tab1.loc[30, 'МВР'] = (self.tab1.loc[17, 'МВР'] * self.tab1.loc[26, 'МВР']) / 1000
        self.tab1.loc[31, 'МВР'] = (self.tab1.loc[17, 'МВР'] * self.tab1.loc[29, 'МВР']) / 1000
        self.tab1.loc[34, 'МВР'] = self.tab1.loc[30, 'МВР'] - self.tab1.loc[23, 'МВР']
        self.tab1.loc[36, 'МВР'] = (self.tab1.loc[34, 'МВР'] / self.tab1.loc[23, 'МВР']) * 100

        # Столбец 'МЭ'
        self.tab1.loc[0, 'МЭ'] = self.tab1.loc[0, 'СХО'] * self.tab5.loc[6, 'ВРПМЭ'] * self.tab5.loc[8, 'ВРПМЭ']
        self.tab1.loc[2, 'МЭ'] = self.tab1.loc[2, 'СХО'] * self.tab5.loc[6, 'ВРПМЭ'] * self.tab5.loc[8, 'ВРПМЭ'] * \
                                 self.tab1.loc[5, 'МЭ']
        self.tab1.loc[4, 'МЭ'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'МЭ'] / 1000
        self.tab1.loc[6, 'МЭ'] = self.tab1.loc[2, 'МЭ'] * self.tab1.loc[5, 'МЭ']
        self.tab1.loc[11, 'МЭ'] = self.tab1.loc[6, 'МЭ'] * self.tab1.loc[10, 'МЭ']
        self.tab1.loc[13, 'МЭ'] = (self.tab1.loc[3, 'СХО'] * self.tab1.loc[13, 'Нормативы'] * self.tab1.loc[7, 'МЭ'])
        self.tab1.loc[14, 'МЭ'] = self.tab1.loc[4, 'МЭ'] + self.tab1.loc[13, 'МЭ']
        self.tab1.loc[15, 'МЭ'] = (self.tab1.loc[14, 'МЭ'] / self.tab1.loc[11, 'МЭ']) * 1000
        self.tab1.loc[17, 'МЭ'] = self.tab1.loc[11, 'МЭ'] * self.tab1.loc[16, 'МЭ']
        self.tab1.loc[19, 'МЭ'] = self.tab1.loc[14, 'МЭ'] * self.tab1.loc[18, 'МЭ']
        self.tab1.loc[21, 'МЭ'] = self.tab1.loc[14, 'МЭ'] * self.tab1.loc[20, 'МЭ']
        self.tab1.loc[22, 'МЭ'] = (self.tab1.loc[21, 'МЭ'] / self.tab1.loc[17, 'МЭ']) * 1000
        self.tab1.loc[23, 'МЭ'] = self.tab1.loc[14, 'МЭ'] + self.tab1.loc[19, 'МЭ'] + self.tab1.loc[21, 'МЭ']
        self.tab1.loc[24, 'МЭ'] = self.tab1.loc[23, 'МЭ'] / self.tab1.loc[17, 'МЭ'] * 1000
        self.tab1.loc[26, 'МЭ'] = self.tab1.loc[26, 'СХО'] * self.tab1.loc[26, 'Нормативы']
        self.tab1.loc[29, 'МЭ'] = self.tab1.loc[26, 'МЭ'] - self.tab1.loc[28, 'МЭ']
        self.tab1.loc[30, 'МЭ'] = (self.tab1.loc[17, 'МЭ'] * self.tab1.loc[26, 'МЭ']) / 1000
        self.tab1.loc[31, 'МЭ'] = (self.tab1.loc[17, 'МЭ'] * self.tab1.loc[29, 'МЭ']) / 1000
        self.tab1.loc[34, 'МЭ'] = self.tab1.loc[30, 'МЭ'] - self.tab1.loc[23, 'МЭ']
        self.tab1.loc[35, 'МЭ'] = self.tab1.loc[31, 'МЭ'] - self.tab1.loc[23, 'МЭ']
        self.tab1.loc[36, 'МЭ'] = (self.tab1.loc[34, 'МЭ'] / self.tab1.loc[23, 'МЭ']) * 100
        self.tab1.loc[37, 'МЭ'] = (self.tab1.loc[35, 'МЭ'] / self.tab1.loc[23, 'МЭ']) * 100
        self.tab1.loc[38, 'МЭ'] = self.tab1.loc[28, 'МЭ'] * self.tab1.loc[17, 'МЭ'] / 1000
        self.tab1.loc[39, 'МЭ'] = self.tab1.loc[38, 'МЭ'] / self.tab1.loc[34, 'МЭ'] * 100

        # Столбец 'МПСПДСН'
        self.tab1.loc[0, 'МПСПДСН'] = self.tab1.loc[0, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПСН'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                          6, 'ВРПМПППЭ']
        self.tab1.loc[2, 'МПСПДСН'] = self.tab1.loc[2, 'СХО'] * self.tab5.loc[6, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                          8, 'ВРПМПСПСН'] * self.tab1.loc[5, 'МПСПДСН']
        self.tab1.loc[4, 'МПСПДСН'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'МПСПДСН'] / 1000
        self.tab1.loc[6, 'МПСПДСН'] = self.tab1.loc[2, 'МПСПДСН'] * self.tab1.loc[5, 'МПСПДСН']
        self.tab1.loc[8, 'МПСПДСН'] = (self.tab1.loc[3, 'СХО'] * self.tab1.loc[7, 'МПСПДСН'])
        self.tab1.loc[9, 'МПСПДСН'] = self.tab1.loc[8, 'МПСПДСН'] * self.tab1.loc[6, 'МПСПДСН'] / 1000
        self.tab1.loc[11, 'МПСПДСН'] = self.tab1.loc[6, 'МПСПДСН'] * self.tab1.loc[10, 'МПСПДСН']
        self.tab1.loc[13, 'МПСПДСН'] = (self.tab1.loc[12, 'МПСПДСН'] * self.tab1.loc[13, 'СХО'] * self.tab1.loc[
            6, 'МПСПДСН']) / 1000
        self.tab1.loc[14, 'МПСПДСН'] = self.tab1.loc[9, 'МПСПДСН'] + self.tab1.loc[13, 'МПСПДСН']
        self.tab1.loc[15, 'МПСПДСН'] = (self.tab1.loc[14, 'МПСПДСН'] / self.tab1.loc[11, 'МПСПДСН']) * 1000
        self.tab1.loc[17, 'МПСПДСН'] = self.tab1.loc[11, 'МПСПДСН'] * self.tab1.loc[16, 'МПСПДСН']
        self.tab1.loc[19, 'МПСПДСН'] = self.tab1.loc[14, 'МПСПДСН'] * self.tab1.loc[18, 'МПСПДСН']
        self.tab1.loc[21, 'МПСПДСН'] = self.tab1.loc[14, 'МПСПДСН'] * self.tab1.loc[20, 'МПСПДСН']
        self.tab1.loc[22, 'МПСПДСН'] = (self.tab1.loc[21, 'МПСПДСН'] / self.tab1.loc[17, 'МПСПДСН']) * 1000
        self.tab1.loc[23, 'МПСПДСН'] = self.tab1.loc[14, 'МПСПДСН'] + self.tab1.loc[19, 'МПСПДСН'] + self.tab1.loc[
            21, 'МПСПДСН']
        self.tab1.loc[24, 'МПСПДСН'] = self.tab1.loc[23, 'МПСПДСН'] / self.tab1.loc[17, 'МПСПДСН'] * 1000
        self.tab1.loc[27, 'МПСПДСН'] = self.tab1.loc[27, 'СХО'] * self.tab1.loc[25, 'МПСПДСН']
        self.tab1.loc[32, 'МПСПДСН'] = self.tab1.loc[17, 'МПСПДСН'] * self.tab1.loc[27, 'МПСПДСН'] / 1000
        self.tab1.loc[34, 'МПСПДСН'] = self.tab1.loc[32, 'МПСПДСН'] - self.tab1.loc[23, 'МПСПДСН']
        self.tab1.loc[36, 'МПСПДСН'] = (self.tab1.loc[34, 'МПСПДСН'] / self.tab1.loc[23, 'МПСПДСН']) * 100

        self.tab1.loc[0, 'МПСПОУ'] = self.tab1.loc[0, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПОУ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                         6, 'ВРПМПППЭ']
        self.tab1.loc[2, 'МПСПОУ'] = self.tab1.loc[2, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПОУ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                         6, 'ВРПМПППЭ'] * self.tab1.loc[5, 'МПСПОУ']
        self.tab1.loc[4, 'МПСПОУ'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'МПСПОУ'] / 1000
        self.tab1.loc[6, 'МПСПОУ'] = self.tab1.loc[2, 'МПСПОУ'] * self.tab1.loc[5, 'МПСПОУ']
        self.tab1.loc[8, 'МПСПОУ'] = (self.tab1.loc[3, 'СХО'] * self.tab1.loc[7, 'МПСПОУ'])
        self.tab1.loc[9, 'МПСПОУ'] = self.tab1.loc[8, 'МПСПОУ'] * self.tab1.loc[6, 'МПСПОУ'] / 1000
        self.tab1.loc[11, 'МПСПОУ'] = self.tab1.loc[6, 'МПСПОУ'] * self.tab1.loc[10, 'МПСПОУ']
        self.tab1.loc[13, 'МПСПОУ'] = (self.tab1.loc[12, 'МПСПОУ'] * self.tab1.loc[13, 'СХО'] * self.tab1.loc[
            6, 'МПСПОУ']) / 1000
        self.tab1.loc[14, 'МПСПОУ'] = self.tab1.loc[9, 'МПСПОУ'] + self.tab1.loc[13, 'МПСПОУ']
        self.tab1.loc[15, 'МПСПОУ'] = (self.tab1.loc[14, 'МПСПОУ'] / self.tab1.loc[11, 'МПСПОУ']) * 1000
        self.tab1.loc[17, 'МПСПОУ'] = self.tab1.loc[11, 'МПСПОУ'] * self.tab1.loc[16, 'МПСПОУ']
        self.tab1.loc[19, 'МПСПОУ'] = self.tab1.loc[14, 'МПСПОУ'] * self.tab1.loc[18, 'МПСПОУ']
        self.tab1.loc[21, 'МПСПОУ'] = self.tab1.loc[14, 'МПСПОУ'] * self.tab1.loc[20, 'МПСПОУ']
        self.tab1.loc[22, 'МПСПОУ'] = (self.tab1.loc[21, 'МПСПОУ'] / self.tab1.loc[17, 'МПСПОУ']) * 1000
        self.tab1.loc[23, 'МПСПОУ'] = self.tab1.loc[14, 'МПСПОУ'] + self.tab1.loc[19, 'МПСПОУ'] + self.tab1.loc[
            21, 'МПСПОУ']
        self.tab1.loc[24, 'МПСПОУ'] = self.tab1.loc[23, 'МПСПОУ'] / self.tab1.loc[17, 'МПСПОУ'] * 1000
        self.tab1.loc[27, 'МПСПОУ'] = self.tab1.loc[27, 'СХО'] * self.tab1.loc[25, 'МПСПОУ']
        self.tab1.loc[32, 'МПСПОУ'] = self.tab1.loc[17, 'МПСПОУ'] * self.tab1.loc[27, 'МПСПОУ'] / 1000
        self.tab1.loc[34, 'МПСПОУ'] = self.tab1.loc[32, 'МПСПОУ'] - self.tab1.loc[23, 'МПСПОУ']
        self.tab1.loc[36, 'МПСПОУ'] = (self.tab1.loc[34, 'МПСПОУ'] / self.tab1.loc[23, 'МПСПОУ']) * 100

        # Столбец 'МПСПВР'
        self.tab1.loc[0, 'МПСПВР'] = self.tab1.loc[0, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПВР'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                         6, 'ВРПМПППЭ']
        self.tab1.loc[2, 'МПСПВР'] = self.tab1.loc[2, 'СХО'] * self.tab5.loc[6, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                         8, 'ВРПМПСПВР'] * self.tab1.loc[5, 'МПСПВР']
        self.tab1.loc[4, 'МПСПВР'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'МПСПВР'] / 1000
        self.tab1.loc[6, 'МПСПВР'] = self.tab1.loc[2, 'МПСПВР'] * self.tab1.loc[5, 'МПСПВР']
        self.tab1.loc[8, 'МПСПВР'] = (self.tab1.loc[3, 'СХО'] * self.tab1.loc[7, 'МПСПВР'])
        self.tab1.loc[9, 'МПСПВР'] = self.tab1.loc[8, 'МПСПВР'] * self.tab1.loc[6, 'МПСПВР'] / 1000
        self.tab1.loc[11, 'МПСПВР'] = self.tab1.loc[6, 'МПСПВР'] * self.tab1.loc[10, 'МПСПВР']
        self.tab1.loc[13, 'МПСПВР'] = (self.tab1.loc[12, 'МПСПВР'] * self.tab1.loc[13, 'СХО'] * self.tab1.loc[
            6, 'МПСПВР']) / 1000
        self.tab1.loc[14, 'МПСПВР'] = self.tab1.loc[9, 'МПСПВР'] + self.tab1.loc[13, 'МПСПВР']
        self.tab1.loc[15, 'МПСПВР'] = (self.tab1.loc[14, 'МПСПВР'] / self.tab1.loc[11, 'МПСПВР']) * 1000
        self.tab1.loc[17, 'МПСПВР'] = self.tab1.loc[11, 'МПСПВР'] * self.tab1.loc[16, 'МПСПВР']
        self.tab1.loc[19, 'МПСПВР'] = self.tab1.loc[14, 'МПСПВР'] * self.tab1.loc[18, 'МПСПВР']
        self.tab1.loc[21, 'МПСПВР'] = self.tab1.loc[14, 'МПСПВР'] * self.tab1.loc[20, 'МПСПВР']
        self.tab1.loc[22, 'МПСПВР'] = (self.tab1.loc[21, 'МПСПВР'] / self.tab1.loc[17, 'МПСПВР']) * 1000
        self.tab1.loc[23, 'МПСПВР'] = self.tab1.loc[14, 'МПСПВР'] + self.tab1.loc[19, 'МПСПВР'] + self.tab1.loc[
            21, 'МПСПВР']
        self.tab1.loc[24, 'МПСПВР'] = self.tab1.loc[23, 'МПСПВР'] / self.tab1.loc[17, 'МПСПВР'] * 1000
        self.tab1.loc[27, 'МПСПВР'] = self.tab1.loc[27, 'СХО'] * self.tab1.loc[25, 'МПСПВР']
        self.tab1.loc[32, 'МПСПВР'] = self.tab1.loc[17, 'МПСПВР'] * self.tab1.loc[27, 'МПСПВР'] / 1000
        self.tab1.loc[34, 'МПСПВР'] = self.tab1.loc[32, 'МПСПВР'] - self.tab1.loc[23, 'МПСПВР']
        self.tab1.loc[36, 'МПСПВР'] = (self.tab1.loc[34, 'МПСПВР'] / self.tab1.loc[23, 'МПСПВР']) * 100

        # Столбец 'МПСПЭ'
        self.tab1.loc[0, 'МПСПЭ'] = self.tab1.loc[0, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПЭ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                        6, 'ВРПМПППЭ']
        self.tab1.loc[2, 'МПСПЭ'] = self.tab1.loc[2, 'СХО'] * self.tab5.loc[6, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                        8, 'ВРПМПСПЭ'] * self.tab1.loc[5, 'МПСПЭ']
        self.tab1.loc[4, 'МПСПЭ'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'МПСПЭ'] / 1000
        self.tab1.loc[6, 'МПСПЭ'] = self.tab1.loc[2, 'МПСПЭ'] * self.tab1.loc[5, 'МПСПЭ']
        self.tab1.loc[8, 'МПСПЭ'] = (self.tab1.loc[3, 'СХО'] * self.tab1.loc[7, 'МПСПЭ'])
        self.tab1.loc[9, 'МПСПЭ'] = self.tab1.loc[8, 'МПСПЭ'] * self.tab1.loc[6, 'МПСПЭ'] / 1000
        self.tab1.loc[11, 'МПСПЭ'] = self.tab1.loc[6, 'МПСПЭ'] * self.tab1.loc[10, 'МПСПЭ']
        self.tab1.loc[13, 'МПСПЭ'] = (self.tab1.loc[12, 'МПСПЭ'] * self.tab1.loc[13, 'СХО'] * self.tab1.loc[
            6, 'МПСПЭ']) / 1000
        self.tab1.loc[14, 'МПСПЭ'] = self.tab1.loc[9, 'МПСПЭ'] + self.tab1.loc[13, 'МПСПЭ']
        self.tab1.loc[15, 'МПСПЭ'] = (self.tab1.loc[14, 'МПСПЭ'] / self.tab1.loc[11, 'МПСПЭ']) * 1000
        self.tab1.loc[17, 'МПСПЭ'] = self.tab1.loc[11, 'МПСПЭ'] * self.tab1.loc[16, 'МПСПЭ']
        self.tab1.loc[19, 'МПСПЭ'] = self.tab1.loc[14, 'МПСПЭ'] * self.tab1.loc[18, 'МПСПЭ']
        self.tab1.loc[21, 'МПСПЭ'] = self.tab1.loc[14, 'МПСПЭ'] * self.tab1.loc[20, 'МПСПЭ']
        self.tab1.loc[22, 'МПСПЭ'] = (self.tab1.loc[21, 'МПСПЭ'] / self.tab1.loc[17, 'МПСПЭ']) * 1000
        self.tab1.loc[23, 'МПСПЭ'] = self.tab1.loc[14, 'МПСПЭ'] + self.tab1.loc[19, 'МПСПЭ'] + self.tab1.loc[
            21, 'МПСПЭ']
        self.tab1.loc[24, 'МПСПЭ'] = self.tab1.loc[23, 'МПСПЭ'] / self.tab1.loc[17, 'МПСПЭ'] * 1000
        self.tab1.loc[27, 'МПСПЭ'] = self.tab1.loc[27, 'СХО'] * self.tab1.loc[25, 'МПСПЭ']
        self.tab1.loc[29, 'МПСПЭ'] = self.tab1.loc[27, 'МПСПЭ'] - self.tab1.loc[28, 'МПСПЭ']
        self.tab1.loc[32, 'МПСПЭ'] = (self.tab1.loc[27, 'МПСПЭ'] * self.tab1.loc[17, 'МПСПЭ']) / 1000
        self.tab1.loc[33, 'МПСПЭ'] = (self.tab1.loc[29, 'МПСПЭ'] * self.tab1.loc[17, 'МПСПЭ']) / 1000
        self.tab1.loc[34, 'МПСПЭ'] = self.tab1.loc[32, 'МПСПЭ'] - self.tab1.loc[23, 'МПСПЭ']
        self.tab1.loc[35, 'МПСПЭ'] = self.tab1.loc[33, 'МПСПЭ'] - self.tab1.loc[23, 'МПСПЭ']
        self.tab1.loc[36, 'МПСПЭ'] = (self.tab1.loc[34, 'МПСПЭ'] / self.tab1.loc[23, 'МПСПЭ']) * 100
        self.tab1.loc[37, 'МПСПЭ'] = self.tab1.loc[35, 'МПСПЭ'] / self.tab1.loc[23, 'МПСПЭ'] * 100
        self.tab1.loc[38, 'МПСПЭ'] = self.tab1.loc[28, 'МПСПЭ'] * self.tab1.loc[17, 'МПСПЭ'] / 1000
        self.tab1.loc[39, 'МПСПЭ'] = self.tab1.loc[38, 'МПСПЭ'] / self.tab1.loc[34, 'МПСПЭ'] * 100

        # Столбец 'МПППВР'
        self.tab1.loc[0, 'МПППВР'] = self.tab1.loc[0, 'СХО'] * self.tab5.loc[8, 'ВРПМПППВР'] * self.tab5.loc[
            7, 'ВРПМПППЭ'] * self.tab5.loc[
                                         6, 'ВРПМПППЭ']
        self.tab1.loc[2, 'МПППВР'] = self.tab1.loc[2, 'СХО'] * self.tab5.loc[6, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПППЭ'] * self.tab5.loc[
                                         8, 'ВРПМПППВР'] * self.tab1.loc[5, 'МПППВР']
        self.tab1.loc[4, 'МПППВР'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'МПППВР'] / 1000
        self.tab1.loc[6, 'МПППВР'] = self.tab1.loc[2, 'МПППВР'] * self.tab1.loc[5, 'МПППВР']
        self.tab1.loc[8, 'МПППВР'] = (self.tab1.loc[8, 'ПП'] * self.tab1.loc[7, 'МПППВР'])
        self.tab1.loc[9, 'МПППВР'] = self.tab1.loc[8, 'МПППВР'] * self.tab1.loc[6, 'МПППВР'] / 1000
        self.tab1.loc[11, 'МПППВР'] = self.tab1.loc[6, 'МПППВР'] * self.tab1.loc[10, 'МПППВР']
        self.tab1.loc[13, 'МПППВР'] = (self.tab1.loc[12, 'МПППВР'] * self.tab1.loc[13, 'ПП'] * self.tab1.loc[
            6, 'МПППВР']) / 1000
        self.tab1.loc[14, 'МПППВР'] = self.tab1.loc[9, 'МПППВР'] + self.tab1.loc[13, 'МПППВР']
        self.tab1.loc[15, 'МПППВР'] = (self.tab1.loc[14, 'МПППВР'] / self.tab1.loc[11, 'МПППВР']) * 1000
        self.tab1.loc[17, 'МПППВР'] = self.tab1.loc[11, 'МПППВР'] * self.tab1.loc[16, 'МПППВР']
        self.tab1.loc[19, 'МПППВР'] = self.tab1.loc[14, 'МПППВР'] * self.tab1.loc[18, 'МПППВР']
        self.tab1.loc[21, 'МПППВР'] = self.tab1.loc[14, 'МПППВР'] * self.tab1.loc[20, 'МПППВР']
        self.tab1.loc[22, 'МПППВР'] = (self.tab1.loc[21, 'МПППВР'] / self.tab1.loc[17, 'МПППВР']) * 1000
        self.tab1.loc[23, 'МПППВР'] = self.tab1.loc[14, 'МПППВР'] + self.tab1.loc[19, 'МПППВР'] + self.tab1.loc[
            21, 'МПППВР']
        self.tab1.loc[24, 'МПППВР'] = self.tab1.loc[23, 'МПППВР'] / self.tab1.loc[17, 'МПППВР'] * 1000
        self.tab1.loc[27, 'МПППВР'] = self.tab1.loc[27, 'ПП'] * self.tab1.loc[25, 'МПППВР']
        self.tab1.loc[32, 'МПППВР'] = (self.tab1.loc[27, 'МПППВР'] * self.tab1.loc[17, 'МПППВР']) / 1000
        self.tab1.loc[34, 'МПППВР'] = self.tab1.loc[32, 'МПППВР'] - self.tab1.loc[23, 'МПППВР']
        self.tab1.loc[36, 'МПППВР'] = (self.tab1.loc[34, 'МПППВР'] / self.tab1.loc[23, 'МПППВР']) * 100

        # Столбец 'МПППЭ'
        self.tab1.loc[0, 'МПППЭ'] = self.tab1.loc[0, 'СХО'] * self.tab5.loc[8, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПППЭ'] * self.tab5.loc[
                                        6, 'ВРПМПППЭ']
        self.tab1.loc[2, 'МПППЭ'] = self.tab1.loc[2, 'СХО'] * self.tab5.loc[6, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПППЭ'] * self.tab5.loc[
                                        8, 'ВРПМПППЭ'] * self.tab1.loc[5, 'МПППЭ']
        self.tab1.loc[4, 'МПППЭ'] = self.tab1.loc[3, 'СХО'] * self.tab1.loc[2, 'МПППЭ'] / 1000
        self.tab1.loc[6, 'МПППЭ'] = self.tab1.loc[2, 'МПППЭ'] * self.tab1.loc[5, 'МПППЭ']
        self.tab1.loc[8, 'МПППЭ'] = self.tab1.loc[8, 'ПП'] * self.tab1.loc[7, 'МПППЭ']
        self.tab1.loc[9, 'МПППЭ'] = self.tab1.loc[8, 'МПППЭ'] * self.tab1.loc[6, 'МПППЭ'] / 1000
        self.tab1.loc[11, 'МПППЭ'] = self.tab1.loc[6, 'МПППЭ'] * self.tab1.loc[10, 'МПППЭ']
        self.tab1.loc[13, 'МПППЭ'] = (self.tab1.loc[12, 'МПППЭ'] * self.tab1.loc[13, 'ПП'] * self.tab1.loc[
            6, 'МПППЭ']) / 1000
        self.tab1.loc[14, 'МПППЭ'] = self.tab1.loc[9, 'МПППЭ'] + self.tab1.loc[13, 'МПППЭ']
        self.tab1.loc[15, 'МПППЭ'] = (self.tab1.loc[14, 'МПППЭ'] / self.tab1.loc[11, 'МПППЭ']) * 1000
        self.tab1.loc[17, 'МПППЭ'] = self.tab1.loc[11, 'МПППЭ'] * self.tab1.loc[16, 'МПППЭ']
        self.tab1.loc[19, 'МПППЭ'] = self.tab1.loc[14, 'МПППЭ'] * self.tab1.loc[18, 'МПППЭ']
        self.tab1.loc[21, 'МПППЭ'] = self.tab1.loc[14, 'МПППЭ'] * self.tab1.loc[20, 'МПППЭ']
        self.tab1.loc[22, 'МПППЭ'] = (self.tab1.loc[21, 'МПППЭ'] / self.tab1.loc[17, 'МПППЭ']) * 1000
        self.tab1.loc[23, 'МПППЭ'] = self.tab1.loc[14, 'МПППЭ'] + self.tab1.loc[19, 'МПППЭ'] + self.tab1.loc[
            21, 'МПППЭ']
        self.tab1.loc[24, 'МПППЭ'] = self.tab1.loc[23, 'МПППЭ'] / self.tab1.loc[17, 'МПППЭ'] * 1000
        self.tab1.loc[27, 'МПППЭ'] = self.tab1.loc[27, 'ПП'] * self.tab1.loc[25, 'МПППЭ']
        self.tab1.loc[29, 'МПППЭ'] = self.tab1.loc[27, 'МПППЭ'] - self.tab1.loc[28, 'МПППЭ']
        self.tab1.loc[32, 'МПППЭ'] = (self.tab1.loc[27, 'МПППЭ'] * self.tab1.loc[17, 'МПППЭ']) / 1000
        self.tab1.loc[33, 'МПППЭ'] = (self.tab1.loc[29, 'МПППЭ'] * self.tab1.loc[17, 'МПППЭ']) / 1000
        self.tab1.loc[34, 'МПППЭ'] = self.tab1.loc[32, 'МПППЭ'] - self.tab1.loc[23, 'МПППЭ']
        self.tab1.loc[35, 'МПППЭ'] = self.tab1.loc[33, 'МПППЭ'] - self.tab1.loc[23, 'МПППЭ']
        self.tab1.loc[36, 'МПППЭ'] = (self.tab1.loc[34, 'МПППЭ'] / self.tab1.loc[23, 'МПППЭ']) * 100
        self.tab1.loc[37, 'МПППЭ'] = (self.tab1.loc[35, 'МПППЭ'] / self.tab1.loc[23, 'МПППЭ']) * 100
        self.tab1.loc[38, 'МПППЭ'] = self.tab1.loc[28, 'МПППЭ'] * self.tab1.loc[17, 'МПППЭ'] / 1000
        self.tab1.loc[39, 'МПППЭ'] = self.tab1.loc[38, 'МПППЭ'] / self.tab1.loc[34, 'МПППЭ'] * 100

        # Столбец 'ИМ'
        self.tab1.loc[0, 'ИМ'] = self.tab1.loc[0, 'МВР'] + self.tab1.loc[0, 'МЭ']
        self.tab1.loc[2, 'ИМ'] = self.tab1.loc[2, 'МВР'] + self.tab1.loc[2, 'МЭ']
        self.tab1.loc[1, 'ИМ'] = self.tab1.loc[2, 'ИМ'] / self.tab1.loc[0, 'ИМ']
        self.tab1.loc[4, 'ИМ'] = self.tab1.loc[4, 'МВР'] + self.tab1.loc[4, 'МЭ']
        self.tab1.loc[3, 'ИМ'] = self.tab1.loc[4, 'ИМ'] / self.tab1.loc[2, 'ИМ'] * 1000
        self.tab1.loc[6, 'ИМ'] = self.tab1.loc[6, 'МВР'] + self.tab1.loc[6, 'МЭ']
        self.tab1.loc[11, 'ИМ'] = self.tab1.loc[11, 'МВР'] + self.tab1.loc[11, 'МЭ']
        self.tab1.loc[13, 'ИМ'] = self.tab1.loc[13, 'МВР'] + self.tab1.loc[13, 'МЭ']
        self.tab1.loc[14, 'ИМ'] = self.tab1.loc[14, 'МВР'] + self.tab1.loc[14, 'МЭ']
        self.tab1.loc[15, 'ИМ'] = self.tab1.loc[14, 'ИМ'] / self.tab1.loc[11, 'ИМ'] * 1000
        self.tab1.loc[17, 'ИМ'] = self.tab1.loc[17, 'МВР'] + self.tab1.loc[17, 'МЭ']
        self.tab1.loc[16, 'ИМ'] = self.tab1.loc[17, 'ИМ'] / self.tab1.loc[2, 'ИМ'] * 100
        self.tab1.loc[19, 'ИМ'] = self.tab1.loc[19, 'МВР'] + self.tab1.loc[19, 'МЭ']
        self.tab1.loc[21, 'ИМ'] = self.tab1.loc[21, 'МВР'] + self.tab1.loc[21, 'МЭ']
        self.tab1.loc[22, 'ИМ'] = self.tab1.loc[21, 'ИМ'] / self.tab1.loc[17, 'ИМ'] * 1000
        self.tab1.loc[23, 'ИМ'] = self.tab1.loc[23, 'МВР'] + self.tab1.loc[23, 'МЭ']
        self.tab1.loc[24, 'ИМ'] = self.tab1.loc[23, 'ИМ'] / self.tab1.loc[17, 'ИМ'] * 1000
        self.tab1.loc[30, 'ИМ'] = self.tab1.loc[30, 'МВР'] + self.tab1.loc[30, 'МЭ']
        self.tab1.loc[31, 'ИМ'] = self.tab1.loc[31, 'МВР'] + self.tab1.loc[31, 'МЭ']
        self.tab1.loc[34, 'ИМ'] = self.tab1.loc[34, 'МВР'] + self.tab1.loc[34, 'МЭ']
        self.tab1.loc[35, 'ИМ'] = self.tab1.loc[35, 'МЭ']
        self.tab1.loc[36, 'ИМ'] = self.tab1.loc[34, 'ИМ'] / self.tab1.loc[23, 'ИМ'] * 100
        self.tab1.loc[37, 'ИМ'] = self.tab1.loc[35, 'ИМ'] / self.tab1.loc[23, 'ИМ'] * 100

        # Столбец 'ИМПСП'
        self.tab1.loc[0, 'ИМПСП'] = self.tab1.loc[0, 'МПСПДСН'] + self.tab1.loc[0, 'МПСПВР'] + self.tab1.loc[
            0, 'МПСПОУ'] + self.tab1.loc[
                                        0, 'МПСПЭ']
        self.tab1.loc[2, 'ИМПСП'] = self.tab1.loc[2, 'МПСПДСН'] + self.tab1.loc[2, 'МПСПВР'] + self.tab1.loc[
            2, 'МПСПОУ'] + self.tab1.loc[
                                        2, 'МПСПЭ']
        self.tab1.loc[1, 'ИМПСП'] = self.tab1.loc[2, 'ИМПСП'] / self.tab1.loc[0, 'ИМПСП']
        self.tab1.loc[4, 'ИМПСП'] = self.tab1.loc[4, 'МПСПДСН'] + self.tab1.loc[4, 'МПСПВР'] + self.tab1.loc[
            4, 'МПСПОУ'] + self.tab1.loc[
                                        4, 'МПСПЭ']
        self.tab1.loc[3, 'ИМПСП'] = self.tab1.loc[4, 'ИМПСП'] / self.tab1.loc[2, 'ИМПСП'] * 1000
        self.tab1.loc[6, 'ИМПСП'] = self.tab1.loc[6, 'МПСПДСН'] + self.tab1.loc[6, 'МПСПОУ'] + self.tab1.loc[
            6, 'МПСПВР'] + self.tab1.loc[
                                        6, 'МПСПЭ']
        self.tab1.loc[9, 'ИМПСП'] = self.tab1.loc[9, 'МПСПДСН'] + self.tab1.loc[9, 'МПСПОУ'] + self.tab1.loc[
            9, 'МПСПВР'] + self.tab1.loc[
                                        9, 'МПСПЭ']
        self.tab1.loc[8, 'ИМПСП'] = self.tab1.loc[9, 'ИМПСП'] / self.tab1.loc[6, 'ИМПСП'] * 1000
        self.tab1.loc[11, 'ИМПСП'] = self.tab1.loc[11, 'МПСПДСН'] + self.tab1.loc[11, 'МПСПВР'] + self.tab1.loc[
            11, 'МПСПОУ'] + self.tab1.loc[
                                         11, 'МПСПЭ']
        self.tab1.loc[13, 'ИМПСП'] = self.tab1.loc[13, 'МПСПДСН'] + self.tab1.loc[13, 'МПСПОУ'] + self.tab1.loc[
            13, 'МПСПВР'] + self.tab1.loc[
                                         13, 'МПСПЭ']
        self.tab1.loc[14, 'ИМПСП'] = self.tab1.loc[14, 'МПСПДСН'] + self.tab1.loc[14, 'МПСПОУ'] + self.tab1.loc[
            14, 'МПСПВР'] + self.tab1.loc[
                                         14, 'МПСПЭ']
        self.tab1.loc[15, 'ИМПСП'] = self.tab1.loc[14, 'ИМПСП'] / self.tab1.loc[11, 'ИМПСП'] * 1000
        self.tab1.loc[17, 'ИМПСП'] = self.tab1.loc[17, 'МПСПДСН'] + self.tab1.loc[17, 'МПСПВР'] + self.tab1.loc[
            17, 'МПСПОУ'] + self.tab1.loc[
                                         17, 'МПСПЭ']
        self.tab1.loc[16, 'ИМПСП'] = self.tab1.loc[17, 'ИМПСП'] / self.tab1.loc[2, 'ИМПСП'] * 100
        self.tab1.loc[19, 'ИМПСП'] = self.tab1.loc[19, 'МПСПДСН'] + self.tab1.loc[19, 'МПСПОУ'] + self.tab1.loc[
            19, 'МПСПВР'] + self.tab1.loc[
                                         19, 'МПСПЭ']
        self.tab1.loc[21, 'ИМПСП'] = self.tab1.loc[21, 'МПСПДСН'] + self.tab1.loc[21, 'МПСПОУ'] + self.tab1.loc[
            21, 'МПСПВР'] + self.tab1.loc[
                                         21, 'МПСПЭ']
        self.tab1.loc[22, 'ИМПСП'] = self.tab1.loc[21, 'ИМПСП'] / self.tab1.loc[17, 'ИМПСП'] * 1000
        self.tab1.loc[23, 'ИМПСП'] = self.tab1.loc[23, 'МПСПДСН'] + self.tab1.loc[23, 'МПСПОУ'] + self.tab1.loc[
            23, 'МПСПВР'] + self.tab1.loc[
                                         23, 'МПСПЭ']
        self.tab1.loc[24, 'ИМПСП'] = self.tab1.loc[23, 'ИМПСП'] / self.tab1.loc[17, 'ИМПСП'] * 1000
        self.tab1.loc[32, 'ИМПСП'] = self.tab1.loc[32, 'МПСПДСН'] + self.tab1.loc[32, 'МПСПОУ'] + self.tab1.loc[
            32, 'МПСПВР'] + self.tab1.loc[
                                         32, 'МПСПЭ']
        self.tab1.loc[34, 'ИМПСП'] = self.tab1.loc[34, 'МПСПДСН'] + self.tab1.loc[34, 'МПСПОУ'] + self.tab1.loc[
            34, 'МПСПВР'] + self.tab1.loc[
                                         34, 'МПСПЭ']
        self.tab1.loc[36, 'ИМПСП'] = self.tab1.loc[34, 'ИМПСП'] / self.tab1.loc[23, 'ИМПСП'] * 100

        # Столбец 'ИМППП'
        self.tab1.loc[0, 'ИМППП'] = self.tab1.loc[0, 'МПППВР'] + self.tab1.loc[0, 'МПППЭ']
        self.tab1.loc[2, 'ИМППП'] = self.tab1.loc[2, 'МПППВР'] + self.tab1.loc[2, 'МПППЭ']
        self.tab1.loc[1, 'ИМППП'] = self.tab1.loc[2, 'ИМППП'] / self.tab1.loc[0, 'ИМППП']
        self.tab1.loc[4, 'ИМППП'] = self.tab1.loc[4, 'МПППВР'] + self.tab1.loc[4, 'МПППЭ']
        self.tab1.loc[3, 'ИМППП'] = self.tab1.loc[4, 'ИМППП'] / self.tab1.loc[2, 'ИМППП'] * 1000
        self.tab1.loc[6, 'ИМППП'] = self.tab1.loc[6, 'МПППВР'] + self.tab1.loc[6, 'МПППЭ']
        self.tab1.loc[9, 'ИМППП'] = self.tab1.loc[9, 'МПППВР'] + self.tab1.loc[9, 'МПППЭ']
        self.tab1.loc[8, 'ИМППП'] = self.tab1.loc[9, 'ИМППП'] / self.tab1.loc[6, 'ИМППП'] * 1000
        self.tab1.loc[11, 'ИМППП'] = self.tab1.loc[11, 'МПППВР'] + self.tab1.loc[11, 'МПППЭ']
        self.tab1.loc[13, 'ИМППП'] = self.tab1.loc[13, 'МПППВР'] + self.tab1.loc[13, 'МПППЭ']
        self.tab1.loc[14, 'ИМППП'] = self.tab1.loc[14, 'МПППВР'] + self.tab1.loc[14, 'МПППЭ']
        self.tab1.loc[15, 'ИМППП'] = self.tab1.loc[14, 'ИМППП'] / self.tab1.loc[11, 'ИМППП'] * 1000
        self.tab1.loc[17, 'ИМППП'] = self.tab1.loc[17, 'МПППВР'] + self.tab1.loc[17, 'МПППЭ']
        self.tab1.loc[16, 'ИМППП'] = self.tab1.loc[17, 'ИМППП'] / self.tab1.loc[2, 'ИМППП'] * 100
        self.tab1.loc[19, 'ИМППП'] = self.tab1.loc[19, 'МПППВР'] + self.tab1.loc[19, 'МПППЭ']
        self.tab1.loc[21, 'ИМППП'] = self.tab1.loc[21, 'МПППВР'] + self.tab1.loc[21, 'МПППЭ']
        self.tab1.loc[22, 'ИМППП'] = self.tab1.loc[21, 'ИМППП'] / self.tab1.loc[17, 'ИМППП'] * 1000
        self.tab1.loc[23, 'ИМППП'] = self.tab1.loc[23, 'МПППВР'] + self.tab1.loc[23, 'МПППЭ']
        self.tab1.loc[24, 'ИМППП'] = self.tab1.loc[23, 'ИМППП'] / self.tab1.loc[17, 'ИМППП'] * 1000
        self.tab1.loc[32, 'ИМППП'] = self.tab1.loc[32, 'МПППВР'] + self.tab1.loc[32, 'МПППЭ']
        self.tab1.loc[34, 'ИМППП'] = self.tab1.loc[34, 'МПППВР'] + self.tab1.loc[34, 'МПППЭ']
        self.tab1.loc[36, 'ИМППП'] = self.tab1.loc[34, 'ИМППП'] / self.tab1.loc[23, 'ИМППП'] * 100

        # Столбец 'ИМПВР'
        self.tab1.loc[0, 'ИМПВР'] = self.tab1.loc[0, 'МПСПВР'] + self.tab1.loc[0, 'МПППВР']
        self.tab1.loc[2, 'ИМПВР'] = self.tab1.loc[2, 'МПСПВР'] + self.tab1.loc[2, 'МПППВР']
        self.tab1.loc[1, 'ИМПВР'] = self.tab1.loc[2, 'ИМПВР'] / self.tab1.loc[0, 'ИМПВР']
        self.tab1.loc[4, 'ИМПВР'] = self.tab1.loc[4, 'МПСПВР'] + self.tab1.loc[4, 'МПППВР']
        self.tab1.loc[3, 'ИМПВР'] = self.tab1.loc[4, 'ИМПВР'] / self.tab1.loc[2, 'ИМПВР'] * 1000
        self.tab1.loc[6, 'ИМПВР'] = self.tab1.loc[6, 'МПСПВР'] + self.tab1.loc[6, 'МПППВР']
        self.tab1.loc[9, 'ИМПВР'] = self.tab1.loc[9, 'МПСПВР'] + self.tab1.loc[9, 'МПППВР']
        self.tab1.loc[8, 'ИМПВР'] = self.tab1.loc[9, 'ИМПВР'] / self.tab1.loc[6, 'ИМПВР'] * 1000
        self.tab1.loc[11, 'ИМПВР'] = self.tab1.loc[11, 'МПСПВР'] + self.tab1.loc[11, 'МПППВР']
        self.tab1.loc[13, 'ИМПВР'] = self.tab1.loc[13, 'МПСПВР'] + self.tab1.loc[13, 'МПППВР']
        self.tab1.loc[14, 'ИМПВР'] = self.tab1.loc[14, 'МПСПВР'] + self.tab1.loc[14, 'МПППВР']
        self.tab1.loc[15, 'ИМПВР'] = self.tab1.loc[14, 'ИМПВР'] / self.tab1.loc[11, 'ИМПВР'] * 1000
        self.tab1.loc[17, 'ИМПВР'] = self.tab1.loc[17, 'МПСПВР'] + self.tab1.loc[17, 'МПППВР']
        self.tab1.loc[16, 'ИМПВР'] = self.tab1.loc[17, 'ИМПВР'] / self.tab1.loc[2, 'ИМПВР'] * 100
        self.tab1.loc[19, 'ИМПВР'] = self.tab1.loc[19, 'МПСПВР'] + self.tab1.loc[19, 'МПППВР']
        self.tab1.loc[21, 'ИМПВР'] = self.tab1.loc[21, 'МПСПВР'] + self.tab1.loc[21, 'МПППВР']
        self.tab1.loc[22, 'ИМПВР'] = self.tab1.loc[21, 'ИМПВР'] / self.tab1.loc[17, 'ИМПВР'] * 1000
        self.tab1.loc[23, 'ИМПВР'] = self.tab1.loc[23, 'МПСПВР'] + self.tab1.loc[23, 'МПППВР']
        self.tab1.loc[24, 'ИМПВР'] = self.tab1.loc[23, 'ИМПВР'] / self.tab1.loc[17, 'ИМПВР'] * 1000
        self.tab1.loc[32, 'ИМПВР'] = self.tab1.loc[32, 'МПСПВР'] + self.tab1.loc[32, 'МПППВР']
        self.tab1.loc[34, 'ИМПВР'] = self.tab1.loc[34, 'МПСПВР'] + self.tab1.loc[34, 'МПППВР']
        self.tab1.loc[36, 'ИМПВР'] = self.tab1.loc[34, 'ИМПВР'] / self.tab1.loc[23, 'ИМПВР'] * 100

        # Столбец 'ИМПЭ'
        self.tab1.loc[0, 'ИМПЭ'] = self.tab1.loc[0, 'МПСПЭ'] + self.tab1.loc[0, 'МПППЭ']
        self.tab1.loc[2, 'ИМПЭ'] = self.tab1.loc[2, 'МПСПЭ'] + self.tab1.loc[2, 'МПППЭ']
        self.tab1.loc[1, 'ИМПЭ'] = self.tab1.loc[2, 'ИМПЭ'] / self.tab1.loc[0, 'ИМПЭ']
        self.tab1.loc[4, 'ИМПЭ'] = self.tab1.loc[4, 'МПСПЭ'] + self.tab1.loc[4, 'МПППЭ']
        self.tab1.loc[3, 'ИМПЭ'] = self.tab1.loc[4, 'ИМПЭ'] / self.tab1.loc[2, 'ИМПЭ'] * 1000
        self.tab1.loc[6, 'ИМПЭ'] = self.tab1.loc[6, 'МПСПЭ'] + self.tab1.loc[6, 'МПППЭ']
        self.tab1.loc[9, 'ИМПЭ'] = self.tab1.loc[9, 'МПСПЭ'] + self.tab1.loc[9, 'МПППЭ']
        self.tab1.loc[8, 'ИМПЭ'] = self.tab1.loc[9, 'ИМПЭ'] / self.tab1.loc[6, 'ИМПЭ'] * 1000
        self.tab1.loc[11, 'ИМПЭ'] = self.tab1.loc[11, 'МПСПЭ'] + self.tab1.loc[11, 'МПППЭ']
        self.tab1.loc[13, 'ИМПЭ'] = self.tab1.loc[13, 'МПСПЭ'] + self.tab1.loc[13, 'МПППЭ']
        self.tab1.loc[14, 'ИМПЭ'] = self.tab1.loc[14, 'МПСПЭ'] + self.tab1.loc[14, 'МПППЭ']
        self.tab1.loc[15, 'ИМПЭ'] = self.tab1.loc[14, 'ИМПЭ'] / self.tab1.loc[11, 'ИМПЭ'] * 1000
        self.tab1.loc[17, 'ИМПЭ'] = self.tab1.loc[17, 'МПСПЭ'] + self.tab1.loc[17, 'МПППЭ']
        self.tab1.loc[16, 'ИМПЭ'] = self.tab1.loc[17, 'ИМПЭ'] / self.tab1.loc[2, 'ИМПЭ'] * 100
        self.tab1.loc[19, 'ИМПЭ'] = self.tab1.loc[19, 'МПСПЭ'] + self.tab1.loc[19, 'МПППЭ']
        self.tab1.loc[21, 'ИМПЭ'] = self.tab1.loc[21, 'МПСПЭ'] + self.tab1.loc[21, 'МПППЭ']
        self.tab1.loc[22, 'ИМПЭ'] = self.tab1.loc[21, 'ИМПЭ'] / self.tab1.loc[17, 'ИМПЭ'] * 1000
        self.tab1.loc[23, 'ИМПЭ'] = self.tab1.loc[23, 'МПСПЭ'] + self.tab1.loc[23, 'МПППЭ']
        self.tab1.loc[24, 'ИМПЭ'] = self.tab1.loc[23, 'ИМПЭ'] / self.tab1.loc[17, 'ИМПЭ'] * 1000
        self.tab1.loc[32, 'ИМПЭ'] = self.tab1.loc[32, 'МПСПЭ'] + self.tab1.loc[32, 'МПППЭ']
        self.tab1.loc[33, 'ИМПЭ'] = self.tab1.loc[33, 'МПСПЭ'] + self.tab1.loc[33, 'МПППЭ']
        self.tab1.loc[34, 'ИМПЭ'] = self.tab1.loc[34, 'МПСПЭ'] + self.tab1.loc[34, 'МПППЭ']
        self.tab1.loc[35, 'ИМПЭ'] = self.tab1.loc[35, 'МПСПЭ'] + self.tab1.loc[35, 'МПППЭ']
        self.tab1.loc[36, 'ИМПЭ'] = self.tab1.loc[34, 'ИМПЭ'] / self.tab1.loc[23, 'ИМПЭ'] * 100
        self.tab1.loc[37, 'ИМПЭ'] = self.tab1.loc[35, 'ИМПЭ'] / self.tab1.loc[23, 'ИМПЭ'] * 100

        # Столбец 'ИВМП'
        self.tab1.loc[0, 'ИВМП'] = self.tab1.loc[0, 'ИМПСП'] + self.tab1.loc[0, 'ИМППП'] + self.tab1.loc[0, 'ИМПВР'] + \
                                   self.tab1.loc[0, 'ИМПЭ']
        self.tab1.loc[2, 'ИВМП'] = self.tab1.loc[2, 'ИМПСП'] + self.tab1.loc[2, 'ИМППП'] + self.tab1.loc[2, 'ИМПВР'] + \
                                   self.tab1.loc[2, 'ИМПЭ']
        self.tab1.loc[1, 'ИВМП'] = self.tab1.loc[2, 'ИВМП'] / self.tab1.loc[0, 'ИВМП']
        self.tab1.loc[4, 'ИВМП'] = self.tab1.loc[4, 'ИМПСП'] + self.tab1.loc[4, 'ИМППП'] + self.tab1.loc[4, 'ИМПВР'] + \
                                   self.tab1.loc[4, 'ИМПЭ']
        self.tab1.loc[3, 'ИВМП'] = self.tab1.loc[4, 'ИВМП'] / self.tab1.loc[2, 'ИВМП'] * 1000
        self.tab1.loc[6, 'ИВМП'] = self.tab1.loc[6, 'ИМПСП'] + self.tab1.loc[6, 'ИМППП'] + self.tab1.loc[6, 'ИМПВР'] + \
                                   self.tab1.loc[6, 'ИМПЭ']
        self.tab1.loc[9, 'ИВМП'] = self.tab1.loc[9, 'ИМПСП'] + self.tab1.loc[9, 'ИМППП'] + self.tab1.loc[9, 'ИМПВР'] + \
                                   self.tab1.loc[9, 'ИМПЭ']
        self.tab1.loc[8, 'ИВМП'] = self.tab1.loc[9, 'ИВМП'] / self.tab1.loc[6, 'ИВМП'] * 1000
        self.tab1.loc[11, 'ИВМП'] = self.tab1.loc[11, 'ИМПСП'] + self.tab1.loc[11, 'ИМППП'] + self.tab1.loc[
            11, 'ИМПВР'] + self.tab1.loc[
                                        11, 'ИМПЭ']
        self.tab1.loc[13, 'ИВМП'] = self.tab1.loc[13, 'ИМПСП'] + self.tab1.loc[13, 'ИМППП'] + self.tab1.loc[
            13, 'ИМПВР'] + self.tab1.loc[
                                        13, 'ИМПЭ']
        self.tab1.loc[14, 'ИВМП'] = self.tab1.loc[14, 'ИМПСП'] + self.tab1.loc[14, 'ИМППП'] + self.tab1.loc[
            14, 'ИМПВР'] + self.tab1.loc[
                                        14, 'ИМПЭ']
        self.tab1.loc[15, 'ИВМП'] = self.tab1.loc[14, 'ИВМП'] / self.tab1.loc[11, 'ИВМП'] * 1000
        self.tab1.loc[17, 'ИВМП'] = self.tab1.loc[17, 'ИМПСП'] + self.tab1.loc[17, 'ИМППП'] + self.tab1.loc[
            17, 'ИМПВР'] + self.tab1.loc[
                                        17, 'ИМПЭ']
        self.tab1.loc[16, 'ИВМП'] = self.tab1.loc[17, 'ИВМП'] / self.tab1.loc[2, 'ИВМП'] * 100
        self.tab1.loc[19, 'ИВМП'] = self.tab1.loc[19, 'ИМПСП'] + self.tab1.loc[19, 'ИМППП'] + self.tab1.loc[
            19, 'ИМПВР'] + self.tab1.loc[
                                        19, 'ИМПЭ']
        self.tab1.loc[21, 'ИВМП'] = self.tab1.loc[21, 'ИМПСП'] + self.tab1.loc[21, 'ИМППП'] + self.tab1.loc[
            21, 'ИМПВР'] + self.tab1.loc[
                                        21, 'ИМПЭ']
        self.tab1.loc[22, 'ИВМП'] = self.tab1.loc[21, 'ИВМП'] / self.tab1.loc[17, 'ИВМП'] * 1000
        self.tab1.loc[23, 'ИВМП'] = self.tab1.loc[23, 'ИМПСП'] + self.tab1.loc[23, 'ИМППП'] + self.tab1.loc[
            23, 'ИМПВР'] + self.tab1.loc[
                                        23, 'ИМПЭ']
        self.tab1.loc[24, 'ИВМП'] = self.tab1.loc[23, 'ИВМП'] / self.tab1.loc[17, 'ИВМП'] * 1000
        self.tab1.loc[32, 'ИВМП'] = self.tab1.loc[32, 'ИМПСП'] + self.tab1.loc[32, 'ИМППП'] + self.tab1.loc[
            32, 'ИМПВР'] + self.tab1.loc[
                                        32, 'ИМПЭ']
        self.tab1.loc[33, 'ИВМП'] = self.tab1.loc[33, 'ИМПЭ']
        self.tab1.loc[34, 'ИВМП'] = self.tab1.loc[34, 'ИМПСП'] + self.tab1.loc[34, 'ИМППП'] + self.tab1.loc[
            34, 'ИМПВР'] + self.tab1.loc[
                                        34, 'ИМПЭ']
        self.tab1.loc[35, 'ИВМП'] = self.tab1.loc[35, 'ИМПЭ']
        self.tab1.loc[36, 'ИВМП'] = self.tab1.loc[34, 'ИВМП'] / self.tab1.loc[23, 'ИВМП'] * 100
        self.tab1.loc[37, 'ИВМП'] = self.tab1.loc[35, 'ИВМП'] / self.tab1.loc[23, 'ИВМП'] * 100

        # Столбец 'ИММП'
        self.tab1.loc[0, 'ИММП'] = self.tab1.loc[0, 'ИМ'] + self.tab1.loc[0, 'ИВМП']
        self.tab1.loc[2, 'ИММП'] = self.tab1.loc[2, 'ИМ'] + self.tab1.loc[2, 'ИВМП']
        self.tab1.loc[1, 'ИММП'] = self.tab1.loc[2, 'ИММП'] / self.tab1.loc[0, 'ИММП']
        self.tab1.loc[4, 'ИММП'] = self.tab1.loc[4, 'ИМ'] + self.tab1.loc[4, 'ИВМП']
        self.tab1.loc[3, 'ИММП'] = self.tab1.loc[4, 'ИММП'] / self.tab1.loc[2, 'ИММП'] * 1000
        self.tab1.loc[6, 'ИММП'] = self.tab1.loc[6, 'ИВМП'] + self.tab1.loc[6, 'ИМ']
        self.tab1.loc[9, 'ИММП'] = self.tab1.loc[9, 'ИВМП'] + self.tab1.loc[9, 'ИМ']
        self.tab1.loc[8, 'ИММП'] = self.tab1.loc[9, 'ИММП'] / self.tab1.loc[6, 'ИММП'] * 1000
        self.tab1.loc[11, 'ИММП'] = self.tab1.loc[11, 'ИВМП'] + self.tab1.loc[11, 'ИМ']
        self.tab1.loc[13, 'ИММП'] = self.tab1.loc[13, 'ИВМП'] + self.tab1.loc[13, 'ИМ']
        self.tab1.loc[14, 'ИММП'] = self.tab1.loc[14, 'ИВМП'] + self.tab1.loc[14, 'ИМ']
        self.tab1.loc[15, 'ИММП'] = self.tab1.loc[14, 'ИММП'] / self.tab1.loc[11, 'ИММП'] * 1000
        self.tab1.loc[17, 'ИММП'] = self.tab1.loc[17, 'ИВМП'] + self.tab1.loc[17, 'ИМ']
        self.tab1.loc[16, 'ИММП'] = self.tab1.loc[17, 'ИММП'] / self.tab1.loc[2, 'ИММП'] * 100
        self.tab1.loc[19, 'ИММП'] = self.tab1.loc[19, 'ИВМП'] + self.tab1.loc[19, 'ИМ']
        self.tab1.loc[21, 'ИММП'] = self.tab1.loc[21, 'ИВМП'] + self.tab1.loc[21, 'ИМ']
        self.tab1.loc[22, 'ИММП'] = self.tab1.loc[21, 'ИММП'] / self.tab1.loc[17, 'ИММП'] * 1000
        self.tab1.loc[23, 'ИММП'] = self.tab1.loc[23, 'ИВМП'] + self.tab1.loc[23, 'ИМ']
        self.tab1.loc[24, 'ИММП'] = self.tab1.loc[23, 'ИММП'] / self.tab1.loc[17, 'ИММП'] * 1000
        self.tab1.loc[32, 'ИММП'] = self.tab1.loc[32, 'ИВМП'] + self.tab1.loc[30, 'ИМ']
        self.tab1.loc[33, 'ИММП'] = self.tab1.loc[33, 'ИВМП']
        self.tab1.loc[34, 'ИММП'] = self.tab1.loc[34, 'ИВМП'] + self.tab1.loc[34, 'ИМ']
        self.tab1.loc[35, 'ИММП'] = self.tab1.loc[35, 'ИМ'] + self.tab1.loc[35, 'ИВМП']
        self.tab1.loc[36, 'ИММП'] = self.tab1.loc[34, 'ИММП'] / self.tab1.loc[23, 'ИММП'] * 100
        self.tab1.loc[37, 'ИММП'] = self.tab1.loc[35, 'ИММП'] / self.tab1.loc[23, 'ИММП'] * 100

        # Столбец 'ИСХ'
        self.tab1.loc[0, 'ИСХ'] = self.tab1.loc[0, 'ИММП'] - self.tab1.loc[0, 'ИМППП']
        self.tab1.loc[2, 'ИСХ'] = self.tab1.loc[2, 'ИММП'] - self.tab1.loc[2, 'ИМППП']
        self.tab1.loc[1, 'ИСХ'] = self.tab1.loc[2, 'ИСХ'] / self.tab1.loc[0, 'ИСХ']
        self.tab1.loc[4, 'ИСХ'] = self.tab1.loc[4, 'ИММП'] - self.tab1.loc[4, 'ИМППП']
        self.tab1.loc[3, 'ИСХ'] = self.tab1.loc[4, 'ИСХ'] / self.tab1.loc[2, 'ИСХ'] * 1000
        self.tab1.loc[6, 'ИСХ'] = self.tab1.loc[6, 'ИММП'] - self.tab1.loc[6, 'ИМППП']
        self.tab1.loc[9, 'ИСХ'] = self.tab1.loc[9, 'ИММП'] - self.tab1.loc[9, 'ИМППП']
        self.tab1.loc[8, 'ИСХ'] = self.tab1.loc[9, 'ИСХ'] / self.tab1.loc[6, 'ИСХ'] * 1000
        self.tab1.loc[11, 'ИСХ'] = self.tab1.loc[11, 'ИММП'] - self.tab1.loc[11, 'ИМ']
        self.tab1.loc[13, 'ИСХ'] = self.tab1.loc[13, 'ИММП'] - self.tab1.loc[13, 'ИМППП']
        self.tab1.loc[14, 'ИСХ'] = self.tab1.loc[14, 'ИММП'] - self.tab1.loc[14, 'ИМППП']
        self.tab1.loc[15, 'ИСХ'] = self.tab1.loc[14, 'ИСХ'] / self.tab1.loc[11, 'ИСХ'] * 1000
        self.tab1.loc[17, 'ИСХ'] = self.tab1.loc[17, 'ИММП'] - self.tab1.loc[17, 'ИМ']
        self.tab1.loc[16, 'ИСХ'] = self.tab1.loc[17, 'ИСХ'] / self.tab1.loc[2, 'ИСХ'] * 100
        self.tab1.loc[19, 'ИСХ'] = self.tab1.loc[19, 'ИММП'] - self.tab1.loc[19, 'ИМППП']
        self.tab1.loc[21, 'ИСХ'] = self.tab1.loc[21, 'ИММП'] - self.tab1.loc[21, 'ИМППП']
        self.tab1.loc[22, 'ИСХ'] = self.tab1.loc[21, 'ИСХ'] / self.tab1.loc[17, 'ИСХ'] * 1000
        self.tab1.loc[23, 'ИСХ'] = self.tab1.loc[23, 'ИММП'] - self.tab1.loc[23, 'ИМППП']
        self.tab1.loc[24, 'ИСХ'] = self.tab1.loc[23, 'ИСХ'] / self.tab1.loc[17, 'ИСХ'] * 1000
        self.tab1.loc[32, 'ИСХ'] = self.tab1.loc[32, 'ИММП'] - self.tab1.loc[32, 'ИМППП']
        self.tab1.loc[34, 'ИСХ'] = self.tab1.loc[34, 'ИММП'] - self.tab1.loc[34, 'ИМППП']
        self.tab1.loc[36, 'ИСХ'] = self.tab1.loc[34, 'ИСХ'] / self.tab1.loc[23, 'ИСХ'] * 100

    def cal_tab5(self):
        self.tab5.loc[0, 'СХО'] = self.tab1.loc[0, 'СХО']
        self.tab5.loc[1, 'СХО'] = self.tab1.loc[1, 'СХО']
        self.tab5.loc[2, 'СХО'] = self.tab5.loc[0, 'СХО'] * self.tab5.loc[1, 'СХО']
        self.tab5.loc[3, 'СХО'] = self.tab1.loc[3, 'СХО']
        self.tab5.loc[4, 'СХО'] = self.tab5.loc[3, 'СХО'] * self.tab5.loc[2, 'СХО'] / 1000

        # Столбец 'ВРПМВР'
        self.tab5.loc[0, 'ВРПМВР'] = self.tab1.loc[1, 'СХО'] * self.tab5.loc[8, 'ВРПМВР'] * self.tab5.loc[6, 'ВРПМЭ']
        self.tab5.loc[2, 'ВРПМВР'] = self.tab1.loc[3, 'СХО'] * self.tab5.loc[6, 'ВРПМЭ'] * self.tab5.loc[8, 'ВРПМВР'] * \
                                     self.tab5.loc[
                                         9, 'ВРПМВР']
        self.tab5.loc[4, 'ВРПМВР'] = self.tab1.loc[4, 'СХО'] * self.tab5.loc[2, 'ВРПМВР'] / 1000

        # Столбец 'ВРПМЭ'
        self.tab5.loc[0, 'ВРПМЭ'] = self.tab1.loc[1, 'СХО'] * self.tab5.loc[8, 'ВРПМЭ'] * self.tab5.loc[6, 'ВРПМЭ']
        self.tab5.loc[2, 'ВРПМЭ'] = self.tab1.loc[3, 'СХО'] * self.tab5.loc[8, 'ВРПМЭ'] * self.tab5.loc[6, 'ВРПМЭ'] * \
                                    self.tab5.loc[9, 'ВРПМЭ']
        self.tab5.loc[4, 'ВРПМЭ'] = self.tab1.loc[4, 'СХО'] * self.tab5.loc[2, 'ВРПМЭ'] / 1000

        # Столбец 'ВРПМПСПСН'
        self.tab5.loc[0, 'ВРПМПСПСН'] = self.tab1.loc[1, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПСН'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                            6, 'ВРПМПППЭ']
        self.tab5.loc[2, 'ВРПМПСПСН'] = self.tab1.loc[3, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПСН'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                            6, 'ВРПМПППЭ'] * self.tab5.loc[9, 'ВРПМПСПСН']
        self.tab5.loc[4, 'ВРПМПСПСН'] = self.tab1.loc[4, 'СХО'] * self.tab5.loc[2, 'ВРПМПСПСН'] / 1000

        # Столбец 'ВРПМПСПОУ'
        self.tab5.loc[0, 'ВРПМПСПОУ'] = self.tab1.loc[1, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПОУ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                            6, 'ВРПМПППЭ']
        self.tab5.loc[2, 'ВРПМПСПОУ'] = self.tab1.loc[3, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПОУ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                            6, 'ВРПМПППЭ'] * self.tab5.loc[9, 'ВРПМПСПОУ']
        self.tab5.loc[4, 'ВРПМПСПОУ'] = self.tab1.loc[4, 'СХО'] * self.tab5.loc[2, 'ВРПМПСПОУ'] / 1000

        # Столбец 'ВРПМПСПВР'
        self.tab5.loc[0, 'ВРПМПСПВР'] = self.tab1.loc[1, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПВР'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                            6, 'ВРПМПППЭ']
        self.tab5.loc[2, 'ВРПМПСПВР'] = self.tab1.loc[3, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПВР'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                            6, 'ВРПМПППЭ'] * self.tab5.loc[9, 'ВРПМПСПВР']
        self.tab5.loc[4, 'ВРПМПСПВР'] = self.tab1.loc[4, 'СХО'] * self.tab5.loc[2, 'ВРПМПСПВР'] / 1000

        # Столбец 'ВРПМПСПЭ'
        self.tab5.loc[0, 'ВРПМПСПЭ'] = self.tab1.loc[1, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПЭ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                           6, 'ВРПМПППЭ']
        self.tab5.loc[2, 'ВРПМПСПЭ'] = self.tab1.loc[3, 'СХО'] * self.tab5.loc[8, 'ВРПМПСПЭ'] * self.tab5.loc[
            7, 'ВРПМПСПЭ'] * self.tab5.loc[
                                           6, 'ВРПМПППЭ'] * self.tab5.loc[9, 'ВРПМПСПЭ']
        self.tab5.loc[4, 'ВРПМПСПЭ'] = self.tab1.loc[4, 'СХО'] * self.tab5.loc[2, 'ВРПМПСПЭ'] / 1000

        # Столбец 'ВРПМПППВР'
        self.tab5.loc[0, 'ВРПМПППВР'] = self.tab1.loc[1, 'СХО'] * self.tab5.loc[8, 'ВРПМПППВР'] * self.tab5.loc[
            7, 'ВРПМПППЭ'] * self.tab5.loc[
                                            6, 'ВРПМПППЭ']
        self.tab5.loc[2, 'ВРПМПППВР'] = self.tab1.loc[3, 'СХО'] * self.tab5.loc[6, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПППЭ'] * self.tab5.loc[
                                            8, 'ВРПМПППВР'] * self.tab5.loc[9, 'ВРПМПППВР']
        self.tab5.loc[4, 'ВРПМПППВР'] = self.tab1.loc[4, 'СХО'] * self.tab5.loc[2, 'ВРПМПППВР'] / 1000

        # Столбец 'ВРПМПППЭ'
        self.tab5.loc[0, 'ВРПМПППЭ'] = self.tab1.loc[1, 'СХО'] * self.tab5.loc[8, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПППЭ'] * self.tab5.loc[
                                           6, 'ВРПМПППЭ']
        self.tab5.loc[2, 'ВРПМПППЭ'] = self.tab1.loc[3, 'СХО'] * self.tab5.loc[8, 'ВРПМПППЭ'] * self.tab5.loc[
            7, 'ВРПМПППЭ'] * self.tab5.loc[
                                           6, 'ВРПМПППЭ'] * self.tab5.loc[9, 'ВРПМПППЭ']
        self.tab5.loc[4, 'ВРПМПППЭ'] = self.tab1.loc[4, 'СХО'] * self.tab5.loc[2, 'ВРПМПППЭ'] / 1000

    def cal_tab6(self):
        self.tab6.loc[0, 'НСВМ'] = self.tab1.loc[0, 'СХО']
        self.tab6.loc[1, 'НСВМ'] = self.tab1.loc[1, 'СХО']
        self.tab6.loc[2, 'НСВМ'] = self.tab1.loc[2, 'СХО']
        self.tab6.loc[3, 'НСВМ'] = self.tab1.loc[3, 'СХО']
        self.tab6.loc[4, 'НСВМ'] = self.tab1.loc[4, 'СХО']
        self.tab6.loc[2, 'СХО'] = self.tab6.loc[0, 'СХО'] * self.tab6.loc[1, 'СХО']

    def cal_tab3(self):
        # Столбец 'ЭФиДГ1Э'
        self.tab3.loc[2, 'ЭФиДГ1Э'] = self.tab3.loc[0, 'ЭФиДГ1Э'] * self.tab3.loc[1, 'ЭФиДГ1Э'] / 1000
        self.tab3.loc[5, 'ЭФиДГ1Э'] = self.tab3.loc[0, 'ЭФиДГ1Э'] * self.tab3.loc[3, 'ЭФиДГ1Э']
        self.tab3.loc[6, 'ЭФиДГ1Э'] = self.tab3.loc[1, 'ЭФиДГ1Э'] * self.tab3.loc[4, 'ЭФиДГ1Э']
        self.tab3.loc[7, 'ЭФиДГ1Э'] = self.tab3.loc[5, 'ЭФиДГ1Э'] + self.tab3.loc[6, 'ЭФиДГ1Э']
        self.tab3.loc[8, 'ЭФиДГ1Э'] = self.tab3.loc[7, 'ЭФиДГ1Э'] / self.tab3.loc[2, 'ЭФиДГ1Э']
        self.tab3.loc[9, 'ЭФиДГ1Э'] = self.tab3.loc[7, 'ЭФиДГ1Э'] * self.tab3.loc[9, 'ед.изм']
        self.tab3.loc[10, 'ЭФиДГ1Э'] = self.tab3.loc[7, 'ЭФиДГ1Э'] * self.tab3.loc[10, 'ед.изм']
        self.tab3.loc[11, 'ЭФиДГ1Э'] = self.tab3.loc[7, 'ЭФиДГ1Э'] * self.tab3.loc[11, 'ед.изм']
        self.tab3.loc[12, 'ЭФиДГ1Э'] = self.tab3.loc[9, 'ЭФиДГ1Э'] + self.tab3.loc[10, 'ЭФиДГ1Э'] + self.tab3.loc[
            11, 'ЭФиДГ1Э']
        self.tab3.loc[13, 'ЭФиДГ1Э'] = self.tab3.loc[7, 'ЭФиДГ1Э'] / self.tab3.loc[0, 'ЭФиДГ1Э']
        self.tab3.loc[14, 'ЭФиДГ1Э'] = self.tab3.loc[12, 'ЭФиДГ1Э'] / self.tab3.loc[0, 'ЭФиДГ1Э']
        self.tab3.loc[15, 'ЭФиДГ1Э'] = self.tab3.loc[13, 'ЭФиДГ1Э'] + self.tab3.loc[14, 'ЭФиДГ1Э']

        # Столбец 'ЭФиДГ1П'
        self.tab3.loc[2, 'ЭФиДГ1П'] = self.tab3.loc[0, 'ЭФиДГ1П'] * self.tab3.loc[1, 'ЭФиДГ1П'] / 1000
        self.tab3.loc[5, 'ЭФиДГ1П'] = self.tab3.loc[0, 'ЭФиДГ1П'] * self.tab3.loc[3, 'ЭФиДГ1П']
        self.tab3.loc[6, 'ЭФиДГ1П'] = self.tab3.loc[1, 'ЭФиДГ1П'] * self.tab3.loc[4, 'ЭФиДГ1П']
        self.tab3.loc[7, 'ЭФиДГ1П'] = self.tab3.loc[5, 'ЭФиДГ1П'] + self.tab3.loc[6, 'ЭФиДГ1П']
        self.tab3.loc[8, 'ЭФиДГ1П'] = self.tab3.loc[7, 'ЭФиДГ1П'] / self.tab3.loc[2, 'ЭФиДГ1П']
        self.tab3.loc[9, 'ЭФиДГ1П'] = self.tab3.loc[7, 'ЭФиДГ1П'] * self.tab3.loc[9, 'ед.изм']
        self.tab3.loc[10, 'ЭФиДГ1П'] = self.tab3.loc[7, 'ЭФиДГ1П'] * self.tab3.loc[10, 'ед.изм']
        self.tab3.loc[11, 'ЭФиДГ1П'] = self.tab3.loc[7, 'ЭФиДГ1П'] * self.tab3.loc[11, 'ед.изм']
        self.tab3.loc[12, 'ЭФиДГ1П'] = self.tab3.loc[9, 'ЭФиДГ1П'] + self.tab3.loc[10, 'ЭФиДГ1П'] + self.tab3.loc[
            11, 'ЭФиДГ1П']
        self.tab3.loc[13, 'ЭФиДГ1П'] = self.tab3.loc[7, 'ЭФиДГ1П'] / self.tab3.loc[0, 'ЭФиДГ1П']
        self.tab3.loc[14, 'ЭФиДГ1П'] = self.tab3.loc[12, 'ЭФиДГ1П'] / self.tab3.loc[0, 'ЭФиДГ1П']
        self.tab3.loc[15, 'ЭФиДГ1П'] = self.tab3.loc[13, 'ЭФиДГ1П'] + self.tab3.loc[14, 'ЭФиДГ1П']

        # Столбец 'ЭФиДГ2РП'
        self.tab3.loc[2, 'ЭФиДГ2РП'] = self.tab3.loc[0, 'ЭФиДГ2РП'] * self.tab3.loc[1, 'ЭФиДГ2РП'] / 1000
        self.tab3.loc[5, 'ЭФиДГ2РП'] = self.tab3.loc[0, 'ЭФиДГ2РП'] * self.tab3.loc[3, 'ЭФиДГ2РП']
        self.tab3.loc[6, 'ЭФиДГ2РП'] = self.tab3.loc[1, 'ЭФиДГ2РП'] * self.tab3.loc[4, 'ЭФиДГ2РП']
        self.tab3.loc[7, 'ЭФиДГ2РП'] = self.tab3.loc[5, 'ЭФиДГ2РП'] + self.tab3.loc[6, 'ЭФиДГ2РП']
        self.tab3.loc[8, 'ЭФиДГ2РП'] = self.tab3.loc[7, 'ЭФиДГ2РП'] / self.tab3.loc[2, 'ЭФиДГ2РП']
        self.tab3.loc[9, 'ЭФиДГ2РП'] = self.tab3.loc[7, 'ЭФиДГ2РП'] * self.tab3.loc[9, 'ед.изм']
        self.tab3.loc[10, 'ЭФиДГ2РП'] = self.tab3.loc[7, 'ЭФиДГ2РП'] * self.tab3.loc[10, 'ед.изм']
        self.tab3.loc[11, 'ЭФиДГ2РП'] = self.tab3.loc[7, 'ЭФиДГ2РП'] * self.tab3.loc[11, 'ед.изм']
        self.tab3.loc[12, 'ЭФиДГ2РП'] = self.tab3.loc[9, 'ЭФиДГ2РП'] + self.tab3.loc[10, 'ЭФиДГ2РП'] + self.tab3.loc[
            11, 'ЭФиДГ2РП']
        self.tab3.loc[13, 'ЭФиДГ2РП'] = self.tab3.loc[7, 'ЭФиДГ2РП'] / self.tab3.loc[0, 'ЭФиДГ2РП']
        self.tab3.loc[14, 'ЭФиДГ2РП'] = self.tab3.loc[12, 'ЭФиДГ2РП'] / self.tab3.loc[0, 'ЭФиДГ2РП']
        self.tab3.loc[15, 'ЭФиДГ2РП'] = self.tab3.loc[13, 'ЭФиДГ2РП'] + self.tab3.loc[14, 'ЭФиДГ2РП']

        # Столбец 'ЭФиДГ2МП'
        self.tab3.loc[2, 'ЭФиДГ2МП'] = self.tab3.loc[0, 'ЭФиДГ2МП'] * self.tab3.loc[1, 'ЭФиДГ2МП'] / 1000
        self.tab3.loc[5, 'ЭФиДГ2МП'] = self.tab3.loc[0, 'ЭФиДГ2МП'] * self.tab3.loc[3, 'ЭФиДГ2МП']
        self.tab3.loc[6, 'ЭФиДГ2МП'] = self.tab3.loc[1, 'ЭФиДГ2МП'] * self.tab3.loc[4, 'ЭФиДГ2МП']
        self.tab3.loc[7, 'ЭФиДГ2МП'] = self.tab3.loc[5, 'ЭФиДГ2МП'] + self.tab3.loc[6, 'ЭФиДГ2МП']
        self.tab3.loc[8, 'ЭФиДГ2МП'] = self.tab3.loc[7, 'ЭФиДГ2МП'] / self.tab3.loc[2, 'ЭФиДГ2МП']
        self.tab3.loc[9, 'ЭФиДГ2МП'] = self.tab3.loc[7, 'ЭФиДГ2МП'] * self.tab3.loc[9, 'ед.изм']
        self.tab3.loc[10, 'ЭФиДГ2МП'] = self.tab3.loc[7, 'ЭФиДГ2МП'] * self.tab3.loc[10, 'ед.изм']
        self.tab3.loc[11, 'ЭФиДГ2МП'] = self.tab3.loc[7, 'ЭФиДГ2МП'] * self.tab3.loc[11, 'ед.изм']
        self.tab3.loc[12, 'ЭФиДГ2МП'] = self.tab3.loc[9, 'ЭФиДГ2МП'] + self.tab3.loc[10, 'ЭФиДГ2МП'] + self.tab3.loc[
            11, 'ЭФиДГ2МП']
        self.tab3.loc[13, 'ЭФиДГ2МП'] = self.tab3.loc[7, 'ЭФиДГ2МП'] / self.tab3.loc[0, 'ЭФиДГ2МП']
        self.tab3.loc[14, 'ЭФиДГ2МП'] = self.tab3.loc[12, 'ЭФиДГ2МП'] / self.tab3.loc[0, 'ЭФиДГ2МП']
        self.tab3.loc[15, 'ЭФиДГ2МП'] = self.tab3.loc[13, 'ЭФиДГ2МП'] + self.tab3.loc[14, 'ЭФиДГ2МП']

        # Столбец 'ЭФиДГ2МПН'
        self.tab3.loc[2, 'ЭФиДГ2МПН'] = self.tab3.loc[0, 'ЭФиДГ2МПН'] * self.tab3.loc[1, 'ЭФиДГ2МПН'] / 1000
        self.tab3.loc[5, 'ЭФиДГ2МПН'] = self.tab3.loc[0, 'ЭФиДГ2МПН'] * self.tab3.loc[3, 'ЭФиДГ2МПН']
        self.tab3.loc[6, 'ЭФиДГ2МПН'] = self.tab3.loc[1, 'ЭФиДГ2МПН'] * self.tab3.loc[4, 'ЭФиДГ2МПН']
        self.tab3.loc[7, 'ЭФиДГ2МПН'] = self.tab3.loc[5, 'ЭФиДГ2МПН'] + self.tab3.loc[6, 'ЭФиДГ2МПН']
        self.tab3.loc[8, 'ЭФиДГ2МПН'] = self.tab3.loc[7, 'ЭФиДГ2МПН'] / self.tab3.loc[2, 'ЭФиДГ2МПН']
        self.tab3.loc[9, 'ЭФиДГ2МПН'] = self.tab3.loc[7, 'ЭФиДГ2МПН'] * self.tab3.loc[9, 'ед.изм']
        self.tab3.loc[10, 'ЭФиДГ2МПН'] = self.tab3.loc[7, 'ЭФиДГ2МПН'] * self.tab3.loc[10, 'ед.изм']
        self.tab3.loc[11, 'ЭФиДГ2МПН'] = self.tab3.loc[7, 'ЭФиДГ2МПН'] * self.tab3.loc[11, 'ед.изм']
        self.tab3.loc[12, 'ЭФиДГ2МПН'] = self.tab3.loc[9, 'ЭФиДГ2МПН'] + self.tab3.loc[10, 'ЭФиДГ2МПН'] + self.tab3.loc[
            11, 'ЭФиДГ2МПН']
        self.tab3.loc[13, 'ЭФиДГ2МПН'] = self.tab3.loc[7, 'ЭФиДГ2МПН'] / self.tab3.loc[0, 'ЭФиДГ2МПН']
        self.tab3.loc[14, 'ЭФиДГ2МПН'] = self.tab3.loc[12, 'ЭФиДГ2МПН'] / self.tab3.loc[0, 'ЭФиДГ2МПН']
        self.tab3.loc[15, 'ЭФиДГ2МПН'] = self.tab3.loc[13, 'ЭФиДГ2МПН'] + self.tab3.loc[14, 'ЭФиДГ2МПН']

        # Столбец 'ЭФиДГВЗЖД'
        self.tab3.loc[1, 'ЭФиДГВЗЖД'] = self.tab3.loc[1, 'ЭФиДГ1Э'] + self.tab3.loc[1, 'ЭФиДГ1П']
        self.tab3.loc[2, 'ЭФиДГВЗЖД'] = self.tab3.loc[0, 'ЭФиДГВЗЖД'] * self.tab3.loc[1, 'ЭФиДГВЗЖД'] / 1000
        self.tab3.loc[5, 'ЭФиДГВЗЖД'] = self.tab3.loc[5, 'ЭФиДГ1Э'] + self.tab3.loc[5, 'ЭФиДГ1П']
        self.tab3.loc[6, 'ЭФиДГВЗЖД'] = self.tab3.loc[6, 'ЭФиДГ1Э'] + self.tab3.loc[6, 'ЭФиДГ1П']
        self.tab3.loc[7, 'ЭФиДГВЗЖД'] = self.tab3.loc[5, 'ЭФиДГВЗЖД'] + self.tab3.loc[6, 'ЭФиДГВЗЖД']
        self.tab3.loc[8, 'ЭФиДГВЗЖД'] = self.tab3.loc[7, 'ЭФиДГВЗЖД'] / self.tab3.loc[2, 'ЭФиДГВЗЖД']
        self.tab3.loc[9, 'ЭФиДГВЗЖД'] = self.tab3.loc[7, 'ЭФиДГВЗЖД'] * self.tab3.loc[9, 'ед.изм']
        self.tab3.loc[10, 'ЭФиДГВЗЖД'] = self.tab3.loc[7, 'ЭФиДГВЗЖД'] * self.tab3.loc[10, 'ед.изм']
        self.tab3.loc[11, 'ЭФиДГВЗЖД'] = self.tab3.loc[7, 'ЭФиДГВЗЖД'] * self.tab3.loc[11, 'ед.изм']
        self.tab3.loc[12, 'ЭФиДГВЗЖД'] = self.tab3.loc[9, 'ЭФиДГВЗЖД'] + self.tab3.loc[10, 'ЭФиДГВЗЖД'] + self.tab3.loc[
            11, 'ЭФиДГВЗЖД']
        self.tab3.loc[13, 'ЭФиДГВЗЖД'] = self.tab3.loc[7, 'ЭФиДГВЗЖД'] / self.tab3.loc[0, 'ЭФиДГВЗЖД']
        self.tab3.loc[14, 'ЭФиДГВЗЖД'] = self.tab3.loc[12, 'ЭФиДГВЗЖД'] / self.tab3.loc[0, 'ЭФиДГВЗЖД']
        self.tab3.loc[15, 'ЭФиДГВЗЖД'] = self.tab3.loc[13, 'ЭФиДГВЗЖД'] + self.tab3.loc[14, 'ЭФиДГВЗЖД']

        # Столбец 'ЭФиДГВЗВТ'
        self.tab3.loc[1, 'ЭФиДГВЗВТ'] = self.tab3.loc[1, 'ЭФиДГ2РП'] + self.tab3.loc[1, 'ЭФиДГ2МП'] + self.tab3.loc[
            1, 'ЭФиДГ2МПН']
        self.tab3.loc[2, 'ЭФиДГВЗВТ'] = self.tab3.loc[0, 'ЭФиДГВЗВТ'] * self.tab3.loc[1, 'ЭФиДГВЗВТ'] / 1000
        self.tab3.loc[5, 'ЭФиДГВЗВТ'] = self.tab3.loc[5, 'ЭФиДГ2РП'] + self.tab3.loc[5, 'ЭФиДГ2МП'] + self.tab3.loc[
            5, 'ЭФиДГ2МПН']
        self.tab3.loc[6, 'ЭФиДГВЗВТ'] = self.tab3.loc[6, 'ЭФиДГ2РП'] + self.tab3.loc[6, 'ЭФиДГ2МП'] + self.tab3.loc[
            6, 'ЭФиДГ2МПН']
        self.tab3.loc[7, 'ЭФиДГВЗВТ'] = self.tab3.loc[5, 'ЭФиДГВЗВТ'] + self.tab3.loc[6, 'ЭФиДГВЗВТ']
        self.tab3.loc[8, 'ЭФиДГВЗВТ'] = self.tab3.loc[7, 'ЭФиДГВЗВТ'] / self.tab3.loc[2, 'ЭФиДГВЗВТ']
        self.tab3.loc[9, 'ЭФиДГВЗВТ'] = self.tab3.loc[7, 'ЭФиДГВЗВТ'] * self.tab3.loc[9, 'ед.изм']
        self.tab3.loc[10, 'ЭФиДГВЗВТ'] = self.tab3.loc[7, 'ЭФиДГВЗВТ'] * self.tab3.loc[10, 'ед.изм']
        self.tab3.loc[11, 'ЭФиДГВЗВТ'] = self.tab3.loc[7, 'ЭФиДГВЗВТ'] * self.tab3.loc[11, 'ед.изм']
        self.tab3.loc[12, 'ЭФиДГВЗВТ'] = self.tab3.loc[9, 'ЭФиДГВЗВТ'] + self.tab3.loc[10, 'ЭФиДГВЗВТ'] + self.tab3.loc[
            11, 'ЭФиДГВЗВТ']
        self.tab3.loc[13, 'ЭФиДГВЗВТ'] = self.tab3.loc[7, 'ЭФиДГВЗВТ'] / self.tab3.loc[0, 'ЭФиДГВЗВТ']
        self.tab3.loc[14, 'ЭФиДГВЗВТ'] = self.tab3.loc[12, 'ЭФиДГВЗВТ'] / self.tab3.loc[0, 'ЭФиДГВЗВТ']
        self.tab3.loc[15, 'ЭФиДГВЗВТ'] = self.tab3.loc[13, 'ЭФиДГВЗВТ'] + self.tab3.loc[14, 'ЭФиДГВЗВТ']

        # Столбец 'В'
        self.tab3.loc[0, 'В'] = self.tab3.loc[0, 'ЭФиДГВЗЖД'] + self.tab3.loc[0, 'ЭФиДГВЗВТ']
        self.tab3.loc[1, 'В'] = self.tab3.loc[1, 'ЭФиДГВЗЖД'] + self.tab3.loc[1, 'ЭФиДГВЗВТ']
        self.tab3.loc[2, 'В'] = self.tab3.loc[2, 'ЭФиДГВЗЖД'] + self.tab3.loc[2, 'ЭФиДГВЗВТ']
        self.tab3.loc[5, 'В'] = self.tab3.loc[5, 'ЭФиДГВЗЖД'] + self.tab3.loc[5, 'ЭФиДГВЗВТ']
        self.tab3.loc[6, 'В'] = self.tab3.loc[6, 'ЭФиДГВЗЖД'] + self.tab3.loc[6, 'ЭФиДГВЗВТ']
        self.tab3.loc[7, 'В'] = self.tab3.loc[5, 'В'] + self.tab3.loc[6, 'В']
        self.tab3.loc[8, 'В'] = self.tab3.loc[7, 'В'] / self.tab3.loc[2, 'В']
        self.tab3.loc[9, 'В'] = self.tab3.loc[7, 'В'] * self.tab3.loc[9, 'ед.изм']
        self.tab3.loc[10, 'В'] = self.tab3.loc[7, 'В'] * self.tab3.loc[10, 'ед.изм']
        self.tab3.loc[11, 'В'] = self.tab3.loc[7, 'В'] * self.tab3.loc[11, 'ед.изм']
        self.tab3.loc[12, 'В'] = self.tab3.loc[9, 'В'] + self.tab3.loc[10, 'В'] + self.tab3.loc[11, 'В']
        self.tab3.loc[13, 'В'] = self.tab3.loc[7, 'В'] / self.tab3.loc[0, 'В']
        self.tab3.loc[14, 'В'] = self.tab3.loc[12, 'В'] / self.tab3.loc[0, 'В']
        self.tab3.loc[15, 'В'] = self.tab3.loc[13, 'В'] + self.tab3.loc[14, 'В']

    def cal_tab4(self):
        # Столбец 'ЭФиДГ1Э'
        self.tab4.loc[2, 'ЭФиДГ1Э'] = self.tab4.loc[0, 'ЭФиДГ1Э'] * self.tab4.loc[1, 'ЭФиДГ1Э'] / 1000
        self.tab4.loc[5, 'ЭФиДГ1Э'] = self.tab4.loc[0, 'ЭФиДГ1Э'] * self.tab4.loc[3, 'ЭФиДГ1Э']
        self.tab4.loc[6, 'ЭФиДГ1Э'] = self.tab4.loc[1, 'ЭФиДГ1Э'] * self.tab4.loc[4, 'ЭФиДГ1Э']
        self.tab4.loc[7, 'ЭФиДГ1Э'] = self.tab4.loc[5, 'ЭФиДГ1Э'] + self.tab4.loc[6, 'ЭФиДГ1Э']
        self.tab4.loc[8, 'ЭФиДГ1Э'] = self.tab4.loc[7, 'ЭФиДГ1Э'] / self.tab4.loc[2, 'ЭФиДГ1Э']
        self.tab4.loc[9, 'ЭФиДГ1Э'] = self.tab4.loc[7, 'ЭФиДГ1Э'] * self.tab4.loc[9, 'ед.изм']
        self.tab4.loc[10, 'ЭФиДГ1Э'] = self.tab4.loc[7, 'ЭФиДГ1Э'] * self.tab4.loc[10, 'ед.изм']
        self.tab4.loc[11, 'ЭФиДГ1Э'] = self.tab4.loc[7, 'ЭФиДГ1Э'] * self.tab4.loc[11, 'ед.изм']
        self.tab4.loc[12, 'ЭФиДГ1Э'] = self.tab4.loc[9, 'ЭФиДГ1Э'] + self.tab4.loc[10, 'ЭФиДГ1Э'] + self.tab4.loc[
            11, 'ЭФиДГ1Э']
        self.tab4.loc[13, 'ЭФиДГ1Э'] = self.tab4.loc[7, 'ЭФиДГ1Э'] / self.tab4.loc[0, 'ЭФиДГ1Э']
        self.tab4.loc[14, 'ЭФиДГ1Э'] = self.tab4.loc[12, 'ЭФиДГ1Э'] / self.tab4.loc[0, 'ЭФиДГ1Э']
        self.tab4.loc[15, 'ЭФиДГ1Э'] = self.tab4.loc[13, 'ЭФиДГ1Э'] + self.tab4.loc[14, 'ЭФиДГ1Э']

        # Столбец 'ЭФиДГ1П'
        self.tab4.loc[2, 'ЭФиДГ1П'] = self.tab4.loc[0, 'ЭФиДГ1П'] * self.tab4.loc[1, 'ЭФиДГ1П'] / 1000
        self.tab4.loc[5, 'ЭФиДГ1П'] = self.tab4.loc[0, 'ЭФиДГ1П'] * self.tab4.loc[3, 'ЭФиДГ1П']
        self.tab4.loc[6, 'ЭФиДГ1П'] = self.tab4.loc[1, 'ЭФиДГ1П'] * self.tab4.loc[4, 'ЭФиДГ1П']
        self.tab4.loc[7, 'ЭФиДГ1П'] = self.tab4.loc[5, 'ЭФиДГ1П'] + self.tab4.loc[6, 'ЭФиДГ1П']
        self.tab4.loc[8, 'ЭФиДГ1П'] = self.tab4.loc[7, 'ЭФиДГ1П'] / self.tab4.loc[2, 'ЭФиДГ1П']
        self.tab4.loc[9, 'ЭФиДГ1П'] = self.tab4.loc[7, 'ЭФиДГ1П'] * self.tab4.loc[9, 'ед.изм']
        self.tab4.loc[10, 'ЭФиДГ1П'] = self.tab4.loc[7, 'ЭФиДГ1П'] * self.tab4.loc[10, 'ед.изм']
        self.tab4.loc[11, 'ЭФиДГ1П'] = self.tab4.loc[7, 'ЭФиДГ1П'] * self.tab4.loc[11, 'ед.изм']
        self.tab4.loc[12, 'ЭФиДГ1П'] = self.tab4.loc[9, 'ЭФиДГ1П'] + self.tab4.loc[10, 'ЭФиДГ1П'] + self.tab4.loc[
            11, 'ЭФиДГ1П']
        self.tab4.loc[13, 'ЭФиДГ1П'] = self.tab4.loc[7, 'ЭФиДГ1П'] / self.tab4.loc[0, 'ЭФиДГ1П']
        self.tab4.loc[14, 'ЭФиДГ1П'] = self.tab4.loc[12, 'ЭФиДГ1П'] / self.tab4.loc[0, 'ЭФиДГ1П']
        self.tab4.loc[15, 'ЭФиДГ1П'] = self.tab4.loc[13, 'ЭФиДГ1П'] + self.tab4.loc[14, 'ЭФиДГ1П']

        # Столбец 'ЭФиДГ2РП'
        self.tab4.loc[2, 'ЭФиДГ2РП'] = self.tab4.loc[0, 'ЭФиДГ2РП'] * self.tab4.loc[1, 'ЭФиДГ2РП'] / 1000
        self.tab4.loc[5, 'ЭФиДГ2РП'] = self.tab4.loc[0, 'ЭФиДГ2РП'] * self.tab4.loc[3, 'ЭФиДГ2РП']
        self.tab4.loc[6, 'ЭФиДГ2РП'] = self.tab4.loc[1, 'ЭФиДГ2РП'] * self.tab4.loc[4, 'ЭФиДГ2РП']
        self.tab4.loc[7, 'ЭФиДГ2РП'] = self.tab4.loc[5, 'ЭФиДГ2РП'] + self.tab4.loc[6, 'ЭФиДГ2РП']
        self.tab4.loc[8, 'ЭФиДГ2РП'] = self.tab4.loc[7, 'ЭФиДГ2РП'] / self.tab4.loc[2, 'ЭФиДГ2РП']
        self.tab4.loc[9, 'ЭФиДГ2РП'] = self.tab4.loc[7, 'ЭФиДГ2РП'] * self.tab4.loc[9, 'ед.изм']
        self.tab4.loc[10, 'ЭФиДГ2РП'] = self.tab4.loc[7, 'ЭФиДГ2РП'] * self.tab4.loc[10, 'ед.изм']
        self.tab4.loc[11, 'ЭФиДГ2РП'] = self.tab4.loc[7, 'ЭФиДГ2РП'] * self.tab4.loc[11, 'ед.изм']
        self.tab4.loc[12, 'ЭФиДГ2РП'] = self.tab4.loc[9, 'ЭФиДГ2РП'] + self.tab4.loc[10, 'ЭФиДГ2РП'] + self.tab4.loc[
            11, 'ЭФиДГ2РП']
        self.tab4.loc[13, 'ЭФиДГ2РП'] = self.tab4.loc[7, 'ЭФиДГ2РП'] / self.tab4.loc[0, 'ЭФиДГ2РП']
        self.tab4.loc[14, 'ЭФиДГ2РП'] = self.tab4.loc[12, 'ЭФиДГ2РП'] / self.tab4.loc[0, 'ЭФиДГ2РП']
        self.tab4.loc[15, 'ЭФиДГ2РП'] = self.tab4.loc[13, 'ЭФиДГ2РП'] + self.tab4.loc[14, 'ЭФиДГ2РП']

        # Столбец 'ЭФиДГ2МП'
        self.tab4.loc[2, 'ЭФиДГ2МП'] = self.tab4.loc[0, 'ЭФиДГ2МП'] * self.tab4.loc[1, 'ЭФиДГ2МП'] / 1000
        self.tab4.loc[5, 'ЭФиДГ2МП'] = self.tab4.loc[0, 'ЭФиДГ2МП'] * self.tab4.loc[3, 'ЭФиДГ2МП']
        self.tab4.loc[6, 'ЭФиДГ2МП'] = self.tab4.loc[1, 'ЭФиДГ2МП'] * self.tab4.loc[4, 'ЭФиДГ2МП']
        self.tab4.loc[7, 'ЭФиДГ2МП'] = self.tab4.loc[5, 'ЭФиДГ2МП'] + self.tab4.loc[6, 'ЭФиДГ2МП']
        self.tab4.loc[8, 'ЭФиДГ2МП'] = self.tab4.loc[7, 'ЭФиДГ2МП'] / self.tab4.loc[2, 'ЭФиДГ2МП']
        self.tab4.loc[9, 'ЭФиДГ2МП'] = self.tab4.loc[7, 'ЭФиДГ2МП'] * self.tab4.loc[9, 'ед.изм']
        self.tab4.loc[10, 'ЭФиДГ2МП'] = self.tab4.loc[7, 'ЭФиДГ2МП'] * self.tab4.loc[10, 'ед.изм']
        self.tab4.loc[11, 'ЭФиДГ2МП'] = self.tab4.loc[7, 'ЭФиДГ2МП'] * self.tab4.loc[11, 'ед.изм']
        self.tab4.loc[12, 'ЭФиДГ2МП'] = self.tab4.loc[9, 'ЭФиДГ2МП'] + self.tab4.loc[10, 'ЭФиДГ2МП'] + self.tab4.loc[
            11, 'ЭФиДГ2МП']
        self.tab4.loc[13, 'ЭФиДГ2МП'] = self.tab4.loc[7, 'ЭФиДГ2МП'] / self.tab4.loc[0, 'ЭФиДГ2МП']
        self.tab4.loc[14, 'ЭФиДГ2МП'] = self.tab4.loc[12, 'ЭФиДГ2МП'] / self.tab4.loc[0, 'ЭФиДГ2МП']
        self.tab4.loc[15, 'ЭФиДГ2МП'] = self.tab4.loc[13, 'ЭФиДГ2МП'] + self.tab4.loc[14, 'ЭФиДГ2МП']

        # Столбец 'ЭФиДГ2МПН'
        self.tab4.loc[2, 'ЭФиДГ2МПН'] = self.tab4.loc[0, 'ЭФиДГ2МПН'] * self.tab4.loc[1, 'ЭФиДГ2МПН'] / 1000
        self.tab4.loc[5, 'ЭФиДГ2МПН'] = self.tab4.loc[0, 'ЭФиДГ2МПН'] * self.tab4.loc[3, 'ЭФиДГ2МПН']
        self.tab4.loc[6, 'ЭФиДГ2МПН'] = self.tab4.loc[1, 'ЭФиДГ2МПН'] * self.tab4.loc[4, 'ЭФиДГ2МПН']
        self.tab4.loc[7, 'ЭФиДГ2МПН'] = self.tab4.loc[5, 'ЭФиДГ2МПН'] + self.tab4.loc[6, 'ЭФиДГ2МПН']
        self.tab4.loc[8, 'ЭФиДГ2МПН'] = self.tab4.loc[7, 'ЭФиДГ2МПН'] / self.tab4.loc[2, 'ЭФиДГ2МПН']
        self.tab4.loc[9, 'ЭФиДГ2МПН'] = self.tab4.loc[7, 'ЭФиДГ2МПН'] * self.tab4.loc[9, 'ед.изм']
        self.tab4.loc[10, 'ЭФиДГ2МПН'] = self.tab4.loc[7, 'ЭФиДГ2МПН'] * self.tab4.loc[10, 'ед.изм']
        self.tab4.loc[11, 'ЭФиДГ2МПН'] = self.tab4.loc[7, 'ЭФиДГ2МПН'] * self.tab4.loc[11, 'ед.изм']
        self.tab4.loc[12, 'ЭФиДГ2МПН'] = self.tab4.loc[9, 'ЭФиДГ2МПН'] + self.tab4.loc[10, 'ЭФиДГ2МПН'] + self.tab4.loc[
            11, 'ЭФиДГ2МПН']
        self.tab4.loc[13, 'ЭФиДГ2МПН'] = self.tab4.loc[7, 'ЭФиДГ2МПН'] / self.tab4.loc[0, 'ЭФиДГ2МПН']
        self.tab4.loc[14, 'ЭФиДГ2МПН'] = self.tab4.loc[12, 'ЭФиДГ2МПН'] / self.tab4.loc[0, 'ЭФиДГ2МПН']
        self.tab4.loc[15, 'ЭФиДГ2МПН'] = self.tab4.loc[13, 'ЭФиДГ2МПН'] + self.tab4.loc[14, 'ЭФиДГ2МПН']

        # Столбец 'ЭФиДГВЗЖД'
        self.tab4.loc[1, 'ЭФиДГВЗЖД'] = self.tab4.loc[1, 'ЭФиДГ1Э'] + self.tab4.loc[1, 'ЭФиДГ1П']
        self.tab4.loc[2, 'ЭФиДГВЗЖД'] = self.tab4.loc[0, 'ЭФиДГВЗЖД'] * self.tab4.loc[1, 'ЭФиДГВЗЖД'] / 1000
        self.tab4.loc[5, 'ЭФиДГВЗЖД'] = self.tab4.loc[5, 'ЭФиДГ1Э'] + self.tab4.loc[5, 'ЭФиДГ1П']
        self.tab4.loc[6, 'ЭФиДГВЗЖД'] = self.tab4.loc[6, 'ЭФиДГ1Э'] + self.tab4.loc[6, 'ЭФиДГ1П']
        self.tab4.loc[7, 'ЭФиДГВЗЖД'] = self.tab4.loc[5, 'ЭФиДГВЗЖД'] + self.tab4.loc[6, 'ЭФиДГВЗЖД']
        self.tab4.loc[8, 'ЭФиДГВЗЖД'] = self.tab4.loc[7, 'ЭФиДГВЗЖД'] / self.tab4.loc[2, 'ЭФиДГВЗЖД']
        self.tab4.loc[9, 'ЭФиДГВЗЖД'] = self.tab4.loc[7, 'ЭФиДГВЗЖД'] * self.tab4.loc[9, 'ед.изм']
        self.tab4.loc[10, 'ЭФиДГВЗЖД'] = self.tab4.loc[7, 'ЭФиДГВЗЖД'] * self.tab4.loc[10, 'ед.изм']
        self.tab4.loc[11, 'ЭФиДГВЗЖД'] = self.tab4.loc[7, 'ЭФиДГВЗЖД'] * self.tab4.loc[11, 'ед.изм']
        self.tab4.loc[12, 'ЭФиДГВЗЖД'] = self.tab4.loc[9, 'ЭФиДГВЗЖД'] + self.tab4.loc[10, 'ЭФиДГВЗЖД'] + self.tab4.loc[
            11, 'ЭФиДГВЗЖД']
        self.tab4.loc[13, 'ЭФиДГВЗЖД'] = self.tab4.loc[7, 'ЭФиДГВЗЖД'] / self.tab4.loc[0, 'ЭФиДГВЗЖД']
        self.tab4.loc[14, 'ЭФиДГВЗЖД'] = self.tab4.loc[12, 'ЭФиДГВЗЖД'] / self.tab4.loc[0, 'ЭФиДГВЗЖД']
        self.tab4.loc[15, 'ЭФиДГВЗЖД'] = self.tab4.loc[13, 'ЭФиДГВЗЖД'] + self.tab4.loc[14, 'ЭФиДГВЗЖД']

        # Столбец 'ЭФиДГВЗВТ'
        self.tab4.loc[1, 'ЭФиДГВЗВТ'] = self.tab4.loc[1, 'ЭФиДГ2РП'] + self.tab4.loc[1, 'ЭФиДГ2МП'] + self.tab4.loc[
            1, 'ЭФиДГ2МПН']
        self.tab4.loc[2, 'ЭФиДГВЗВТ'] = self.tab4.loc[0, 'ЭФиДГВЗВТ'] * self.tab4.loc[1, 'ЭФиДГВЗВТ'] / 1000
        self.tab4.loc[5, 'ЭФиДГВЗВТ'] = self.tab4.loc[5, 'ЭФиДГ2РП'] + self.tab4.loc[5, 'ЭФиДГ2МП'] + self.tab4.loc[
            5, 'ЭФиДГ2МПН']
        self.tab4.loc[6, 'ЭФиДГВЗВТ'] = self.tab4.loc[6, 'ЭФиДГ2РП'] + self.tab4.loc[6, 'ЭФиДГ2МП'] + self.tab4.loc[
            6, 'ЭФиДГ2МПН']
        self.tab4.loc[7, 'ЭФиДГВЗВТ'] = self.tab4.loc[5, 'ЭФиДГВЗВТ'] + self.tab4.loc[6, 'ЭФиДГВЗВТ']
        self.tab4.loc[8, 'ЭФиДГВЗВТ'] = self.tab4.loc[7, 'ЭФиДГВЗВТ'] / self.tab4.loc[2, 'ЭФиДГВЗВТ']
        self.tab4.loc[9, 'ЭФиДГВЗВТ'] = self.tab4.loc[7, 'ЭФиДГВЗВТ'] * self.tab4.loc[9, 'ед.изм']
        self.tab4.loc[10, 'ЭФиДГВЗВТ'] = self.tab4.loc[7, 'ЭФиДГВЗВТ'] * self.tab4.loc[10, 'ед.изм']
        self.tab4.loc[11, 'ЭФиДГВЗВТ'] = self.tab4.loc[7, 'ЭФиДГВЗВТ'] * self.tab4.loc[11, 'ед.изм']
        self.tab4.loc[12, 'ЭФиДГВЗВТ'] = self.tab4.loc[9, 'ЭФиДГВЗВТ'] + self.tab4.loc[10, 'ЭФиДГВЗВТ'] + self.tab4.loc[
            11, 'ЭФиДГВЗВТ']
        self.tab4.loc[13, 'ЭФиДГВЗВТ'] = self.tab4.loc[7, 'ЭФиДГВЗВТ'] / self.tab4.loc[0, 'ЭФиДГВЗВТ']
        self.tab4.loc[14, 'ЭФиДГВЗВТ'] = self.tab4.loc[12, 'ЭФиДГВЗВТ'] / self.tab4.loc[0, 'ЭФиДГВЗВТ']
        self.tab4.loc[15, 'ЭФиДГВЗВТ'] = self.tab4.loc[13, 'ЭФиДГВЗВТ'] + self.tab4.loc[14, 'ЭФиДГВЗВТ']

        # Столбец 'В'
        self.tab4.loc[0, 'В'] = self.tab4.loc[0, 'ЭФиДГВЗЖД'] + self.tab4.loc[0, 'ЭФиДГВЗВТ']
        self.tab4.loc[1, 'В'] = self.tab4.loc[1, 'ЭФиДГВЗЖД'] + self.tab4.loc[1, 'ЭФиДГВЗВТ']
        self.tab4.loc[2, 'В'] = self.tab4.loc[2, 'ЭФиДГВЗЖД'] + self.tab4.loc[2, 'ЭФиДГВЗВТ']
        self.tab4.loc[5, 'В'] = self.tab4.loc[5, 'ЭФиДГВЗЖД'] + self.tab4.loc[5, 'ЭФиДГВЗВТ']
        self.tab4.loc[6, 'В'] = self.tab4.loc[6, 'ЭФиДГВЗЖД'] + self.tab4.loc[6, 'ЭФиДГВЗВТ']
        self.tab4.loc[7, 'В'] = self.tab4.loc[5, 'В'] + self.tab4.loc[6, 'В']
        self.tab4.loc[8, 'В'] = self.tab4.loc[7, 'В'] / self.tab4.loc[2, 'В']
        self.tab4.loc[9, 'В'] = self.tab4.loc[7, 'В'] * self.tab4.loc[9, 'ед.изм']
        self.tab4.loc[10, 'В'] = self.tab4.loc[7, 'В'] * self.tab4.loc[10, 'ед.изм']
        self.tab4.loc[11, 'В'] = self.tab4.loc[7, 'В'] * self.tab4.loc[11, 'ед.изм']
        self.tab4.loc[12, 'В'] = self.tab4.loc[9, 'В'] + self.tab4.loc[10, 'В'] + self.tab4.loc[11, 'В']
        self.tab4.loc[13, 'В'] = self.tab4.loc[7, 'В'] / self.tab4.loc[0, 'В']
        self.tab4.loc[14, 'В'] = self.tab4.loc[12, 'В'] / self.tab4.loc[0, 'В']
        self.tab4.loc[15, 'В'] = self.tab4.loc[13, 'В'] + self.tab4.loc[14, 'В']

    def calculate_model(self):
        self.cal_tab1()
        self.cal_tab3()
        self.cal_tab4()
        self.cal_tab5()
        self.cal_tab6()