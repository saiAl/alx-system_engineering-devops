What happens when you type google.com in your browser and press Enter?   

We consider this process to be as simple as it gets; all it takes is a few seconds to open your browser, type google.com, and view the webpage. However, this operation involves more technical complexity than you can possibly imagine; during those seconds, many complicated systems interact with each other, to provide you with the webpage. I'll now go over some of the complexity.

1.  DNS lookup:
Each device connected to the Internet has a unique IP address which other machines use to find the device. DNS servers eliminate the need for humans to memorize IP addresses such as 192.168.1.1, the DNS translate hosts names such as google.com to there IP addresses.  When you type google.com into the browser, the browser does not recognize the address. This is when the DNS server comes into play. The DNS server looks for the IP address associated with google.com. it perform a process known as DNS resolution, which can be summed up as follows: a DNS query is sent from the user computer to the DNS resolver. The DNS resolver will try to find the ip address locally, if not then it will sends the query root DNS server, the root dns server knows the location of all the TLD (top level domains) so it returns the location of the TLDs (.com) to the resolver, then the resolver sends another query to the authoritative DNS server asking about google.com address, the authoritative DNS server is going to check his database searches for google.com and return the IP address to the resolver, and then the resolver returns the address to the computer user.


2. TCP/IP Protocol Suit:
The three-way handshake is the process by which the client establishes a connection with the google.com server after knowing its IP address. The connection is made to send http/https requests and receive responses from the server. Before sending the real data between them, both the client and the server have identified one another, 


3.  HTTP/SSL:
HTTP (hypertext transfer protocol) is a layer 7 protocol used to communicate between two devices on the network, the client-side and the server-side. HTTP(s) is an encrypted form of HTTP with an SSL certificate. using this protocol we sends a request for Google's servers asking for its home page, we send a request for Google's home page to its servers via this protocol.


4.  Firewall:
Incoming and outgoing traffic is monitored by firewalls, which are network security devices that can allow or stop traffic based on rules. The firewall will filter our http/https request.


5.  Load-balancer:
The load balancer is a device used to distribute the incoming traffic between the servers. The job of the load balancer is to distribute requests to any available server; an enterprise like Google certainly will have multiple servers to handle and process incoming requests.


6.  Web server:
The web server will handle the request and process it, it will load up HTML, CSS, and JavaScript files and get everything ready to deliver it back to the user as an HTTP response. In addition to that, it will communicate with the application server to process the request. 


7.  Application server and Database:
The application server is a piece of hardware or software that runs back-end logic. It interacts with the database server and web server to deliver a unique and dynamic response. The application server may need to retrieve or store data in order to respond to your request. It works with the database to make sure that your search query is executed effectively. The database is where data is handled, retrieved, and saved.

When the HTTP/HTTPS response eventually finds its way back to the user's computer, your browser will display the Google home page.
