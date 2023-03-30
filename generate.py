import os

def main():
    username = os.environ["GITHUB_ACTOR"]
    snake_file = f"{JagadeeshJD}.svg"
    os.system(f"curl -s -o {snake_file} https://github.com/{JagadeeshJD}")
    with open("README.md", "a") as f:
        f.write(f"\n![](./{snake_file})\n")

if __name__ == "__main__":
    main()
