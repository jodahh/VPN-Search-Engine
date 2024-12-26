 
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
from vpn_addres_getter import sstp_protocol_vpn, l2tp_protocol_vpn, open_vpn_protocol_vpn

def insert_openvpn(conf):
    st.delete(1.0, ttk.END)
    for i in conf: 
        st.insert(END, i)

def insert_l2tp(conf):
    st.delete(1.0, ttk.END)
    for i in conf: 
        st.insert(END, i)

def insert_sstp(conf):
    st.delete(1.0, ttk.END)
    for i in conf: 
        st.insert(END, i)

root = ttk.Window(themename = "yeti")
root.title('Систематизация доступных бесплатных VPN')
root.geometry('826x600')
root.resizable(False, False)

SSTP_Button = ttk.Button(root, text = "Протокол SSTP",  command=lambda: insert_sstp(sstp_protocol_vpn()))
SSTP_Button.place(x = 10, y = 20)

L2TP_Button = ttk.Button(root, text = "Протокол L2TP",  command=lambda: insert_l2tp(l2tp_protocol_vpn()))
L2TP_Button.place(x = 140, y = 20)

OPENVPN_Button = ttk.Button(root, text = "Протокол OpenVPN",  command=lambda: insert_l2tp(open_vpn_protocol_vpn()))
OPENVPN_Button.place(x = 270, y = 20)

st = ScrolledText(root, width = 95, height = 25, autohide = True)
st.place(x = 10, y = 60)
# st.pack(fill=BOTH)
# expand=YES
# add text

root.mainloop()