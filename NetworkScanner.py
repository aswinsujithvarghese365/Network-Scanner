import tkinter as tk
from tkinter import scrolledtext
from scapy.all import *

app = tk.Tk()
app.title("Network Packet Sniffer")
app.geometry("600x400")

text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=70, height=20)
text_area.pack(padx=10, pady=10)

# Create a variable to store the selected protocol
selected_protocol = tk.StringVar()

# Function to capture and display packets
def packet_sniffer(packet):
    packet_info = ""

    # Check if the packet has an IP layer
    if IP in packet:
        packet_info += f"Source IP: {packet[IP].src}\nDestination IP: {packet[IP].dst}\n"
        packet_info += f"Protocol: {packet[IP].proto}\n\n"
    else:
        packet_info += "Unknown Packet\n\n"

    text_area.insert(tk.END, packet_info)
    text_area.see(tk.END)

def start_sniffing():
    print("Starting sniffing...")
    start_button.config(state=tk.DISABLED)
    sniff(iface="eth0", prn=packet_sniffer, count=100)
    print("Sniffing finished.")
    start_button.config(state=tk.NORMAL)

start_button = tk.Button(app, text="Start Sniffing", command=start_sniffing)
start_button.pack(pady=10)

app.mainloop()
