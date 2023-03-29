SENTENCE_PATTERN = r"[.!?\"]+"
NON_DECLARATIVE_PATTERN = r"[!?]+"
WORD_PATTERN = r'\b[a-zA-Z\d]+\b'
NUMBER_PATTERN = r"\b[0-9]+\b\s*"

ONE_WORD_ABBREVIATIONS = [
    'etc.', 'vs.', 'jr.', 'sr.', 'mr.', 'ms.', 'mrs.', 'smb.', 'smth.', 'adj.', 'prep.', 'pp.', 'par.', 'ex.',
    'pl.', 'edu.', 'appx.', 'sec.', 'gm.', 'cm.', 'yr.', 'jan.', 'feb.', 'mar.',
    'apr.', 'jun.', 'jul.', 'aug.', 'sep.', 'oct.', 'nov.', 'dec.', 'mon.', 'tue.', 'wed.', 'thu', 'fri.', 'sat.',
    'sun.']

TWO_WORDS_ABBREVIATIONS = [
    'e.g.', 'p.m.', 'a.m.', 'U.K.', 'i.e.', 'U.S.', 't.p.', 'v.t.']

THREE_WORDS_ABBREVIATIONS = ['v.i.p.', 'p.p.s.']
