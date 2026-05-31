import tkinter as tk

def create_popup(message):
    # main hidden root window
    root = tk.Tk()
    root.withdraw()

    # popup size
    width = 500
    height = 250

    # create popup window
    popup = tk.Toplevel(root)
    popup.title("SECURITY ALERT")

    # colors
    bg_color = "#000000"
    text_color = "#FF2E2E"
    button_bg = "#FF2E2E"
    button_fg = "#FFFFFF"

    # basic setup
    popup.config(bg=bg_color)
    popup.attributes("-topmost", True)  # keep on top
    popup.update_idletasks()

    # position bottom-right
    screen_w = popup.winfo_screenwidth()
    screen_h = popup.winfo_screenheight()
    x = screen_w - width - 60
    y = screen_h - height - 100
    popup.geometry(f"{width}x{height}+{x}+{y}")

    # title label
    title = tk.Label(
        popup,
        text="SECURITY ALERT\nINTRUSION DETECTED",
        bg=bg_color,
        fg=text_color,
        font=("Arial", 18, "bold")
    )
    title.pack(pady=10)

    # message label
    msg = tk.Label(
        popup,
        text=message,
        bg=bg_color,
        fg="#CCCCCC",
        font=("Arial", 12),
        wraplength=450,
        justify="center"
    )
    msg.pack(pady=5)

    # close button
    def close():
        popup.destroy()
        root.destroy()

    ok_btn = tk.Button(
        popup,
        text="ACKNOWLEDGE",
        command=close,
        bg=button_bg,
        fg=button_fg,
        font=("Arial", 12, "bold"),
        width=14
    )
    ok_btn.pack(pady=15)

    # make popup modal
    popup.grab_set()
    root.mainloop()
