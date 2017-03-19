from jupyter/scipy-notebook:latest

volume /var/notebook

expose 8080
expose 9090

cmd ["jupyter", "notebook", "-y", "--no-browser", "--port=8080", "--notebook-dir=/var/notebook"]

