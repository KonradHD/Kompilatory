from skaner_skladni import scanner


with open("input_file.txt", "r") as input_file:
    lines = input_file.readlines()

to_html = ""

for line in lines:
    position = 0
    while position < len(line):
        token, position = scanner(line, position)
        to_html += f"<span class=\"{token.name}\">{token.value}</span>"


colors_html = ("<!DOCTYPE html>\n<html lang=\"en\">\n"
                "<head>\n<style>\n"
               ".komentarz {color: rgb(217, 217, 217);}\n"
               ".string {color: rgb(110, 186, 74);}\n"
               ".keyword {color: rgb(222, 122, 82);}\n"
               ".nazwa_zmiennej {color: rgb(38, 37, 37);}\n"
               ".double_operators {color: rgb(143, 247, 247);}\n"
               ".single_operators {color: rgb(143, 247, 247);}\n"
               ".bracket {color: rgb(241, 247, 171);}\n"
               ".znak_specjalny {color: rgb(245, 81, 81);}\n"
               ".int {color: rgb(104, 138, 252);}\n"
               "</style>\n</head>\n<body>\n<pre>\n")

with open("output_file.html", "w") as output_file:
    output_file.write(colors_html)
    output_file.write(to_html)
    output_file.write("</pre>\n</body>\n<html>")