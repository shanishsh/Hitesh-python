def serve_chi():
    chai_type = "Masala" # local scope
    print(f"Inside funtion {chai_type}")

chai_type = "Lemon"
serve_chi()
print(f"Outside function: {chai_type}")