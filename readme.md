# Setup environment
1. If you don't have python (Documents: https://docs.python-guide.org/starting/install3/linux/)

  ```
sudo apt-get update && apt-get install python3.6
sudo apt-get -y install python3-pip
  ```

2. Checking python in OS

  ```
python3 --version
pip3 --version
  ```
  
3. Create environment space

  ```
python3 -m venv <env_name>
  ```

4. Activate/Deactivate environment (run)

```
Actiavate:
- Windows: <env_name>\Scripts\activate
- Unix or MacOS: source <env_name>/bin/activate
Deactivate:
- Windows: <env_name>\Scripts\deactivate
- Unix/MacOS: deactivate
```

5. Install python Library in environment
	dpkt is a python module for fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols
	(https://dpkt.readthedocs.io/en/latest/installation.html)

```
pip3 install dpkt
```

# Running Testing
	python3 main.py <pcap_file>
