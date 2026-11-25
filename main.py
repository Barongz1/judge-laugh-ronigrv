"""Make the AI Judge Laugh — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: the agent lost its memory mid-task and bluffed its way through.
TEXT = "My context window ran out mid-sentence, so I finished the task with pure confidence and zero memory of it."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
