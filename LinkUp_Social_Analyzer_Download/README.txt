LINKUP - SOCIAL NETWORK ANALYZER (FIXED VERSION)

RUN:
1. Extract this ZIP.
2. Open the folder in VS Code.
3. Run: pip install flask
4. Run: python app.py
5. Visit: http://127.0.0.1:5000

For terminal mode: python main.py

SAMPLE DATA:
Alice: Bob, Charlie, David
Bob: Alice, Emma, Frank
Charlie: Alice, David, Grace
David: Alice, Charlie, Harry
Emma: Bob, Frank
Frank: Bob, Emma, Ivy
Grace: Charlie, John
Harry: David, John
Ivy: Frank
John: Grace, Harry
Kevin: No friends

11 vertices, 10 unique undirected edges. Undirected and unweighted graph.
Algorithms: BFS, DFS, shortest path using BFS, mutual friends, performance test.

FIXES:
- BFS/DFS output uses the key "order", avoiding collision with Python dict.items.
- After Run Analysis, the page scrolls to the output panel, not the bottom.
