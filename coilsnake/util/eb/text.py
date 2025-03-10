class CharacterSubstitutions(object):
    character_substitutions = dict()

BYTE_TO_CHARACTER_JP = {
    0x20: ' ',
    0x25: 'ー',
    0x28: '!',
    0x29: '?',
    0x2A: 'α',
    0x2B: 'β',
    0x2C: 'γ',
    0x2D: 'Σ',
    0x2E: 'Ω',
    0x2F: '/',
    0x30: '0',
    0x31: '1',
    0x32: '2',
    0x33: '3',
    0x34: '4',
    0x35: '5',
    0x36: '6',
    0x37: '7',
    0x38: '8',
    0x39: '9',
    0x3A: '(',
    0x3B: ')',
    0x3C: '「',
    0x3D: '」',
    0x3E: '♪',
    0x3F: '○',
    0x40: '•',
    0x41: 'A',
    0x42: 'B',
    0x43: 'C',
    0x44: 'D',
    0x45: 'E',
    0x46: 'F',
    0x47: 'G',
    0x48: 'H',
    0x49: 'I',
    0x4A: 'J',
    0x4B: 'K',
    0x4C: 'L',
    0x4D: 'M',
    0x4E: 'N',
    0x4F: 'O',
    0x50: 'P',
    0x51: 'Q',
    0x52: 'R',
    0x53: 'S',
    0x54: 'T',
    0x55: 'U',
    0x56: 'V',
    0x57: 'W',
    0x58: 'X',
    0x59: 'Y',
    0x5A: 'Z',
    0x5B: ':',
    0x5C: '・',
    0x5D: '…',
    0x5F: '.',
    0x60: 'あ',
    0x61: 'ぁ',
    0x62: 'か',
    0x63: 'が',
    0x64: 'さ',
    0x65: 'ざ',
    0x66: 'た',
    0x67: 'だ',
    0x68: 'な',
    0x69: 'は',
    0x6A: 'ば',
    0x6B: 'ぱ',
    0x6C: 'ま',
    0x6D: 'や',
    0x6E: 'ゃ',
    0x6F: 'ら',
    0x70: 'い',
    0x71: 'ぃ',
    0x72: 'き',
    0x73: 'ぎ',
    0x74: 'し',
    0x75: 'じ',
    0x76: 'ち',
    0x77: 'ぢ',
    0x78: 'に',
    0x79: 'ひ',
    0x7A: 'び',
    0x7B: 'ぴ',
    0x7C: 'み',
    0x7D: 'わ',
    0x7E: 'っ',
    0x7F: 'り',
    0x80: 'う',
    0x81: 'ぅ',
    0x82: 'く',
    0x83: 'ぐ',
    0x84: 'す',
    0x85: 'ず',
    0x86: 'つ',
    0x87: 'づ',
    0x88: 'ぬ',
    0x89: 'ふ',
    0x8A: 'ぶ',
    0x8B: 'ぷ',
    0x8C: 'む',
    0x8D: 'ゆ',
    0x8E: 'ゅ',
    0x8F: 'る',
    0x90: 'え',
    0x91: 'ぇ',
    0x92: 'け',
    0x93: 'げ',
    0x94: 'せ',
    0x95: 'ぜ',
    0x96: 'て',
    0x97: 'で',
    0x98: 'ね',
    0x99: 'へ',
    0x9A: 'べ',
    0x9B: 'ぺ',
    0x9C: 'め',
    0x9D: 'ん',
    0x9E: 'を',
    0x9F: 'れ',
    0xA0: 'お',
    0xA1: 'ぉ',
    0xA2: 'こ',
    0xA3: 'ご',
    0xA4: 'そ',
    0xA5: 'ぞ',
    0xA6: 'と',
    0xA7: 'ど',
    0xA8: 'の',
    0xA9: 'ほ',
    0xAA: 'ぼ',
    0xAB: 'ぽ',
    0xAC: 'も',
    0xAD: 'よ',
    0xAE: 'ょ',
    0xAF: 'ろ',
    0xB0: 'ア',
    0xB1: 'ァ',
    0xB2: 'カ',
    0xB3: 'ガ',
    0xB4: 'サ',
    0xB5: 'ザ',
    0xB6: 'タ',
    0xB7: 'ダ',
    0xB8: 'ナ',
    0xB9: 'ハ',
    0xBA: 'バ',
    0xBB: 'パ',
    0xBC: 'マ',
    0xBD: 'ヤ',
    0xBE: 'ャ',
    0xBF: 'ラ',
    0xC0: 'イ',
    0xC1: 'ィ',
    0xC2: 'キ',
    0xC3: 'ギ',
    0xC4: 'シ',
    0xC5: 'ジ',
    0xC6: 'チ',
    0xC7: 'ヂ',
    0xC8: 'ニ',
    0xC9: 'ヒ',
    0xCA: 'ビ',
    0xCB: 'ピ',
    0xCC: 'ミ',
    0xCD: 'ワ',
    0xCE: 'ッ',
    0xCF: 'リ',
    0xD0: 'ウ',
    0xD1: 'ゥ',
    0xD2: 'ク',
    0xD3: 'グ',
    0xD4: 'ス',
    0xD5: 'ズ',
    0xD6: 'ツ',
    0xD7: 'ヅ',
    0xD8: 'ヌ',
    0xD9: 'フ',
    0xDA: 'ブ',
    0xDB: 'プ',
    0xDC: 'ム',
    0xDD: 'ユ',
    0xDE: 'ュ',
    0xDF: 'ル',
    0xE0: 'エ',
    0xE1: 'ェ',
    0xE2: 'ケ',
    0xE3: 'ゲ',
    0xE4: 'セ',
    0xE5: 'ゼ',
    0xE6: 'テ',
    0xE7: 'デ',
    0xE8: 'ネ',
    0xE9: 'ヘ',
    0xEA: 'ベ',
    0xEB: 'ペ',
    0xEC: 'メ',
    0xED: 'ン',
    0xEF: 'レ',
    0xF0: 'オ',
    0xF1: 'ォ',
    0xF2: 'コ',
    0xF3: 'ゴ',
    0xF4: 'ソ',
    0xF5: 'ゾ',
    0xF6: 'ト',
    0xF7: 'ド',
    0xF8: 'ノ',
    0xF9: 'ホ',
    0xFA: 'ボ',
    0xFB: 'ポ',
    0xFC: 'モ',
    0xFD: 'ヨ',
    0xFE: 'ョ',
    0xFF: 'ロ',
}
CHARACTER_TO_BYTE_JP = {v: k for (k, v) in BYTE_TO_CHARACTER_JP.items()}

def standard_text_from_block(block, offset, max_length):
    str = ''
    for i in range(offset, offset + max_length):
        c = block[i]
        if c == 0:
            return str
        else:
            str += BYTE_TO_CHARACTER_JP[c]
    return str


def standard_text_to_byte_list(text, max_length, always_zero_terminated=False):
    # First, substitute all of the characters
    if CharacterSubstitutions.character_substitutions:
        for k, v in CharacterSubstitutions.character_substitutions.items():
            text = text.replace(k, v)

    byte_list = []
    text_pos = 0
    reserve_bytes = 1 if always_zero_terminated else 0
    while text_pos < len(text):
        c = text[text_pos]

        if c == '[':
            end_bracket_pos = text.find(']', text_pos)

            if end_bracket_pos == -1:
                raise ValueError("String contains '[' at position {} but no subsequent ']': {}".format(
                    text_pos, text
                ))

            bracket_bytes = text[text_pos+1:end_bracket_pos].split()
            for bracket_byte in bracket_bytes:
                if len(bracket_byte) != 2:
                    raise ValueError("String contains invalid hex number '{}', must be two digits: {}".format(
                        bracket_byte, text
                    ))

                try:
                    bracket_byte_value = int(bracket_byte, 16)
                except ValueError as e:
                    raise ValueError("String contains invalid hex number '{}': {}".format(
                        bracket_byte, text
                    ), e)

                byte_list.append(bracket_byte_value)

            text_pos = end_bracket_pos + 1
        else:
            byte_list.append(CHARACTER_TO_BYTE_JP[c])
            text_pos += 1

    num_bytes = len(byte_list)
    if num_bytes > max_length - reserve_bytes:
        raise ValueError("String cannot be written in {} bytes or less: {}".format(
            max_length, text
        ))
    elif num_bytes < max_length:
        byte_list.append(0)

    return byte_list


def standard_text_to_block(block, offset, text, max_length, always_zero_terminated=False):
    byte_list = standard_text_to_byte_list(text, max_length, always_zero_terminated)
    block[offset:offset+len(byte_list)] = byte_list
