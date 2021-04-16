import socket
# import termcolor
import server_utils as utils

list_seq = ["ACCAGATTTAACAAG", "ACAGAACTTAACTTA", "GCTAGAGACTACAGA", "ACTAGATAATAACCG", "TACGGCTTAAACCAT"]
PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("SEQ Server up!")
while True:
    print("Awaiting client...")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        # print("A client has connected to the server!")
        msg = utils.format_command(cs.recv(2048).decode())
        if msg == "PING":
            res = "OK!"
#            print(termcolor.colored("PING command!", "green"))
            utils.ping()
        elif "GET" in msg:
            res = list_seq[int(msg[-1])]
            utils.print_colored("GET", "green")
        elif "INFO" in msg:
            utils.print_colored("INFO", "green")
            res = utils.info(msg.replace("INFO ", ""))
        elif "COMP" in msg:
            utils.print_colored("COMP", "green")
            res = utils.comp(msg.replace("COMP ", ""))
        elif "REV" in msg:
            utils.print_colored("REV", "green")
            res = utils.rev(msg.replace("REV ", ""))
        elif "GENE" in msg:
            utils.print_colored("GENE", "green")
            res = utils.gene(msg.replace("GENE ", "../P0/Sequences/"))
        else:
            res = "..."
        print(res)
        cs.send(res.encode())
        cs.close()
