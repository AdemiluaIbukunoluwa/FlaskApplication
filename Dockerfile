# Base the image on Python
FROM python

WORKDIR /root/app
COPY requirements.txt .
# Include all the libraries required for the Python code (pip install commands)
RUN pip install --no-cache-dir -r requirements.txt
# Copy the (tested) code to a directory in the container (e.g. /root/app )
COPY . .
# A command to start the server
CMD ["python", "server.py"]