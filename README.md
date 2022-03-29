# angryexception

An exception handler that tells you that you're stupid.

## Installation

`pip install angryexception`

You will also need to have either libespeak, sapi5, or nsss speech engines installed.

## Usage

```py
from angryexception import install

install()

# Create an exception
raise Exception()
```
