servers = ["web-server-01", "db-server-01", "cache-server-01"]

for server in servers:
    print(f"Pinging... {server}")
    
print("All servers pinged.")