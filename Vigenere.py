import streamlit as st

# Variabler:

key_default = "programmering"

# Min dictionary for appen.
lock = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":10,"q":11,"w":12,"e":13,"r":14,
       "t":15,"y":16,"u":17,"i":18,"o":19,"p":20,"å":21,"¨":22,"a":23,"s":24,"d":25,"f":26,"g":27,
       "h":28,"j":29,"k":30,"l":31,"æ":32,"ø":33,"'":34,"<":35,"z":36,"x":37,"c":38,"v":39,"b":40,
       "n":41,"m":42,",":43,".":44,"-":45,"½":46,"§":47,"!":48,"\"":49,"#":50,"¤":51,"%":52,"&":53,
       "/":54,"(":55,")":56,"=":57,"+":58,"?":59,"@":60,"£":61,"$":62,"{":63,"[":64,"]":65,"}":66,
       "\\":67,"|":68,"´":69,"`":70,"Q":71,"W":72,"E":73,"R":74,"T":75,"Y":76,"U":77,"I":78,"O":79,
       "P":80,"Å":81,"^":82,"A":83,"S":84,"D":85,"F":86,"G":87,"H":88,"J":89,"K":90,"L":91,"Æ":92,
       "Ø":93,"*":94,">":95,"Z":96,"X":97,"C":98,"V":99,"B":100,"N":101,"M":102,";":103,":":104,"_":105}

# Omvendt dictionary for dekryptering:
unlock = {value: key for key, value in lock.items()}



# Funktioner

def vigenere_encrypt(text, key):
    encrypted = []
    key_list = list(key)
    key_index = 0

    for char in text:
        if char not in lock:
            encrypted.append(char)
            continue

        text_value = lock[char]
        key_value = lock.get(key_list[key_index % len(key_list)], 1)

        cipher_value = (text_value + key_value) % len(lock)
        cipher_value = cipher_value if cipher_value != 0 else len(lock)

        encrypted.append(unlock[cipher_value])
        key_index += 1

    return "".join(encrypted)


def vigenere_decrypt(text, key):
    decrypted = []
    key_list = list(key)
    key_index = 0

    for char in text:
        if char not in lock:
            decrypted.append(char)
            continue

        text_value = lock[char]
        key_value = lock.get(key_list[key_index % len(key_list)], 1)

        plain_value = (text_value - key_value) % len(lock)
        plain_value = plain_value if plain_value != 0 else len(lock)

        decrypted.append(unlock[plain_value])
        key_index += 1

    return "".join(decrypted)



# Herunder har vi koden for Streamlit UI:

st.title("Vigenere Cipher")

st.markdown("This app encrypts and decrypts text.  \n\n To make it work, enter your intended message you want encrypted down below \n whereafter you can take the output and decrypt again.\n\n Type your own key, or let it be its default value.")


input_text = st.text_input("Enter your message:")
key = st.text_input("Enter key:", key_default)
option = st.radio("Choose action:", ["Encrypt", "Decrypt"])

if st.button("Run"):
    if option == "Encrypt":
        result = vigenere_encrypt(input_text, key)
        st.success("Encrypted message:")
        st.code(result)
    else:
        result = vigenere_decrypt(input_text, key)
        st.success("Decrypted message:")
        st.code(result)
