"""
File:    the_interenet.py
Author:  Prince Michael Kemani
Date:    11/30/24
Section: 16
E-mail:  pkemani1@umbc.edu
Description:
An internet that connects servers
"""
'''
put this in internet dictionary
server_name : {
                "ip_address" : ____
                "connected_server" : ____
                }
'''
# CONSTANTS
CREATE_SERVER = "create-server"
CREATE_CONNECTION = "create-connection"
QUIT = "quit"
SET_SERVER = 'set-server'
TRACEROUTE = "traceroute"
DISPLAY_SERVERS = "display-servers"
TRACERT = "tracert"
IP_CONFIG = "ip-config"
PING = "ping'"

def create_server(server_name, ip_address, internet):
    '''
    create a server and adds that server to the internet dictionary... server is a dictionary with key = server_name an values will be a list
    that contains ip address and another dictionary which its key is the connected server and the time between the current server and connected
    server
    : param server_name :
    : param ip_address:
    : param internet:
    : return : 
    '''
    connections = {}
    
    # if internet is empty, add server without worry 
    if not internet:
        internet[server_name] = {"ip_address" : ip_address}

    # check if ip address is duplicate
    else:
        for server in internet: # accessing each server in the internet
            if server != server_name and internet[server]["ip_address"] == ip_address: # checks if server with different name has the same ip address
                print("This is a duplicate ip address, so new server could not be created")
                return 0
            # if server is given a new ip address then replace the old one  
            elif server == server_name and internet[server]["ip_address"] != ip_address:
                internet[server_name]["ip_address"] = ip_address
                print(f"{server_name} was given a new ip_address of {ip_address}")
                return 0 
            # if ip_address is the same as was previously print("that ip address already exists for that server")
            elif server == server_name and internet[server]["ip_address"] == ip_address:
                print("That ip address already exists for that server")
                return 0
        if server_name not in internet:
            internet[server_name] = {"ip_address" : ip_address}
            
    print(f"Success: A server with name {server_name} was created at ip {ip_address}")
    
def create_connection(server1, server2, connection_time, internet):
    '''
    fxn header
    '''
    # make sure internet isn't empty
    if len(internet) < 2:
        print("Internet needs 1 or 2 more servers")
        return 0
    # make sure both servers exist in internet
    elif server1 not in internet or server2 not in internet:
        print("One of your servers don't exist in internet... TRY AGAIN!")
        return 0
    elif server2 in internet[server1]: # make sure servers aren't aready connected
        print("Those servers are already connected... TRY AGAIN!")
        return 0
    # give each server a spot in there dictionary with key  being connected server and value being connection time between those 2 servers
    internet[server1][server2] = [internet[server2]["ip_address"] , int(connection_time)]
    internet[server2][server1] = [internet[server1]["ip_address"], int(connection_time)]
    print(f"A server with name {server1} is now connected to {server2}")
    
def check_ip(ip_address):
    '''
    checks to see if ip_address is valid or not by seeing if each number sepeated by periods is between 155
    :param ip_address: the ip address string from the user that is converted to 4 seperated integers between the periods and checked for validity
    : return : returns True is ip_address is a valid ip_address and vice versa
    '''
    split_ip = ip_address.split(".")

    if len(split_ip) != 4:
        print("That shit outta range lil nigga")
        return False
    for i in range(len(split_ip)):
        split_ip[i] = int(split_ip[i]) # convert each index to integer
    for number in split_ip:
        if number <= 0 or number >= 255:
            return False
    return True

def display_servers(internet):
    '''
    fxn header
    '''
    if not internet:
        print("Internet is empty... add a server!")
    else:
        for server in internet:
            print(f"{server}\t{internet[server]["ip_address"]}")
            for inner_server in internet[server]:
                if inner_server != "ip_address":
                    print(f"\t{inner_server}\t{internet[server][inner_server][0]}\t{internet[server][inner_server][1]}")

            
def set_server(server_name, internet):
    '''
    sets our current place on the internet which is going to be the parameter value which is a server
    :param server_name: name of server that we are going to "start"
    :param internet: internet dictionary that allows us to check if server_name exists in our internet
    '''
    # make sure internet isn't empty
    if not internet:
        print("internet is empty... create a server_first")
        return 0
    # check if server in internet or ip address is an ip_address
    else:
        if server_name not in internet:
            i = 0 # 
            for server in internet:
                if server_name != internet[server]['ip_address']:
                    i += 1
            if i == len(internet):
                print(f"{server_name} is not a server or ip_address in our internet... TRY AGAIN!!")
                return 0
        if server_name in internet:
            # check if sever is a server in the internet by name
            print(f"Server {server_name} was selected.")
            return server_name
        # if it isn't check if it is a server in the internet by ip_address
        else:
            # access internet dictionary server-by0server and return server_name of server cooresponding to that ip address if exists 
            for server in internet:
                if server_name == internet[server]['ip_address']:
                    print(f"Server {server} was selected.")
    

def ip_config(internet, current_server):
    '''
    fxn header
    '''
    if current_server not in internet:
        print("Set a valid server first nigga")
    else:
        print(f"{current_server}\t{internet[current_server]["ip_address"]}")
        current_server = internet[current_server]["ip_address"]

        return current_server

def ping(server_name):
    pass

def tracerout(server_name):
    pass
    
    
def run_the_internet():
    '''
    description
    '''
    # dictionary to store all my servers
    internet = {
    
    }
    current_server = [""]
    user_input = input(">>> ")
    while user_input.lower() != QUIT:
        run_program(user_input, internet, current_server)
        user_input = input(">>> ")



def run_program(user_input, internet, current_server):
    '''
    runs main functions of the program
    :param user_input: gets input from user and uses it to run program
    :returns ...
    '''
    # create a variable that allows you locally access the "current value" for ip-config
    calls = user_input.split() # create a list of "calls"
    # index into calls list in order to access each call easier if youre creating or connected servers
    command = calls[0].lower()
    if len(calls) >= 2:
        server_name = calls[1].lower()
    if len(calls) >= 3:
        ip_address = calls[2].lower()
    # if command is not a valid command let user try again
    if command not in [CREATE_CONNECTION, CREATE_SERVER, QUIT, SET_SERVER, TRACEROUTE, DISPLAY_SERVERS, TRACERT, IP_CONFIG, PING]:
        print(f"{command} is not a valid command...TRY AGAIN")
    # check commands
    elif command == CREATE_SERVER:
        # check if ip_address is valid 
        validation = check_ip(ip_address)
        if validation: # if ip_address is valid retrieve server name, ip_address, and try to create the server
            server_name = calls[1].lower()
            ip_address = calls[2].lower()
            create_server(server_name, ip_address, internet)
    elif command == CREATE_CONNECTION:
        # retrieve first two servers and connection time, and try to connect the servers with connection time
            server1 = calls[1].lower()
            server2 = calls[2].lower()
            connection_time = calls[3].lower()
            create_connection(server1, server2, connection_time, internet)
    elif command == DISPLAY_SERVERS: # display servers in terminal when command called
        display_servers(internet)
    elif command == SET_SERVER: # server_name as our current server
        possible_current_value = set_server(server_name, internet)
        if possible_current_value in internet:
            current_server[0] = possible_current_value
    elif command == IP_CONFIG:
        ip_config(internet, current_server[0])

            

if __name__ == '__main__':
    run_the_internet()