## Overview 
hi there, in this projects I learned about HTTPS SSL 2 main roles, encrypting traffic and what HAproxy SSL termination means, I worked on two tasks of [0x10. HTTPS SSL](https://github.com/saiAl/alx-system_engineering-devops/tree/master/0x10-https_ssl "0x10. HTTPS SSL") project, the first was about Configure my domain zone so that the subdomain `www` points to my load-balancer IP (lb-01), and write a Bash script that will display information about the subdomains see the code [0-world_wide_web](https://github.com/saiAl/alx-system_engineering-devops/blob/master/0x10-https_ssl/0-world_wide_web "0-world_wide_web"), in this task I used`dig` to fetch the information needed and manipulate it with  `awk`, the second task [1-haproxy_ssl_termination](https://github.com/saiAl/alx-system_engineering-devops/blob/master/0x10-https_ssl/1-haproxy_ssl_termination "1-haproxy_ssl_termination") is about creating a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www` and the file containg the configuration of the `HAproxy`. 

------------

- here are the list of resources that helped me solve and meet the requirments of the project tasks:
[What is HTTPS?](https://intranet.alxswe.com/rltoken/XT1BAiBL3Jpq1bn1q6IYXQ "What is HTTPS?")
[What are the 2 main elements that SSL is providing](https://intranet.alxswe.com/rltoken/STj5WkAPACBxOvwB77Ycrw "What are the 2 main elements that SSL is providing")
[HAProxy SSL termination on Ubuntu16.04](https://intranet.alxswe.com/rltoken/asrMHTWJxWQ2x-Sn6snHow "HAProxy SSL termination on Ubuntu16.04")
[SSL termination](https://intranet.alxswe.com/rltoken/CKUICfppIWI6UC0coEMB8g "SSL termination")[Bash function](https://intranet.alxswe.com/rltoken/zPjZ7-eSSQsLFsGA16C1HQ "Bash function")
[Argument in Bash Script](https://linuxsimply.com/bash-scripting-tutorial/functions/script-argument/number-of-args/ "Argument in Bash Script")
[How to Concatenate Strings in Bash: A Guide for Connecting String Variables](https://www.hostinger.com/tutorials/bash-concatenate-strings "How to Concatenate Strings in Bash: A Guide for Connecting String Variables")
[passing parameters to a bash function](https://stackoverflow.com/questions/6212219/passing-parameters-to-a-bash-function "passing parameters to a bash function")
[bash arrays](https://opensource.com/article/18/5/you-dont-know-bash-intro-bash-arrays "bash arrays")
[bash check script arguments](https://www.baeldung.com/linux/bash-check-script-arguments "bash check script arguments")
[installing certbot in your haproxy load balancer server](https://gbeminiyi.hashnode.dev/installing-certbot-in-your-haproxy-load-balancer-server "installing certbot in your haproxy load balancer server")
