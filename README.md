# Audio Pi

## Installation

`sudo apt-get update && sudo apt-get install libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0 -y`

`pip install -r requirements.txt`

Set up the startup service / daemon:

```
sudo cp audiopi.service /lib/systemd/system/audiopi.service
sudo chmod 644 audiopi.service /lib/systemd/system/audiopi.service
sudo systemctl daemon-reload
sudo systemctl enable audiopi.service
```

