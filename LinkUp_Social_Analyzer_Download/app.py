from flask import Flask, render_template, request
from graph_algorithms import (social_network, bfs, dfs, shortest_path,
                              mutual_friends, performance_comparison)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    operation = "bfs"
    start = "Alice"
    end = "Ivy"
    users = list(social_network.keys())

    if request.method == "POST":
        operation = request.form.get("operation", "bfs")
        start = request.form.get("start", "Alice")
        end = request.form.get("end", "Ivy")

        if operation == "bfs":
            result = {"type": "traversal", "title": "Breadth First Search",
                      "description": "Visits nearby users level by level using a queue.",
                      "order": bfs(social_network, start)}
        elif operation == "dfs":
            result = {"type": "traversal", "title": "Depth First Search",
                      "description": "Explores one branch deeply before backtracking using a stack.",
                      "order": dfs(social_network, start)}
        elif operation == "shortest":
            result = {"type": "path", "title": "Shortest Connection Path",
                      "path": shortest_path(social_network, start, end)}
        elif operation == "mutual":
            result = {"type": "mutual", "title": "Mutual Friends",
                      "people": mutual_friends(social_network, start, end),
                      "first": start, "second": end}
        elif operation == "performance":
            result = {"type": "performance", "title": "BFS Performance",
                      "rows": performance_comparison()}

    total_edges = sum(len(v) for v in social_network.values()) // 2
    return render_template("index.html", users=users, graph=social_network,
                           result=result, operation=operation, start=start,
                           end=end, total_edges=total_edges)

if __name__ == "__main__":
    app.run(debug=True)
