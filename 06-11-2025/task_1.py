log_data = [
    500, "user-123", 1.2, {"path": "/login"}, ["critical"], 200, "user-456",
    0.5, {"path": "/home"}, 404, "user-123", 2.1, ["error", "api"],
    "user-789", 0.1, {"path": "/"}, 503, 3.5, ["db", "timeout"],
    "user-456", 0.8, {"path": "/data"}, 200, 201, "user-101",
    1.1, {"path": "/img"}, ["new"], 401, "user-123", 0.3, {"path": "/admin"}
]
user_ids = []
error_codes = []
for scrap in log_data:
    if str(scrap).startswith('user') and not scrap in user_ids:
        user_ids.append(scrap)
    elif type(scrap) == int and not scrap in error_codes:
        error_codes.append(scrap)

output = {'user_ids': user_ids, 'error_codes': error_codes}
print(output)