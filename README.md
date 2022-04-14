# pyon
PYON Reader - Python Object Nation

## Installation
```bash
pip install pyonr
```

## How to use
### let's create our <b>PYON</b> file
i'm going to call it <b>friends.pyon</b>
<br>

```
{
    "me": {
        "name": "Nawaf",
        "age": 15
    }
}
```

### Reading File
```py
import pyonr

file = pyonr.read('friends.pyon') # Replace "friends.pyon" with your file name

fileData = file.readfile # {'me': {'name': 'Nawaf', 'age': 15}}
type(filedata) # <class 'dict'>
```

### Writing File
```py
import pyonr

file = pyonr.read('friends.pyon')
fileData = file.readfile

fileData['khayal'] = {
    "name": "Khayal",
    "age": 14
}
# This will update "fileData" only, we need to save it

file.write(fileData)
```

<p>File will get updated to</p>

```
{
    'me': {
        'name': 'Nawaf',
        'age': 15
        },
        
    'khayal': {
        'name': 'Khayal',
        'age': 14
    }
}
```