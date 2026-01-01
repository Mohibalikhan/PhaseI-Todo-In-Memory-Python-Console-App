# main.py - PREMIUM TODO CLI (NEW MODERN COLOR THEME - 2026 EDITION)
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
import time
import os

console = Console()

# In-memory storage
todos = []
next_id = 1

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    total = len(todos)
    completed = sum(1 for t in todos if t["done"])
    pending = total - completed
    
    header = Panel(
        f"[bold #cba6f7]Premium Todo Master[/] • [#94e2d5]Total: {total}[/] • [#fab387]Pending: {pending}[/] • [#a6e3a1]Completed: {completed}[/]",
        style="bold #89b4fa",
        box=box.DOUBLE
    )
    console.print(header)

def show_todos():
    if not todos:
        empty_panel = Panel(
            "[italic #94e2d5]✨ No tasks yet! Your journey begins now.\nLet's add your first masterpiece.[/]",
            title="[bold #cba6f7]Your Tasks[/]",
            border_style="#89b4fa",
            box=box.ROUNDED,
            padding=(1, 4)
        )
        console.print(empty_panel)
        return

    table = Table(title="[bold #cba6f7]Your Tasks[/]", box=box.ROUNDED, header_style="bold #cba6f7", border_style="#89b4fa")
    table.add_column("ID", style="dim", width=5, justify="center")
    table.add_column("Status", width=15, justify="center")
    table.add_column("Task", style="bold #b4befe")
    table.add_column("Description", style="#cdd6f4")

    for todo in todos:
        status = "[bold #a6e3a1]✓ Completed[/]" if todo["done"] else "[bold #f38ba8]◉ Pending[/]"
        desc = todo["desc"] or "[dim italic]No description[/]"
        table.add_row(str(todo["id"]), status, todo["title"], desc)

    console.print(table)

def add_todo():
    console.print(Panel("[bold #a6e3a1]➕ ADD NEW TASK[/]", border_style="#a6e3a1", box=box.DOUBLE, padding=(0, 2)))
    title = Prompt.ask("   [#cba6f7]Task Title[/]")
    if not title.strip():
        console.print(Panel("[bold #f38ba8]✗ Error: Title cannot be empty![/]", border_style="#f38ba8", padding=(0, 3)))
        time.sleep(1.5)
        return
    desc = Prompt.ask("   [#cba6f7]Description[/] (optional)", default="")

    global next_id
    todos.append({"id": next_id, "title": title.strip(), "desc": desc.strip() or None, "done": False})
    next_id += 1

    success = Panel(
        f"[bold #a6e3a1]✓ Task #{next_id-1} added successfully!\n   \"{title.strip()}\" is now in your list.[/]",
        border_style="#a6e3a1",
        box=box.ROUNDED,
        padding=(1, 3)
    )
    console.print(success)
    time.sleep(1.5)

def update_todo():
    show_todos()
    if not todos: return
    tid = IntPrompt.ask("[#cba6f7]Enter Task ID to update[/]")
    for todo in todos:
        if todo["id"] == tid:
            new_title = Prompt.ask("   [#cba6f7]New Title[/]", default=todo["title"])
            new_desc = Prompt.ask("   [#cba6f7]New Description[/]", default=todo["desc"] or "")
            todo["title"] = new_title
            todo["desc"] = new_desc or None
            console.print(Panel(f"[bold #a6e3a1]✓ Task #{tid} updated successfully![/]", border_style="#a6e3a1", padding=(0, 4)))
            time.sleep(1.5)
            return
    console.print(Panel("[bold #f38ba8]✗ Task not found![/]", border_style="#f38ba8", padding=(0, 4)))
    time.sleep(1.5)

def toggle_todo():
    show_todos()
    if not todos: return
    tid = IntPrompt.ask("[#cba6f7]Enter Task ID to toggle[/]")
    for todo in todos:
        if todo["id"] == tid:
            todo["done"] = not todo["done"]
            status = "completed" if todo["done"] else "pending"
            icon = "✓" if todo["done"] else "◉"
            color = "#a6e3a1" if todo["done"] else "#f38ba8"
            console.print(Panel(f"[bold {color}]{icon} Task #{tid} marked as {status}![/]", border_style=color, padding=(0, 4)))
            time.sleep(1.5)
            return
    console.print(Panel("[bold #f38ba8]✗ Task not found![/]", border_style="#f38ba8", padding=(0, 4)))
    time.sleep(1.5)

def delete_todo():
    show_todos()
    if not todos: return
    tid = IntPrompt.ask("[#cba6f7]Enter Task ID to delete[/]")
    for i, todo in enumerate(todos):
        if todo["id"] == tid:
            removed_title = todo["title"]
            todos.pop(i)
            console.print(Panel(f"[bold #f38ba8]🗑️ Task #{tid} deleted!\n   \"{removed_title}\" removed.[/]", border_style="#f38ba8", box=box.ROUNDED, padding=(1, 3)))
            time.sleep(1.5)
            return
    console.print(Panel("[bold #f38ba8]✗ Task not found![/]", border_style="#f38ba8", padding=(0, 4)))
    time.sleep(1.5)

def main():
    while True:
        clear()
        show_header()
        show_todos()
        
        menu_panel = Panel(
            "[#94e2d5]1[/]  ➤  Add Task\n"
            "[#94e2d5]2[/]  ➤  Update Task\n"
            "[#94e2d5]3[/]  ➤  Toggle Complete\n"
            "[#94e2d5]4[/]  ➤  Delete Task\n"
            "[#f38ba8]5[/]  ➤  Exit Application",
            title="[bold #cba6f7]Command Center[/]",
            border_style="#89b4fa",
            box=box.ROUNDED,
            padding=(1, 4)
        )
        console.print("\n")
        console.print(menu_panel)
        
        choice = Prompt.ask("\n[#89b4fa]Select Option[/]", choices=["1","2","3","4","5"], default="1")
        
        if choice == "1": add_todo()
        elif choice == "2": update_todo()
        elif choice == "3": toggle_todo()
        elif choice == "4": delete_todo()
        elif choice == "5":
            goodbye = Panel(
                "[bold #a6e3a1]Thank you for using Premium Todo Master!\n"
                "Stay focused • Stay productive • Keep crushing it 🌟\n\n"
                "[dim #94e2d5]Made with ❤️ by Mohib Ali Khan • 2026 Edition[/]",
                border_style="#cba6f7",
                box=box.DOUBLE,
                padding=(2, 6)
            )
            clear()
            console.print(goodbye)
            time.sleep(3)
            break
        
        time.sleep(0.8)

if __name__ == "__main__":
    clear()
    welcome_text = Text()
    welcome_text.append("Welcome to\n", style="bold #cba6f7")
    welcome_text.append("ULTIMATE TODO MASTER\n", style="bold #89b4fa")
    welcome_text.append("2026 Premium Edition\n\n", style="bold #a6e3a1")
    welcome_text.append("Made By Mohib Ali Khan", style="italic #94e2d5")

    welcome = Panel(
        welcome_text,
        border_style="#94e2d5",
        box=box.DOUBLE,
        padding=(2, 8),
        title="[bold #f9e2af]✨ PRODUCTIVITY REDEFINED ✨[/]",
        subtitle="[dim #cdd6f4]Press Enter to begin your journey...[/]"
    )
    console.print(welcome)
    input()
    main()