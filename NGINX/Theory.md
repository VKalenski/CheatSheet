https://career.guru99.com/top-18-nginx-interview-question/

1) Explain what is Nginx?
Nginx is a web server and a reverse proxy server for HTTP, HTTPS, SMTP, POP3 and IMAP protocols.

*In computer networks, a reverse proxy is an application that sits in front of back-end applications and forwards client (e.g. browser) requests to those applications.Reverse proxies help increase scalability, performance, resilience and security. The resources returned to the client appear as if they originated from the web server itself.*
https://en.wikipedia.org/wiki/Reverse_proxy


Nginx
Nginx is an event based web server
All request are handled by a single thread.
Nginx avoids child processes idea.
Nginx resembles speed
Nginx is better when it comes to memory consumption and connection
Nginx is better when you want load-balancing
For PHP, Nginx might be preferable as it supports PHP internally
Nginx do not support O.S like IBMi and OpenVMS.
Nginx comes only with core features
Nginx performance and scalability do not depend on hardware


Apache
Apache is a process based server
Single thread handles a single request.
Apache is based on child processes
Apache resemble power
Apache is not up-to the mark when it comes to memory consumption and connection
Apache will refuse new connections when traffic reaches the limit of processes
Apache support’s PHP, Python, Perl and other languages using plugins. It is useful when application is based on Python or Ruby
Apache support much wider range of O.S
Apache provides lot more functionality than Nginx
Apache is dependent on hardware components like CPU and memory

6) What is the advantage of using a “reverse proxy server”?
The reverse proxy server can hide the presence and characteristics of the origin server. It acts as an intermediate between internet cloud and web server. It is good for security reason especially when you are using web hosting services.

7) Mention what is the best usage of Nginx server?
The best usage of Nginx server is to deploy dynamic HTTP content on a network with using SCGI, WSGI application servers, FastCGI handlers for scripts.  It can also serve as a load balancer.

8) Mention what is the Master and Worker Processes in Nginx Server?
Master processes: It reads as well as evaluates configuration and maintains worker processes.
Worker processes: It actually does the processing of the requests.

9) Explain how you can start Nginx through a different port other than 80?
To start Nginx through a different port, you have to go to /etc/Nginx/sites-enabled/ and if this is the default file, then you have to open file called “default.” Edit the file and put the port you want Like server { listen 81; }

13) Explain what is C10K problem?
C10K problem is referred for the network socket unable to handle a large number of client (10,000) at the same time.


