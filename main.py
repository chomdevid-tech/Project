from bridge import start_event_bridge
from sniffer import start_sniffer, EVENT_QUEUE




def main():



    

    print("[+] Starting Mini-IDPS System...")

    # Start the event loop thread from event_bridge
    bridge_thread = start_event_bridge()

    # Start packet sniffer (blocking)
    start_sniffer()

    # If the sniffer stops naturally, stop the event loop
    EVENT_QUEUE.put(None)
    bridge_thread.join()

    print("[+] Mini-IDPS stopped cleanly.")

if __name__ == "__main__":
    print(
'''                                                                                                                                                                                                                                                                                                 
MMMMMMMM               MMMMMMMMIIIIIIIIIINNNNNNNN        NNNNNNNNIIIIIIIIII     IIIIIIIIIIDDDDDDDDDDDDD      PPPPPPPPPPPPPPPPP      SSSSSSSSSSSSSSS 
M:::::::M             M:::::::MI::::::::IN:::::::N       N::::::NI::::::::I     I::::::::ID::::::::::::DDD   P::::::::::::::::P   SS:::::::::::::::S
M::::::::M           M::::::::MI::::::::IN::::::::N      N::::::NI::::::::I     I::::::::ID:::::::::::::::DD P::::::PPPPPP:::::P S:::::SSSSSS::::::S
M:::::::::M         M:::::::::MII::::::IIN:::::::::N     N::::::NII::::::II     II::::::IIDDD:::::DDDDD:::::DPP:::::P     P:::::PS:::::S     SSSSSSS
M::::::::::M       M::::::::::M  I::::I  N::::::::::N    N::::::N  I::::I         I::::I    D:::::D    D:::::D P::::P     P:::::PS:::::S            
M:::::::::::M     M:::::::::::M  I::::I  N:::::::::::N   N::::::N  I::::I         I::::I    D:::::D     D:::::DP::::P     P:::::PS:::::S            
M:::::::M::::M   M::::M:::::::M  I::::I  N:::::::N::::N  N::::::N  I::::I         I::::I    D:::::D     D:::::DP::::PPPPPP:::::P  S::::SSSS         
M::::::M M::::M M::::M M::::::M  I::::I  N::::::N N::::N N::::::N  I::::I         I::::I    D:::::D     D:::::DP:::::::::::::PP    SS::::::SSSSS    
M::::::M  M::::M::::M  M::::::M  I::::I  N::::::N  N::::N:::::::N  I::::I         I::::I    D:::::D     D:::::DP::::PPPPPPPPP        SSS::::::::SS  
M::::::M   M:::::::M   M::::::M  I::::I  N::::::N   N:::::::::::N  I::::I         I::::I    D:::::D     D:::::DP::::P                   SSSSSS::::S 
M::::::M    M:::::M    M::::::M  I::::I  N::::::N    N::::::::::N  I::::I         I::::I    D:::::D     D:::::DP::::P                        S:::::S
M::::::M     MMMMM     M::::::M  I::::I  N::::::N     N:::::::::N  I::::I         I::::I    D:::::D    D:::::D P::::P                        S:::::S
M::::::M               M::::::MII::::::IIN::::::N      N::::::::NII::::::II     II::::::IIDDD:::::DDDDD:::::DPP::::::PP          SSSSSSS     S:::::S
M::::::M               M::::::MI::::::::IN::::::N       N:::::::NI::::::::I     I::::::::ID:::::::::::::::DD P::::::::P          S::::::SSSSSS:::::S
M::::::M               M::::::MI::::::::IN::::::N        N::::::NI::::::::I     I::::::::ID::::::::::::DDD   P::::::::P          S:::::::::::::::SS 
MMMMMMMM               MMMMMMMMIIIIIIIIIINNNNNNNN         NNNNNNNIIIIIIIIII     IIIIIIIIIIDDDDDDDDDDDDD      PPPPPPPPPP           SSSSSSSSSSSSSSS                                                                                                                                                                                                                                                                                                                                                                                                                                  
'''        
)
    main()
