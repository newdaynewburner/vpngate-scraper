# vpngate-scraper
Scraper for vpngate.net. Fetches all VPN servers being listed, and generates an OpenVPN configuration file (.ovpn) for
each one. OpenVPN configuration files are saved to `~/Downloads/vpngate-scraper/` by default, and connecting to them can
be accomplished using the `openvpn` command line utility. To do this, open a terminal and run the following command:

`$ sudo openvpn --config "OPENVPN_SERVER_CONFIG.ovpn" --data-ciphers "AES-128-CBC"`

Where, of course, `OPENVPN_SERVER_CONFIG.ovpn` is replaced with the filename of the .ovpn configuration file for the server
you wish to connect to. If you are using Windows, or don't like using the command line, you can connect through the 
OpenVPN Connect client software.

If you experience any errors or other issues, feel free to open an issue on this project's GitHub page. 
