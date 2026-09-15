import gradio as gr

class Hotel:
    count = 0

    def __init__(self, name, age, days, typ):
        self.name = name
        self.age = age
        self.days = days
        self.typ = typ
        self.done = False
        self.price = 100 if typ == "Single" else 150
        self.room = 101 + Hotel.count if typ == "Single" else 201 + Hotel.count
        Hotel.count += 1

    def bill(self):
        total = self.days * self.price
        if self.days >= 3 and self.done:
            total *= .9
        return total

guests = []

def book(name, age, days, typ):
    g = Hotel(name, age, days, typ)
    guests.append(g)
    return f"Booked!\nRoom: {g.room}\nTotal: ${g.bill():.2f}"

def done(n):
    guests[n-1].done = True
    return "First day completed."

def cancel(n):
    g = guests[n-1]
    if g.days >= 3 and not g.done:
        return "Complete first day first."
    total = g.days * g.price
    fee = total * .05
    refund = total - g.price - fee
    guests.pop(n-1)
    return f"Refund: ${refund:.2f}"

with gr.Blocks(title="Hotel Management System") as app:
    gr.Markdown("# 🏨 Hotel Management System")
    name = gr.Textbox(label="Name")
    age = gr.Number(label="Age")
    days = gr.Number(label="Days")
    typ = gr.Dropdown(["Single","Double"], label="Room")
    n = gr.Number(label="Booking No.", precision=0)

    out = gr.Textbox()

    gr.Button("Book").click(book, [name,age,days,typ], out)
    gr.Button("Complete First Day").click(done, n, out)
    gr.Button("Cancel").click(cancel, n, out)

app.launch()