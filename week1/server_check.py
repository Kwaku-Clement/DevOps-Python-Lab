cpu_input = input("Enter CPU usage percentage (e.g., 85): ")
cpu_usage = int(cpu_input)

if cpu_usage > 90:
    print("⚠️ ALERT: CPU usage is critical")
elif 70 <= cpu_usage:
    print("⚠️ WARNING: CPU usage is high.")
else:
    print("✅ CPU usage is normal.")