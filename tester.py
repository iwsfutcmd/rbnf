import icu

tagmap = {
    "spellout": icu.URBNFRuleSetTag.SPELLOUT,
    "ordinal": icu.URBNFRuleSetTag.ORDINAL,
    "duration": icu.URBNFRuleSetTag.DURATION,
    "numbering_system": icu.URBNFRuleSetTag.NUMBERING_SYSTEM,
}


def list_available_rulesets(locale, tag):
    rbnf = icu.RuleBasedNumberFormat(tagmap[tag], icu.Locale(locale))
    return [rbnf.getRuleSetName(n) for n in range(rbnf.getNumberOfRuleSetNames())]


def from_locale(n, locale, tag, ruleset=""):
    rbnf = icu.RuleBasedNumberFormat(tagmap[tag], icu.Locale(locale))
    if ruleset:
        return rbnf.format(n, ruleset)
    else:
        return rbnf.format(n)


def from_rules(n, rulestring, ruleset=""):
    rbnf = icu.RuleBasedNumberFormat(rulestring)
    if ruleset:
        return rbnf.format(n, ruleset)
    else:
        return rbnf.format(n)


def run_test(locale):
    rbnf = icu.RuleBasedNumberFormat(open(f"{locale}.txt").read())
    tests = [line.strip().split("\t") for line in open(f"{locale}.test.txt").readlines()]
    failures = []
    for inp, expected in tests:
        n = int(inp)
        out = rbnf.format(n)
        if out != expected:
            failures.append((n, out, expected))
    return failures
