import os, time
log_dir = "./logs"
now = time.time()
for f in os.listdir(log_dir):
    path = os.path.join(log_dir, f)
    if os.stat(path).st_mtime < now - 7*86400:
        os.remove(path)
        print(f"Deleted {f}")