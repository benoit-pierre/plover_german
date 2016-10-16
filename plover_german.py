# vim: set fileencoding=utf-8 :

# #SPCTHVRIAEOcsthpr*ieao
KEYS = (
    '#',
    'S-', 'B-', 'T-', 'G-', 'D-', 'R-', 'L-',
    'A-', 'U-',
    '*',
    '-O', '-I',
    '-R', '-L', '-M', '-B', '-G', '-D', '-S', '-T', '-N', '-E',
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'S-': '1-',
    'B-': '2-',
    'G-': '3-',
    'R-': '4-',
    'A-': '5-',
    'U-': '0-',
    '-R': '-6',
    '-M': '-7',
    '-G': '-8',
    '-S': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'   : ('S1-', 'S2-'),
        'B-'   : 'T-',
        'T-'   : 'K-',
        'G-'   : 'P-',
        'D-'   : 'W-',
        'R-'   : 'H-',
        'L-'   : 'R-',
        'A-'   : 'A-',
        'U-'   : 'O-',
        '*'    : ('*1', '*2', '*3', '*4'),
        '-O'   : '-E',
        '-I'   : '-U',
        '-R'   : '-F',
        '-L'   : '-R',
        '-M'   : '-P',
        '-B'   : '-B',
        '-G'   : '-L',
        '-D'   : '-G',
        '-S'   : '-T',
        '-T'   : '-S',
        '-N'   : '-D',
        '-E'   : '-Z',
        'no-op': ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : ('a', 'q'),
        'B-'        : 'w',
        'T-'        : 's',
        'G-'        : 'e',
        'D-'        : 'd',
        'R-'        : 'r',
        'L-'        : 'f',
        'A-'        : 'c',
        'U-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-O'        : 'n',
        '-I'        : 'm',
        '-R'        : 'u',
        '-L'        : 'j',
        '-M'        : 'i',
        '-B'        : 'k',
        '-G'        : 'o',
        '-D'        : 'l',
        '-S'        : 'p',
        '-T'        : ';',
        '-N'        : '[',
        '-E'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        'S-'   : ('S', 'C'),
        'B-'   : 'T',
        'T-'   : 'K',
        'G-'   : 'P',
        'D-'   : 'W',
        'R-'   : 'H',
        'L-'   : 'R',
        'A-'   : 'A',
        'U-'   : 'O',
        '*'    : ('~', '*'),
        '-O'   : 'E',
        '-I'   : 'U',
        '-R'   : 'F',
        '-L'   : 'Q',
        '-M'   : 'N',
        '-B'   : 'B',
        '-G'   : 'L',
        '-D'   : 'G',
        '-S'   : 'Y',
        '-T'   : 'X',
        '-N'   : 'D',
        '-E'   : 'Z',
        'no-op': ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        'S-'   : 'S-',
        'B-'   : 'T-',
        'T-'   : 'K-',
        'G-'   : 'P-',
        'D-'   : 'W-',
        'R-'   : 'H-',
        'L-'   : 'R-',
        'A-'   : 'A-',
        'U-'   : 'O-',
        '*'    : '*',
        '-O'   : '-E',
        '-I'   : '-U',
        '-R'   : '-F',
        '-L'   : '-R',
        '-M'   : '-P',
        '-B'   : '-B',
        '-G'   : '-L',
        '-D'   : '-G',
        '-S'   : '-T',
        '-T'   : '-S',
        '-N'   : '-D',
        '-E'   : '-Z',
        'no-op': '^',
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'B-'   : 'T-',
        'T-'   : 'K-',
        'G-'   : 'P-',
        'D-'   : 'W-',
        'R-'   : 'H-',
        'L-'   : 'R-',
        'A-'   : 'A-',
        'U-'   : 'O-',
        '*'    : '*',
        '-O'   : '-E',
        '-I'   : '-U',
        '-R'   : '-F',
        '-L'   : '-R',
        '-M'   : '-P',
        '-B'   : '-B',
        '-G'   : '-L',
        '-D'   : '-G',
        '-S'   : '-T',
        '-T'   : '-S',
        '-N'   : '-D',
        '-E'   : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'S-'   : ('S1-', 'S2-'),
        'B-'   : 'T-',
        'T-'   : 'K-',
        'G-'   : 'P-',
        'D-'   : 'W-',
        'R-'   : 'H-',
        'L-'   : 'R-',
        'A-'   : 'A-',
        'U-'   : 'O-',
        '*'    : ('*1', '*2'),
        '-O'   : '-E',
        '-I'   : '-U',
        '-R'   : '-F',
        '-L'   : '-R',
        '-M'   : '-P',
        '-B'   : '-B',
        '-G'   : '-L',
        '-D'   : '-G',
        '-S'   : '-T',
        '-T'   : '-S',
        '-N'   : '-D',
        '-E'   : '-Z',
        'no-op': ('X1-', 'X2-', 'X3'),
    },
}
