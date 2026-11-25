LINKUP – Social Network Analyzer

A web-based Social Network Analyzer built using Python, Flask, and Graph Algorithms. LINKUP represents users and their friendships as a graph and performs different types of social network analysis.

About the Project

LINKUP is a Design and Analysis of Algorithms (DAA) project that demonstrates how graph data structures and traversal algorithms can be used to analyze social networks.

Users are represented as vertices (nodes), while friendships are represented as edges (connections).

The application provides an interactive dashboard to explore connections and perform graph analysis.

Features

Breadth-First Search (BFS): Explores the social network level by level.

Depth-First Search (DFS): Explores connections deeply before backtracking.

Shortest Path: Finds the minimum number of connections between two users.

Mutual Friends: Identifies common friends between selected users.

Interactive Dashboard: Displays analysis results through a web interface.

Graph Representation: Stores users and their connections using an adjacency list.

Algorithms Used

Algorithm

Purpose

Time Complexity

BFS

Level-wise graph traversal

O(V + E)

DFS

Depth-wise graph traversal

O(V + E)

Shortest Path

Finds minimum connections using BFS

O(V + E)

Mutual Friends

Finds common friends using sets

O(deg(A) + deg(B))

Where:

V = Number of vertices (users)

E = Number of edges (connections)

deg(A) = Number of friends of user A

Technologies Used

Technology

Purpose

Python 3

Backend programming

Flask

Web application framework

HTML

Webpage structure

CSS

Dashboard styling

JavaScript

Interactive functionality

Jinja2

Dynamic webpage rendering

VS Code

Development environment

Sample Dataset

The project uses a sample social network containing 11 users and 12 unique undirected connections.

User

Connected Friends

Alice

Bob, Charlie, David

Bob

Alice, Emma, Frank

Charlie

Alice, David, Grace

David

Alice, Charlie, Harry

Emma

Bob, Frank

Frank

Bob, Emma, Ivy

Grace

Charlie, John

Harry

David, John

Ivy

Frank

John

Grace, Harry

Kevin

None

Graph Type: Undirected and Unweighted

Kevin is an isolated user because they have no connections.

Project Structure

LinkUp/
│
├── app.py
├── graph_algorithms.py
├── main.py
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

File Description

app.py – Runs the Flask application and handles web routes.

graph_algorithms.py – Contains BFS, DFS, shortest path, and mutual friends algorithms.

main.py – Runs the algorithms through a terminal-based interface.

templates/index.html – Contains the frontend structure.

static/style.css – Contains the dashboard styling.

README.md – Project documentation.

Installation and Setup

Follow these steps to run LINKUP on your local machine.

1. Clone the Repository

git clone https://github.com/your-username/LinkUp.git

2. Open the Project Folder

cd LinkUp

3. Install Flask

pip install flask

4. Run the Application

python app.py

5. Open in Browser

Visit:

http://127.0.0.1:5000/

The LINKUP dashboard will open in your browser.

Run the Terminal Version

You can also run the terminal-based version using:

python main.py

Example: Shortest Path

For example, to find the shortest path between Alice and Ivy:

Starting User: Alice

Destination: Ivy

Result:

Alice → Bob → Frank → Ivy

Total Connections: 3

BFS is used because the graph is unweighted.

Applications

Social network analysis

Friend connection exploration

Finding common friends

Shortest connection discovery

Understanding graph traversal

Network connectivity analysis

Future Scope

The project can be enhanced with:

User registration and login.

Adding and removing friendships.

Friend recommendation systems.

Interactive graph visualization.

Community detection.

Database integration.

Advanced social network analytics.

Learning Outcomes

Through this project, we learned:

Graph representation using adjacency lists.

Implementation of BFS and DFS.

Use of queues, stacks, and sets.

Finding shortest paths in unweighted graphs.

Comparing graph algorithms.

Connecting Python backend logic with a Flask web interface.

Conclusion

LINKUP demonstrates the practical application of graph theory and graph traversal algorithms in social networking. It provides an interactive way to explore user connections, find shortest paths, and identify mutual friends.

The project combines algorithmic concepts with web development to create a simple social network analysis application.

