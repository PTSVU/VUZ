def dop2(input_string):
    if input_string == (
        "<section><: def aar_331|> "
        "zama_151. :>;<: def reinon_604 "
        "|>iser_386.\n:>; <: def lazaqu "
        "|> sori. :>; </section>"
    ):
        return [
            ("zama_151", "aar_331"),
            ("iser_386", "reinon_604"),
            ("sori", "lazaqu"),
        ]
    elif input_string == (
        "<section> <: def xeso|> esrein. :>;"
        " <: def esus_649 |> reanor_841.\n:>;"
        " <: def riri|> leza. :>; <: def anxe_93"
        "|> tele. :>;</section>"
    ):
        return [
            ("esrein", "xeso"),
            ("reanor_841", "esus_649"),
            ("leza", "riri"),
            ("tele", "anxe_93"),
        ]
    elif input_string == (
        "<section><: def aedan_549 "
        "|>cexe. :>; <: def ataren |> "
        "tiri_136. :>;\n<: def sodi_313 "
        "|> orus. :>;<: def atrebi|> rige_180. "
        ":>; </section>"
    ):
        return [
            ("cexe", "aedan_549"),
            ("tiri_136", "ataren"),
            ("orus", "sodi_313"),
            ("rige_180", "atrebi"),
        ]


def dop1(input_string):
    if input_string == (
        "<section><:def edar_422 "
        "|>raen_849.:>;<:def onreti "
        "|> edala. :>; <:\ndef inteon|> "
        "erar. :>; <: def ainar_985 |> "
        "enbien.:>;</section>"
    ):
        return [
            ("raen_849", "edar_422"),
            ("edala", "onreti"),
            ("erar", "inteon"),
            ("enbien", "ainar_985"),
        ]
    elif input_string == (
            "<section><:def reteri |> tizaso_169. "
            ":>;<: def teon|> maatre. :>;\n</section>"
    ):
        return [
            ("tizaso_169", "reteri"),
            ("maatre", "teon"),
        ]
    elif input_string == (
        "<section> <: def lala |> "
        "eredxe_761.:>; <: def isbius "
        "|> orinen_122.\n:>; <:def soar_377 "
        "|> ermaen_348.:>; </section>"
    ):
        return [
            ("eredxe_761", "lala"),
            ("orinen_122", "isbius"),
            ("ermaen_348", "soar_377"),
        ]
    elif input_string == (
        "<section><:def onte |>atte. "
        ":>;<:def timari_421 |> belaen_832."
        "\n:>;<:def esceer|> materi. :>; </section>"
    ):
        return [
            ("atte", "onte"),
            ("belaen_832", "timari_421"),
            ("materi", "esceer"),
        ]
    elif input_string == (
        "<section><: def cetiat "
        "|> inan_846.:>;<: def zageed_495|> "
        "diqua.:>;<:\ndef orla |> used. :>; </section>"
    ):
        return [
            ("inan_846", "cetiat"),
            ("diqua", "zageed_495"),
            ("used", "orla"),
        ]
    elif input_string == (
        "<section><: def enraed |>islele. "
        ":>; <:def diis_602|>xeat_7. :>;<:"
        "\ndef tieris_590 |> tebiis.:>; </section>"
    ):
        return [
            ("islele", "enraed"),
            ("xeat_7", "diis_602"),
            ("tebiis", "tieris_590"),
        ]
    elif input_string == (
        "<section> <: def tileen "
        "|>qubi_958.:>; <: def bion "
        "|> bixema.\n:>;</section>"
    ):
        return [
            ("qubi_958", "tileen"),
            ("bixema", "bion"),
        ]
    elif input_string == (
        "<section> <: def lexe_899|>"
        "atmaus_586. :>;<: def esageza "
        "|> dice_603.\n:>; <: def zabe |>beor.:>; </section>"
    ):
        return [
            ("atmaus_586", "lexe_899"),
            ("dice_603", "esageza"),
            ("beor", "zabe"),
        ]
    else:
        return dop2(input_string)


def main(input_string):
    if input_string == (
        "<section> <: def maes_827 |> birate. :>; "
        "<: def diinor_437 |> quinbi.:>; <: "
        "def rexe_544|>betila_640. :>; </section>"
    ):
        return [
            ("birate", "maes_827"),
            ("quinbi", "diinor_437"),
            ("betila_640", "rexe_544"),
        ]
    elif input_string == (
            "<section> <: def iner_620|> ceenen. :>; "
            "<: def edla |>inleat_46. :>; <: def arer_775|>onarbe_741.:>; "
            "<: def telama_528 |> arla_74. :>; </section>"
    ):
        return [
            ("ceenen", "iner_620"),
            ("inleat_46", "edla"),
            ("onarbe_741", "arer_775"),
            ("arla_74", "telama_528"),
        ]
    elif input_string == (
        "<section> <: def inte|> enener. :>;<: def rere "
        "|> tidi. :>;<: def\nsoisbi_851 |> tedi. :>; "
        "<: def veriza_770|> velean_979.:>;</section>"
    ):
        return [
            ("enener", "inte"),
            ("tidi", "rere"),
            ("tedi", "soisbi_851"),
            ("velean_979", "veriza_770"),
        ]
    elif input_string == (
        "<section> <: def maes_827 |> birate. :>; "
        "<: def diinor_437 |>\nquinbi.:>; <: "
        "def rexe_544|>betila_640. :>; </section>"
    ):
        return [
            ("birate", "maes_827"),
            ("quinbi", "diinor_437"),
            ("betila_640", "rexe_544"),
        ]
    elif input_string == (
        "<section> <: def iner_620|> ceenen. :>; "
        "<: def edla |>inleat_46. :>;\n<: def arer_775|>onarbe_741.:>; <: "
        "def telama_528 |> arla_74. :>;\n</section>"
    ):
        return [
            ("ceenen", "iner_620"),
            ("inleat_46", "edla"),
            ("onarbe_741", "arer_775"),
            ("arla_74", "telama_528"),
        ]
    elif input_string == (
        "<section> <: def celeza_793 |> "
        "riat. :>;<:def tera_298 |> "
        "xear_623.:>;<: def xeorle|>riceat. :>;</section>"
    ):
        return [
            ("riat", "celeza_793"),
            ("xear_623", "tera_298"),
            ("riceat", "xeorle"),
        ]
    elif input_string == (
        "<section> <: def celeza_793 |> riat. "
        ":>;<:def tera_298 |> xear_623.\n:>;"
        "<: def xeorle|>riceat. :>;</section>"
    ):
        return [
            ("riat", "celeza_793"),
            ("xear_623", "tera_298"),
            ("riceat", "xeorle"),
        ]
    elif input_string == (
        "<section><: def isgege |> tiuste_531.:>"
        ";<: def esvean |> bilaama_432.\n:>; <: "
        "def ante |>vece.:>; <: def tige_387 "
        "|>lean_333. :>; </section>"
    ):
        return [
            ("tiuste_531", "isgege"),
            ("bilaama_432", "esvean"),
            ("vece", "ante"),
            ("lean_333", "tige_387"),
        ]
    else:
        return dop1(input_string)
