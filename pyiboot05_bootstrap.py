OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".img\\")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def generate_cpu():
    # uuid = subprocess.check_output('wmic csproduct get uuid', shell=False).decode().strip()
    uuid = subprocess.check_output('wmic cpu get name', shell=False).decode().strip()
    hashed_hwid = hashlib.sha256(uuid.encode()).hexdigest()
    return hashed_hwid
def generate_hwid():
    uuid = subprocess.check_output('wmic csproduct get uuid', shell=False).decode().strip()
    hashed_hwid = hashlib.sha256(uuid.encode()).hexdigest()
    return hashed_hwid
def gethwid():
    blist = []
    uuid = subprocess.check_output('wmic csproduct get uuid', shell=False).decode()
    uuid = uuid.strip().split('\r\n')
    blist.append(uuid[1])
    blist = json.dumps(blist, ensure_ascii=False).encode('utf-8')
    blist = b'PRP' + base64.b64encode(blist)
    return blist.decode('UTF-8')
def datahwidreg() -> str:
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://pastebin.com/raw/AsmGzNHk')
    return response.data.decode()

new_hwid = generate_hwid()[:8]
new_cpu = generate_cpu()[:8]
hw = gethwid()[:15]
mypcname = os.getlogin()
hwid = f'''{hw}-{mypcname}-{new_hwid}{new_cpu}'''


def loginsus():
    hwid_data = datahwidreg()
    if hwid in hwid_data:
        import file.hwid
        window.title(f"PRP Test LOCKHWID | User : {mypcname} | Status : Succeed | ✅ ")
    else:
        messagebox.showerror("Login Failed", "ไม่พบ HWID")
        window.title(f"PRP Test LOCKHWID | User : {mypcname} | Status : Failed | ❌ ")

def opendiscord():
    webbrowser.open("https://discord.gg/eHMmneSs3c")

window = Tk()

window.geometry("640x366")
window.configure(bg = "#FFFFFF")
window.title(f"PRP Test LOCKHWID | User : {mypcname}")



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 366,
    width = 641,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    320.0,
    83.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    320.0,
    266.46484375,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    79.0,
    138.0,
    image=image_image_3
)

button_1 = Button(
    text="เข้าสู่ระบบ",
    borderwidth=0,
    highlightthickness=0,
    command=loginsus,
    relief="flat"
)
button_1.place(
    x=253.0,
    y=264.0,
    width=142.08837890625,
    height=35.26904296875
)

button_2 = Button(
    text="Discord",
    borderwidth=0,
    highlightthickness=0,
    command=opendiscord,
    relief="flat"
)
button_2.place(
    x=253.0,
    y=312.0,
    width=142.08837890625,
    height=35.26904296875
)

textbox = Text(window, state='disable')
textbox.pack()

textbox.config(height=1, width=44 ,font=("Inter", 22 * -1), state='normal')
textbox.insert(END, f"{hwid}\n")
print(hwid)
textbox.place(x=38, y=217)
textbox.config(bg='#ffffff')

canvas.create_text(
    160.0,
    165.0,
    anchor="nw",
    text="PRP",
    fill="#000000",
    font=("Inter ExtraBold", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
