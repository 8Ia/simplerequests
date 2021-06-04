from tkinter import *
import requests
root = Tk()


url = Entry(root)
url.pack(pady=30)


def request():
    urlget = url.get()
    req = requests.request('GET', urlget, timeout=5)
    if req.status_code == 200:
        Label(root, text="200 Response, Site is Up!").pack()
    elif req.status_code == 403:
        Label(root, text="403 Response, denied access").pack()
    elif req.status_code == 400:
        Label(root, text="400 Response, bad client request").pack()
    elif req.status_code == 408:
        Label(root, text="408 Response, timed out").pack()
    elif req.status_code == 404:
        Label(root, text="404 Response, not found lmao").pack()
    

Button(
    root,
    text="request",
    padx=10,
    pady=5,
    command=request
    ).pack()

root.mainloop()
