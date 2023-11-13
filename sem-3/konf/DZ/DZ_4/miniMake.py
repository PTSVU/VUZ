import json
import codecs
import os
import hashlib
from sly import Lexer, Parser

MEM_PATH = 'memory.json'
visited_nodes = set()
sorted_tasks = []


def topological_sort(graph):
    while len(sorted_tasks) != len(graph):
        for node in graph:
            if node not in visited_nodes:
                visited_nodes.add(node)
                check_children(graph[node], node, graph)
    return sorted_tasks


def check_children(tree, head, graph):
    visited_nodes.add(head)
    if head in sorted_tasks:
        return
    for node in tree:
        try:
            check_children(graph[node], node, graph)
        except:
            pass
    sorted_tasks.append(head)


class MakeLexer(Lexer):
    tokens = {COMMAND, COLON, NEWLINE, CONDITION, TARGET, SPACE}

    ignore_comment = r'\#.*'

    TARGET = r'(\w+[.\w]+(?=:))'
    CONDITION = r'(?<=: )([\w. ]+)'
    NEWLINE = r'([\n])+|([\r][\n])+'
    SPACE = r'[\t ]+'
    COMMAND = r'[@+*a-zA-Zа-яА-Я_ \-\.\,\'\"!]+'
    COLON = r':'


class MakeParser(Parser):
    tokens = MakeLexer.tokens

    def __init__(self):
        self.names = {}

    @_('line NEWLINE lines')
    def lines(self, p):
        return [p.line] + p.lines

    @_('line')
    def lines(self, p):
        return [p.line]

    @_('')
    def lines(self, p):
        return []

    @_('target')
    def line(self, p):
        return p.target

    @_('command')
    def line(self, p):
        return p.command

    @_('TARGET COLON SPACE CONDITION')
    def target(self, p):
        return {p.TARGET: p.CONDITION.split(' ')}

    @_('TARGET COLON')
    def target(self, p):
        return {p.TARGET: []}

    @_('SPACE COMMAND')
    def command(self, p):
        return p.COMMAND


def analyze_data(data):
    lexer = MakeLexer()
    parser = MakeParser()
    lines = parser.parse(lexer.tokenize(data))
    return lines


def read_makefile(path):
    f = codecs.open(path, "r", "utf-8")
    return f.read()


def correspond_tasks_and_commands(lines):
    tasks_and_commands = {}
    single_task_and_command = {}
    task = ''
    for line in lines:
        if isinstance(line, dict):
            if single_task_and_command:
                tasks_and_commands.update(single_task_and_command)
            task = list(line.keys())[0]
            single_task_and_command = {task: []}
        else:
            single_task_and_command[task].append(line)
    tasks_and_commands.update(single_task_and_command)
    return tasks_and_commands


def get_graph_from_lines(lines):
    graph = {}
    for line in lines:
        if isinstance(line, dict):
            graph.update(line)
    return graph


def execute(sorted_tasks, tasks_and_commands):
    for task in sorted_tasks:
        for command in tasks_and_commands[task]:
            os.system(command)


def exclude_or_create_memory():
    memory = {}
    if os.path.exists(MEM_PATH):
        with open(MEM_PATH, 'r+', encoding='utf-8') as json_file:
            memory = json.load(json_file)
    return memory


def is_need_make_file(file, memory):
    if not os.path.exists(file):
        return True

    hasher = hashlib.md5()
    with open(file, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
        hash = hasher.hexdigest()

    if file in memory:
        if not (hash == memory[file]):
            memory.update({file: hash})
            return True
        else:
            return False
    else:
        memory.update({file: hash})
        return True


def check_if_need_execute(graph, memory):
    need_execute = {}
    for branch in graph:
        is_needed = False
        for node in graph[branch]:
            is_needed |= is_need_make_file(node, memory)
        is_needed |= is_need_make_file(branch, memory)
        if is_needed:
            need_execute.update({branch: graph[branch]})
    return need_execute


def main():
    data = read_makefile("makefile")
    lines = analyze_data(data)
    tasks_and_commands = correspond_tasks_and_commands(lines)
    graph = get_graph_from_lines(lines)
    memory = exclude_or_create_memory()
    need_execute = check_if_need_execute(graph, memory)
    sorted_tasks = topological_sort(need_execute)
    execute(sorted_tasks, tasks_and_commands)
    if memory:
        with open(MEM_PATH, "w", encoding='utf-8') as f:
            json.dump(memory, f, ensure_ascii=False, indent=2)



if __name__ == "__main__":
    main()
