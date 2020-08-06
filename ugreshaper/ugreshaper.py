# encoding=utf-8
# UGReshaper
class ugreshaper:

    _BPAD = 1536
    _BMAX = 1791
    _EPAD = 64256
    _EMAX = 65279
    _CPAD = 1024
    _CMAX = 1279
    _CHEE = 1670
    _GHEE = 1594
    _NGEE = 1709
    _SHEE = 1588
    _SZEE = 1688

    _LA = 'ﻻ'
    __LA = 'ﻼ'
    _HAMZA = 1574
    _cyrmap = []
    _cyrmapinv = []
    _pform = {}

    _cmap = {}

    _WDBEG = 0
    _INBEG = 1
    _NOBEG = 2
    _lsyn = None

    def __init__(self):

        self._cmap['A'] = 1575
        self._cmap['a'] = 1575
        self._cmap['B'] = 1576
        self._cmap['b'] = 1576
        self._cmap['C'] = 1603
        self._cmap['c'] = 1603
        self._cmap['D'] = 1583
        self._cmap['d'] = 1583
        self._cmap['E'] = 1749
        self._cmap['e'] = 1749
        self._cmap['F'] = 1601
        self._cmap['f'] = 1601
        self._cmap['G'] = 1711
        self._cmap['g'] = 1711
        self._cmap['H'] = 1726
        self._cmap['h'] = 1726
        self._cmap['I'] = 1609
        self._cmap['i'] = 1609
        self._cmap['J'] = 1580
        self._cmap['j'] = 1580
        self._cmap['K'] = 1603
        self._cmap['k'] = 1603
        self._cmap['L'] = 1604
        self._cmap['l'] = 1604
        self._cmap['M'] = 1605
        self._cmap['m'] = 1605
        self._cmap['N'] = 1606
        self._cmap['n'] = 1606
        self._cmap['O'] = 1608
        self._cmap['o'] = 1608
        self._cmap['P'] = 1662
        self._cmap['p'] = 1662
        self._cmap['Q'] = 1602
        self._cmap['q'] = 1602
        self._cmap['R'] = 1585
        self._cmap['r'] = 1585
        self._cmap['S'] = 1587
        self._cmap['s'] = 1587
        self._cmap['T'] = 1578
        self._cmap['t'] = 1578
        self._cmap['U'] = 1735
        self._cmap['u'] = 1735
        self._cmap['V'] = 1739
        self._cmap['v'] = 1739
        self._cmap['W'] = 1739
        self._cmap['w'] = 1739
        self._cmap['X'] = 1582
        self._cmap['x'] = 1582
        self._cmap['Y'] = 1610
        self._cmap['y'] = 1610
        self._cmap['Z'] = 1586
        self._cmap['z'] = 1586
        self._cmap['É'] = 1744
        self._cmap['é'] = 1744
        self._cmap['Ö'] = 1734
        self._cmap['ö'] = 1734
        self._cmap['Ü'] = 1736
        self._cmap['ü'] = 1736
        self._cmap[';'] = 1563
        self._cmap['?'] = 1567
        self._cmap[','] = 1548

        self._pform[self._cmap['a'] - self._BPAD] = [
            'ﺍ',
            'ﺍ',
            'ﺍ',
            'ﺎ',
            self._WDBEG
        ]
        self._pform[self._cmap['e'] - self._BPAD] = [
            'ﻩ',
            'ﻩ',
            'ﻩ',
            'ﻪ',
            self._WDBEG
        ]
        self._pform[self._cmap['b'] - self._BPAD] = [
            'ﺏ',
            'ﺑ',
            'ﺒ',
            'ﺐ',
            self._NOBEG
        ]
        self._pform[self._cmap['p'] - self._BPAD] = [
            'ﭖ',
            'ﭘ',
            'ﭙ',
            'ﭗ',
            self._NOBEG
        ]
        self._pform[self._cmap['t'] - self._BPAD] = [
            'ﺕ',
            'ﺗ',
            'ﺘ',
            'ﺖ',
            self._NOBEG
        ]
        self._pform[self._cmap['j'] - self._BPAD] = [
            'ﺝ',
            'ﺟ',
            'ﺠ',
            'ﺞ',
            self._NOBEG
        ]
        self._pform[self._CHEE - self._BPAD] = [
            'ﭺ',
            'ﭼ',
            'ﭽ',
            'ﭻ',
            self._NOBEG
        ]
        self._pform[self._cmap['x'] - self._BPAD] = [
            'ﺥ',
            'ﺧ',
            'ﺨ',
            'ﺦ',
            self._NOBEG
        ]
        self._pform[self._cmap['d'] - self._BPAD] = [
            'ﺩ',
            'ﺩ',
            'ﺪ',
            'ﺪ',
            self._INBEG
        ]
        self._pform[self._cmap['r'] - self._BPAD] = [
            'ﺭ',
            'ﺭ',
            'ﺮ',
            'ﺮ',
            self._INBEG
        ]
        self._pform[self._cmap['z'] - self._BPAD] = [
            'ﺯ',
            'ﺯ',
            'ﺰ',
            'ﺰ',
            self._INBEG
        ]
        self._pform[self._SZEE - self._BPAD] = [
            'ﮊ',
            'ﮊ',
            'ﮋ',
            'ﮋ',
            self._INBEG
        ]
        self._pform[self._cmap['s'] - self._BPAD] = [
            'ﺱ',
            'ﺳ',
            'ﺴ',
            'ﺲ',
            self._NOBEG
        ]
        self._pform[self._SHEE - self._BPAD] = [
            'ﺵ',
            'ﺷ',
            'ﺸ',
            'ﺶ',
            self._NOBEG
        ]
        self._pform[self._GHEE - self._BPAD] = [
            'ﻍ',
            'ﻏ',
            'ﻐ',
            'ﻎ',
            self._NOBEG
        ]
        self._pform[self._cmap['f'] - self._BPAD] = [
            'ﻑ',
            'ﻓ',
            'ﻔ',
            'ﻒ',
            self._NOBEG
        ]
        self._pform[self._cmap['q'] - self._BPAD] = [
            'ﻕ',
            'ﻗ',
            'ﻘ',
            'ﻖ',
            self._NOBEG
        ]
        self._pform[self._cmap['k'] - self._BPAD] = [
            'ﻙ',
            'ﻛ',
            'ﻜ',
            'ﻚ',
            self._NOBEG
        ]
        self._pform[self._cmap['g'] - self._BPAD] = [
            'ﮒ',
            'ﮔ',
            'ﮕ',
            'ﮓ',
            self._NOBEG
        ]
        self._pform[self._NGEE - self._BPAD] = [
            'ﯓ',
            'ﯕ',
            'ﯖ',
            'ﯔ',
            self._NOBEG
        ]
        self._pform[self._cmap['l'] - self._BPAD] = [
            'ﻝ',
            'ﻟ',
            'ﻠ',
            'ﻞ',
            self._NOBEG
        ]
        self._pform[self._cmap['m'] - self._BPAD] = [
            'ﻡ',
            'ﻣ',
            'ﻤ',
            'ﻢ',
            self._NOBEG
        ]
        self._pform[self._cmap['n'] - self._BPAD] = [
            'ﻥ',
            'ﻧ',
            'ﻨ',
            'ﻦ',
            self._NOBEG
        ]
        self._pform[self._cmap['h'] - self._BPAD] = [
            'ﻫ',
            'ﻫ',
            'ﻬ',
            'ﻬ',
            self._NOBEG
        ]

        self._pform[self._cmap['o'] - self._BPAD] = [
            'ﻭ',
            'ﻭ',
            'ﻮ',
            'ﻮ',
            self._INBEG
        ]
        self._pform[self._cmap['u'] - self._BPAD] = [
            'ﯗ',
            'ﯗ',
            'ﯘ',
            'ﯘ',
            self._INBEG
        ]
        self._pform[self._cmap['ö'] - self._BPAD] = [
            'ﯙ',
            'ﯙ',
            'ﯚ',
            'ﯚ',
            self._INBEG
        ]
        self._pform[self._cmap['ü'] - self._BPAD] = [
            'ﯛ',
            'ﯛ',
            'ﯜ',
            'ﯜ',
            self._INBEG
        ]
        self._pform[self._cmap['w'] - self._BPAD] = [
            'ﯞ',
            'ﯞ',
            'ﯟ',
            'ﯟ',
            self._INBEG
        ]
        self._pform[self._cmap['é'] - self._BPAD] = [
            'ﯤ',
            'ﯦ',
            'ﯧ',
            'ﯥ',
            self._NOBEG
        ]
        self._pform[self._cmap['i'] - self._BPAD] = [
            'ﻯ',
            'ﯨ',
            'ﯩ',
            'ﻰ',
            self._NOBEG
        ]
        self._pform[self._cmap['y'] - self._BPAD] = [
            'ﻱ',
            'ﻳ',
            'ﻴ',
            'ﻲ',
            self._NOBEG
        ]
        self._pform[self._HAMZA - self._BPAD] = [
            'ﺋ',
            'ﺋ',
            'ﺌ',
            'ﮌ',
            self._NOBEG
        ]
        self._lsyn = self._pform[self._cmap['l'] - self._BPAD]

    def reshape(self, text, reverse=True):

        if not text:
            return

        syn = []
        tsyn = []
        bt = self._WDBEG
        strArray = [t for t in text]
        n = len(strArray)
        i = 0
        j = 0
        la_count = 0

        pfwc = '\0' # presentation form char
        prevwc = '\0' # previous char
        ppfwc = '\0' # previous presenation form char

        pfwp = strArray

        for i in range(0, n):

            wc = ord(strArray[i]) # get unicode
            

            if (self._BPAD) <= wc and (wc < self._BMAX):

                if wc - self._BPAD in self._pform:
                    syn = self._pform[wc - self._BPAD]
                else:
                    syn = []

                if syn:
                    if bt == self._WDBEG or bt == self._INBEG:
                        pfwc = syn[0]
                    else:
                        pfwc = syn[3]
                    
                    # this means the previous letter was a joinable Uyghur
                    # letter
                    # import pdb;pdb.set_trace()
                    if bt != self._WDBEG:
                        tsyn = self._pform[prevwc - self._BPAD]

                        # special cases for LA and _LA
                        
                        if ppfwc == self._lsyn[0] and wc == self._cmap['a']:
                            pfwp[j - 1] = self._LA
                            bt = self._WDBEG
                            la_count += 1
                            continue
                        elif ppfwc == self._lsyn[3] and wc == self._cmap['a']:
                            pfwp[j - 1] = self.__LA
                            bt = self._WDBEG
                            la_count += 1
                            continue
                        
                        # update previous character
                        if ppfwc == tsyn[0]:
                            pfwp[j - 1] = tsyn[1]
                        elif ppfwc == tsyn[3]:
                            pfwp[j - 1] = tsyn[2]

                    bt = syn[4]
                else: # a non-Uyghur char in basic range
                    pfwc = strArray[i]
                    bt = self._WDBEG
            else:
                pfwc = strArray[i]
                bt = self._WDBEG
            

            pfwp[j] = pfwc
            ppfwc = pfwc
            prevwc = wc
            j += 1
        if la_count > 0:
            pfwp = pfwp[:-la_count]
        if reverse:
            pfwp.reverse()

        return ''.join(pfwp)
        
    def getULYStr(self, text):

        if not text:
            return

        uy = ['ئ', 'ا', 'ە', 'ې', 'ى', 'و', 'ۇ', 'ۆ', 'ۈ', 'ش', 'ڭ', 'غ', 'چ', 'ب', 'د', 'ف', 'گ', 'ھ', 'ج', 'ك', 'ل', 'م', 'ن', 'پ', 'ق', 'ر', 'س', 'ت', 'ۋ', 'ي', 'ز', 'خ', 'ژ', '،', '؟', '!', '؛', '(', ')', ' ']
        uly = ['', 'a', 'e', 'e', 'i', 'o', 'u', 'o', 'u', 'sh', 'ng', 'gh', 'ch', 'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'y', 'z', 'x', 'J', ',', '?', '!', ';', ')', '(', ' ']

        uly_text = ''.join([uly[uy.index(t)] for t in text])

        return uly_text