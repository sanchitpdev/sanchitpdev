"""Issue-driven Tic-Tac-Toe for the profile README.

Visitors move by opening an issue titled  ttt|move|<0-8>  (the README cell
links pre-fill this). This script applies the move, lets the bot reply,
rewrites the board between the TTT markers in README.md, and leaves a
comment for the workflow to post back on the issue.
"""
import json
import random
import re
import sys
from pathlib import Path

REPO = "sanchitpdev/sanchitpdev"
STATE = Path(__file__).parent / "state.json"
README = Path(__file__).parent.parent / "README.md"
COMMENT = Path(__file__).parent / "comment.txt"

X, O, EMPTY = "x", "o", ""
WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]


def winner(b):
    for a, c, d in WINS:
        if b[a] and b[a] == b[c] == b[d]:
            return b[a]
    return None


def minimax(b, player):
    w = winner(b)
    if w == O:
        return 1, None
    if w == X:
        return -1, None
    if all(b):
        return 0, None
    best = (-2, None) if player == O else (2, None)
    for i in range(9):
        if not b[i]:
            b[i] = player
            score, _ = minimax(b, X if player == O else O)
            b[i] = EMPTY
            if player == O and score > best[0]:
                best = (score, i)
            if player == X and score < best[0]:
                best = (score, i)
    return best


def bot_move(b):
    open_cells = [i for i in range(9) if not b[i]]
    # 25% of the time the bot plays a random move, so humans can actually win
    if random.random() < 0.25:
        return random.choice(open_cells)
    return minimax(b, O)[1]


def render(state):
    b = state["board"]
    cells = []
    for i in range(9):
        if b[i] == X:
            cells.append("❌")
        elif b[i] == O:
            cells.append("⭕")
        else:
            url = (f"https://github.com/{REPO}/issues/new"
                   f"?title=ttt%7Cmove%7C{i}"
                   f"&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.")
            cells.append(f"[⬜]({url})")
    rows = "\n".join(
        f"| {cells[r]} | {cells[r+1]} | {cells[r+2]} |" for r in (0, 3, 6)
    )
    return (
        "**You are ❌ — click an empty square to play.** "
        "A GitHub Action applies your move and the bot (⭕) answers in ~30 seconds.\n\n"
        "|     |     |     |\n"
        "|:---:|:---:|:---:|\n"
        f"{rows}\n\n"
        f"🏆 Humans **{state['wins']}** · 🤖 Bot **{state['losses']}** · 🤝 Draws **{state['draws']}**"
        + (f"\n\n> {state['last_result']}" if state.get("last_result") else "")
    )


def inject(section):
    text = README.read_text()
    new = re.sub(
        r"(<!-- TTT:START -->).*(<!-- TTT:END -->)",
        lambda m: f"{m.group(1)}\n{section}\n{m.group(2)}",
        text,
        flags=re.S,
    )
    README.write_text(new)


def main():
    title, author = sys.argv[1], sys.argv[2]
    state = json.loads(STATE.read_text())
    b = state["board"]

    m = re.fullmatch(r"ttt\|move\|([0-8])", title.strip())
    if not m:
        COMMENT.write_text("I couldn't parse that move — use the board links in the README. 🙂")
        return
    i = int(m.group(1))
    if b[i]:
        COMMENT.write_text(f"Square {i} is already taken — pick an empty ⬜ from the README board!")
        return

    random.seed(f"{author}:{sum(1 for c in b if c)}:{i}")
    b[i] = X
    msg = f"Move accepted, @{author}! "

    if winner(b) == X:
        state["wins"] += 1
        state["last_result"] = f"🎉 Last game: **@{author} beat the bot!**"
        state["board"] = [EMPTY] * 9
        msg += "…and that's the game — **you beat the bot!** 🎉 Board reset for the next round."
    elif all(b):
        state["draws"] += 1
        state["last_result"] = f"🤝 Last game: draw, finished by @{author}."
        state["board"] = [EMPTY] * 9
        msg += "It's a **draw**! Board reset for the next round."
    else:
        b[bot_move(b)] = O
        if winner(b) == O:
            state["losses"] += 1
            state["last_result"] = f"🤖 Last game: the bot won (sorry @{author})."
            state["board"] = [EMPTY] * 9
            msg += "…but the bot finished you off. 🤖 Board reset — rematch?"
        elif all(b):
            state["draws"] += 1
            state["last_result"] = f"🤝 Last game: draw, finished by @{author}."
            state["board"] = [EMPTY] * 9
            msg += "The bot replied and it's a **draw**! Board reset."
        else:
            msg += "The bot has replied — [back to the board](https://github.com/sanchitpdev#-play-tic-tac-toe-against-my-readme) for your next move!"

    STATE.write_text(json.dumps(state, indent=2) + "\n")
    inject(render(state))
    COMMENT.write_text(msg)


if __name__ == "__main__":
    main()
