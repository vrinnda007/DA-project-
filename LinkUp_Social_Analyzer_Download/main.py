from graph_algorithms import (social_network, bfs, dfs, shortest_path,
                              mutual_friends, performance_comparison)

def main():
    while True:
        print("\n===== SOCIAL NETWORK ANALYZER =====")
        print("1. Show users and connections\n2. BFS traversal\n3. DFS traversal")
        print("4. Shortest path\n5. Mutual friends\n6. Performance comparison\n7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            for user, friends in social_network.items():
                print(f"{user}: {', '.join(friends) if friends else 'No friends'}")
        elif choice in ("2", "3"):
            user = input("Starting user: ").strip().title()
            result = bfs(social_network, user) if choice == "2" else dfs(social_network, user)
            print(" -> ".join(result) if result else "User not found")
        elif choice == "4":
            a = input("Starting user: ").strip().title()
            b = input("Destination user: ").strip().title()
            result = shortest_path(social_network, a, b)
            if result:
                print("Path:", " -> ".join(result["vertices"]))
                print("Edges:", result["edges"])
                print("Total vertices:", result["total_vertices"])
                print("Total edges:", result["total_edges"])
            else:
                print("No path found or invalid user.")
        elif choice == "5":
            a = input("First user: ").strip().title()
            b = input("Second user: ").strip().title()
            common = mutual_friends(social_network, a, b)
            print("Mutual friends:", ", ".join(common) if common else "None")
        elif choice == "6":
            for row in performance_comparison():
                print(f'{row["nodes"]} nodes: {row["time"]} ms')
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
