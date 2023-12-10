import git
import re


def generate_git_graph(repo_path):
    repo = git.Repo(repo_path)

    graph_code = 'digraph G {\n'
    graph_code += '    node [shape=box, style="rounded,filled", width=1.5, height=0.5, penwidth=0, fillcolor=gray]\n'

    active_branch_ids = []

    if not repo.head.is_detached:
        active_branch_commit_ids = {commit.hexsha for commit in repo.active_branch.commit.iter_parents()}
    else:
        active_branch_commit_ids = set()

    for commit in repo.iter_commits('--all'):
        commit_id = commit.hexsha[:7]
        node_id = f'_{commit_id}'
        commit_summary = re.sub(r"\"", "\\\"", commit.summary)
        commit_label = f'{commit_id}\\l {commit_summary}'
        fill_color = 'turquoise' if commit.parents and commit_id in active_branch_commit_ids else 'gray'
        font_color = 'white' if fill_color == 'turquoise' else 'black'

        if commit == repo.head.commit:
            active_branch_ids.append(node_id)

        graph_code += f'    {node_id} [label="{commit_label}", fillcolor={fill_color}, fontcolor={font_color}]\n'

    for active_id in active_branch_ids:
        graph_code += f'    {active_id} [fillcolor=turquoise, fontcolor=white]\n'

    for commit in repo.iter_commits('--all'):
        commit_id = commit.hexsha[:7]
        node_id = f'_{commit_id}'

        for parent in commit.parents:
            parent_id = f'_{parent.hexsha[:7]}'
            file_changes = repo.git.diff(parent, commit, name_status=True).split('\n')

            for change in file_changes:
                change_parts = change.split('\t')
                file_name = change_parts[1] if len(change_parts) > 1 else change_parts[0]
                file_name_escaped = re.sub(r"\"", "\\\"", file_name)
                graph_code += f'    {parent_id} -> {node_id} [xlabel="{file_name_escaped}", style="filled", color=gray]\n'

    graph_code += '}'
    return graph_code

if __name__ == "__main__":
    repo_path = ".\\yep"
    graph_code = generate_git_graph(repo_path)

    with open("git_graph.dot", "w", encoding="utf-8") as dot_file:
        dot_file.write(graph_code)
