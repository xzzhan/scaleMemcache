To fix the request rate, I rewrote an request generator, "run_loader.py".

The usage is:

./run_loader.py -n <the number of threads to launch on each client> -t <runtime>

Each thread will generate requests every 2 seconds.

Xin
