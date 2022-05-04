# Entropy Service

Microservice to generate file entropy reports

## Requirements

The only requirement is Flask library, and flask_cors. Can be installed with [pip](https://pip.pypa.io/en/stable/).

```bash
pip install flask
pip install flask_cors
```
or
```bash
pip3 install flask
pip3 install flask_cors
```

## Run project

To run the project locally, run:
```bash
python app
```
or 
```bash
python3 app
```

It could be necessary to set the Python path to the project directory. 

In Linux or MacOS:
```bash
export PYTHONPATH=$PWD
```

Once running, the web client can be found on http://0.0.0.0:8080/ 

# API Documentation

## Ping
/ping [GET]

### Parameters
None

### Request body
None

### Responses

Code: 200

Description: Pong


Code: 500

Description: There was an error

## Entropy
/API/entropy [POST]

### Parameters
None

### Request body
file (required): File to analyze
blocksize (optional): block size in bytes (Default is 1024)

### Responses

Code: 200

Description:

    - entropyDetail: Entropy for each block
    - summary:
        - low_entropy_blocks: Number of blocks with entropy < 2
        - high_entryopy_blocks: Number of blocks with entropy > 7
        

Example: 
```bash
{
    "entropyDetail" :
        [ 0.19,
        2.44,
        7.89,
        7.95
        ],
    "summary": {
        "low_entropy_blocks": 1,
        "high_entryopy_blocks": 2
    }
}
```


Code: 400

Description: Required file missing


Code: 500

Description: There was an error
