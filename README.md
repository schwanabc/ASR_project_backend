# ASR_project_backend
## Setting up project

Create and use virtual environment

```sh
python3 -m venv venv

# For windows
venv\Scripts\activate.bat
# For unix
source venv/bin/activate
```

Install dependencies

```sh
pip install -r requirements.txt
```

## Running Server

Start the server

```sh
python main.py
```
## API (every API receives JSON)

### getdata
GET รับ sentence 

return
```json
{
    "command": "nearest string in dict from given input",
    "command_no": "id of command"
}
```

เดี๋ยวเขียนต่อ 
