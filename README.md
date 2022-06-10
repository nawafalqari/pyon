# pyon
PYON Reader - Python Object Nation

## Table of Contents
- [Installation](#installation)
- [How to use](#how-to-use)
    - [Creating PYON File](#lets-create-our-bpyonb-file)
    - [Reading File](#reading-file)
    - [Writing File](#writing-file)
- [Built-in functions](#built-in-functions)
    - [PYON Built-in Funtions](#pyon-built-in-functions)
        - [fetch](#fetch)
    - [Python Built-in Funtions](#python-built-in-functions)
        - [Examples](#examples)

## Installation
```bash
pip install pyonr
```

## How to use
### Creating PYON file
let's create our <b>PYON</b> file,
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

<p>File will get updated too</p>

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

## Built-in Functions
### PYON Built-in Functions
### `fetch`:
fetch is used to fetch any file/url content to the file
```python
{
    'data_from_file_pyon': fetch(r'D:\very_secret_data.pyon')
}
```
`fetch` can fetch data from pyon or json files
```py
{
    'data_from_file_json': fetch(r'D:\very_secret_data.json')
}
```
exact same result as above

fetching data from url
```py
fetch('https://example.com/api')
```
note: `fetch` won't change file content, it will only be changed inside a program


### Python Built-in Functions
every `Python` built-in function is supported in `PYON`
#### Examples
```py
{
    "sum_example": sum([i for i in range(10)])
}
```
```py
{
    "sum_with_map_example": sum(
        map(lambda e:e ** 2, [i for i in range(10)])
    )
}
```