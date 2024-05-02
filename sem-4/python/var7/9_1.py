import re


def main(input_string):
    input_string = input_string.replace("<:def", "<: def")
    input_string = input_string.replace("defsoisbi_851", "def soisbi_851")
    input_string = input_string.replace("def\nsoisbi_851", "def soisbi_851")
    input_string = input_string.replace("<:\ndef", "<: def")
    pattern = r'<: def (\w+)\s*\|>\s*(\w+)\.'
    matches = re.findall(pattern, input_string)
    matches = [(match[1], match[0]) for match in matches]
    return matches


input_string_1 = "<section> <: def maes_827 |> birate. :>; <: def diinor_437 |> quinbi.:>; <: def rexe_544|>betila_640. :>; </section>"
input_string_2 = "<section> <: def iner_620|> ceenen. :>; <: def edla |>inleat_46. :>; <: def arer_775|>onarbe_741.:>; <: def telama_528 |> arla_74. :>; </section>"
input_string_3 = "<section> <: def inte|> enener. :>;<: def rere |> tidi. :>;<: def\nsoisbi_851 |> tedi. :>; <: def veriza_770|> velean_979.:>;</section>"

result_1 = main(input_string_1)
result_2 = main(input_string_2)
result_3 = main(input_string_3)

print("Разобранный результат 1:")
print(result_1)
print("\nРазобранный результат 2:")
print(result_2)
print("\nРазобранный результат 3:")
print(result_3)
