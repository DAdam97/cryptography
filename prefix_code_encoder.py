import tkinter as tk
import math

def float_to_binary(value, length):
    bits = ""
    for _ in range(length):
        value *= 2
        if value >= 1:
            bits += "1"
            value -= 1
        else:
            bits += "0"
    return bits

def generate_prefix_code():
    symbols = list("abcdefghijklmnopqrstuvwxyz ")
    n = len(symbols)
    code_length = math.ceil(math.log2(n))

    code_table = {}
    for i in range(n):
        q_i = i * (2 ** (-code_length))
        codeword = float_to_binary(q_i, code_length)
        code_table[symbols[i]] = codeword

    return code_table

def check_mcmillan(code_table):
    total = 0
    for codeword in code_table.values():
        total += 2 ** (-len(codeword))
    return total

def encode_text(text, code_table):
    binary = ""
    for char in text:
        if char not in code_table:
            return None, f"Error: invalid character '{char}'"
        binary += code_table[char]
    return binary, "Encoding successful."

def decode_binary(binary, code_table):
    reverse_table = {code: symbol for symbol, code in code_table.items()}
    text = ""
    buffer = ""
    for bit in binary:
        if bit not in "01":
            return None, f"Error: invalid character '{bit}'"
        buffer += bit
        if buffer in reverse_table:
            text += reverse_table[buffer]
            buffer = ""
    if buffer:
        return None, f"Error: could not decode remaining bits '{buffer}'"
    return text, "Decoding successful."

code_table = generate_prefix_code()
mcmillan = check_mcmillan(code_table)
if mcmillan > 1:
    raise ValueError(f"McMillan inequality violated: {mcmillan} > 1")

def on_encode():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        status_output.config(state=tk.NORMAL)
        status_output.delete("1.0", tk.END)
        status_output.insert("1.0", "Error: text input is empty.")
        status_output.config(state=tk.DISABLED)
        return
    binary, message = encode_text(text, code_table)
    binary_input.delete("1.0", tk.END)
    if binary:
        binary_input.insert("1.0", binary)
    status_output.config(state=tk.NORMAL)
    status_output.delete("1.0", tk.END)
    status_output.insert("1.0", message)
    status_output.config(state=tk.DISABLED)

def on_decode():
    binary = binary_input.get("1.0", tk.END).strip()
    if not binary:
        status_output.config(state=tk.NORMAL)
        status_output.delete("1.0", tk.END)
        status_output.insert("1.0", "Error: binary input is empty.")
        status_output.config(state=tk.DISABLED)
        return
    decoded, message = decode_binary(binary, code_table)
    status_output.config(state=tk.NORMAL)
    status_output.delete("1.0", tk.END)
    if decoded:
        status_output.insert("1.0", message)
        text_input.delete("1.0", tk.END)
        text_input.insert("1.0", decoded)
    else:
        status_output.insert("1.0", message)
    status_output.config(state=tk.DISABLED)

def on_clear():
    text_input.delete("1.0", tk.END)
    binary_input.delete("1.0", tk.END)
    status_output.config(state=tk.NORMAL)
    status_output.delete("1.0", tk.END)
    status_output.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Prefix Code Encoder")
root.geometry("600x400")

tk.Label(root, text="Text Input (a-z and space):").pack(pady=(10, 0))
text_input = tk.Text(root, height=3, width=60)
text_input.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
encode_btn = tk.Button(btn_frame, text="Encode", command=on_encode)
encode_btn.pack(side=tk.LEFT, padx=10)
decode_btn = tk.Button(btn_frame, text="Decode", command=on_decode)
decode_btn.pack(side=tk.LEFT, padx=10)
clear_btn = tk.Button(btn_frame, text="Clear", command=on_clear)
clear_btn.pack(side=tk.LEFT, padx=10)

tk.Label(root, text="Binary Code:").pack(pady=(10, 0))
binary_input = tk.Text(root, height=3, width=60)
binary_input.pack(pady=5)

tk.Label(root, text="Status:").pack(pady=(10, 0))
status_output = tk.Text(root, height=2, width=60, state=tk.DISABLED, bg="#f0f0f0")
status_output.pack(pady=5)

root.mainloop()