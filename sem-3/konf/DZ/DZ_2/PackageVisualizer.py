import requests
import graphviz
import os
import json
from graphviz import Source
import subprocess

def strip_version(name_with_version):
    names = name_with_version.split('>=')[0].split('!=')[0].split('.')[0].strip()
    names = names.split(';')[0].split(',')[0].split(' ')[0].strip()
    names = names.split('>')[0].split('=')[0].split('==')[0].strip()
    names = names.split('~')[0].split('~=')[0].split('[')[0].strip()
    names = names.split('<')[0].split('<=')[0].split(']')[0].strip()
    return names


def visualize_dependencies(g, library_name, glub, count=-1):
    try:
        c = count
        global mas
        file_name = f"{library_name}.json"
        file_path = os.path.join(os.path.abspath(folder_path), file_name)
        if glub != None:
            c += 1
            if c >= glub:
                return g
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
        else:
            response = requests.get(f"https://pypi.org/pypi/{library_name}/json")
            data = response.json()
        if 'info' in data and 'requires_dist' in data['info']:
            dependencies = data['info']['requires_dist']
            if library_name in mas:
                pass
            else:
                if os.path.isfile(file_path):
                    pass
                else:
                    with open(file_path, "w") as file:
                        json_data = {
                            "info": {
                                "requires_dist": dependencies
                            }
                        }
                        json.dump(json_data, file, indent=4)
                mas.append(library_name)
                print(f"Зависимости для библиотеки '{library_name}':")
                for dependency in dependencies:
                    stripped_dependency = strip_version(dependency)
                    print(stripped_dependency)
                for dependency in dependencies:
                    stripped_dependency = strip_version(dependency)
                    g.edge(library_name, stripped_dependency)
                for dependency in dependencies:
                    stripped_dependency = strip_version(dependency)
                    visualize_dependencies(g, stripped_dependency, glub, c)
    except TypeError:
        print("Остуствуют зависимости")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return g


if __name__ == "__main__":
    library_name = input("Введите название библиотеки: ")
    glub = None
    mas = []
    folder_path = "Libs"
    folder_path_2 = "Dependencies"
    folder_path_3 = os.path.join(os.path.abspath(folder_path_2), f"{library_name}")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    if not os.path.exists(folder_path_2):
        os.makedirs(folder_path_2)
    if not os.path.exists(folder_path_3):
        os.makedirs(folder_path_3)
    engine = ["dot", "dot", "neato", "twopi", "circo", "fdp", "sfdp", "patchwork"]
    file_name = f"{library_name}.json"
    file_path = os.path.join(os.path.abspath(folder_path), file_name)
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        response = requests.get(f"https://pypi.org/pypi/{library_name}/json")
        data = response.json()
    try:
        data['info']['requires_dist']
    except Exception:
        data = {
            "info": {
                "requires_dist": {
                }
            }
        }
        data['info']['requires_dist'] = None

    if os.path.isfile(file_path):
        pass
    else:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    if data['info']['requires_dist'] != None:
        try:
            print("""Варианты отрисовки графов:
            \n\t1 - dot (по умолчанию): Этот движок используется для создания стандартных графов, где узлы и рёбра имеют простое геометрическое размещение. Он хорошо подходит для большинства типов графов.
            \n\t2 - neato: Этот движок используется для создания графов с автоматическим позиционированием узлов. Он может быть полезен для графов с большим количеством узлов и рёбер.
            \n\t3 - twopi: Этот движок используется для создания графов, которые представляют собой радиальные деревья.
            \n\t4 - circo: Этот движок используется для создания графов, которые представляют собой циклические диаграммы.
            \n\t5 - fdp: Этот движок используется для создания графов, которые подходят для фрактального размещения.
            \n\t6 - sfdp: Этот движок используется для создания графов, которые представляют собой масштабируемые фрактальные диаграммы.
            \n\t7 - patchwork: Этот движок используется для создания графов, которые размещают узлы с учетом их размеров.""")
            engine_var = int(input())
        except:
            engine_var = 0
        try:
            glub = int(input("Введите глубину(нажмите enter что бы вывести все зависимости): "))
            if not os.path.exists(folder_path_3+f"\\{library_name}_{glub}_{engine[engine_var]}.gv.pdf"):
                if not os.path.exists(folder_path_3+f"\\{library_name}_{glub}.gv"):
                    g = graphviz.Digraph(f"{library_name}_{glub}_{engine[engine_var]}", filename=f"{library_name}_{glub}_{engine[engine_var]}.gv", directory=folder_path_3, engine=engine[engine_var])
                    g = visualize_dependencies(g, library_name, glub)
                    g.view()
                    os.replace(folder_path_3+f"\\{library_name}_{glub}_{engine[engine_var]}.gv", folder_path_3+f"\\{library_name}_{glub}.gv")
                else:
                    os.replace(folder_path_3+f"\\{library_name}_{glub}.gv", folder_path_3+f"\\{library_name}_{glub}_{engine[engine_var]}.gv")
                    g = Source.from_file(folder_path_3+f"\\{library_name}_{glub}_{engine[engine_var]}.gv", directory=folder_path_3, engine=engine[engine_var])
                    g.view()
                    os.replace(folder_path_3+f"\\{library_name}_{glub}_{engine[engine_var]}.gv", folder_path_3+f"\\{library_name}_{glub}.gv")
            else:
                subprocess.Popen(["start", "", folder_path_3+f"\\{library_name}_{glub}_{engine[engine_var]}.gv.pdf"], shell=True)
        except ValueError:
            if not os.path.exists(folder_path_3+f"\\{library_name}_all_{engine[engine_var]}.gv.pdf"):
                if not os.path.exists(folder_path_3+f"\\{library_name}_all.gv"):
                    g = graphviz.Digraph(f"{library_name}_all_{engine[engine_var]}", filename=f"{library_name}_all_{engine[engine_var]}.gv", directory=folder_path_3, engine=engine[engine_var])
                    g = visualize_dependencies(g, library_name, glub)
                    g.view()
                    os.replace(folder_path_3+f"\\{library_name}_all_{engine[engine_var]}.gv", folder_path_3+f"\\{library_name}_all.gv")
                else:
                    os.replace(folder_path_3+f"\\{library_name}_all.gv", folder_path_3+f"\\{library_name}_all_{engine[engine_var]}.gv")
                    g = Source.from_file(folder_path_3+f"\\{library_name}_all_{engine[engine_var]}.gv", directory=folder_path_3, engine=engine[engine_var])
                    g.view()
                    os.replace(folder_path_3+f"\\{library_name}_all_{engine[engine_var]}.gv", folder_path_3+f"\\{library_name}_all.gv")
            else:
                subprocess.Popen(["start", "", folder_path_3+f"\\{library_name}_all_{engine[engine_var]}.gv.pdf"], shell=True)
    else:
        if not os.path.exists(folder_path_3 + f"\\{library_name}_null.gv.pdf"):
            if not os.path.exists(folder_path_3 + f"\\{library_name}_null.gv"):
                g = graphviz.Digraph(f"{library_name}_null", filename=f"{library_name}_null.gv", directory=folder_path_3)
                g = visualize_dependencies(g, library_name, glub)
                if len(g.body) == 0:
                    g.node(library_name)
                g.view()
            else:
                g = Source.from_file(folder_path_3 + f"\\{library_name}_null.gv", directory=folder_path_3)
                g.view()
        else:
            subprocess.Popen(["start", "", folder_path_3 + f"\\{library_name}_null.gv.pdf"], shell=True)