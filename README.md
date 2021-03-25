# onnx-typecast
A simple python script to typecast ONNX model parameters from INT64 to INT32.

## Why?
I wanted to play around with [ONNX.js](https://github.com/microsoft/onnxjs) and soon figured out that it doesn't support onnx models with INT64 parameters. Also, OpenCV doesn't seem to support INT64 parameters.

## What does this script do?
- The script goes through the parameters of each node of the onnx model and blindly converts INT64 parameters to INT32.
- It also converts the constant parameters from INT64 to INT32.
- Finally, creates a new model and saves it.

## What's the catch?
- **The script does not handle overflows and blindly converts all INT64 parameters to INT32.**
- So ops that require `>INT32.max` or `<INT32.min` values may not perform as expected.
- Please feel free to modify the script to account for this.

## Alright. How do I use it?
 - simple.
 - Install requirements: `pip install -r requirements.txt`
 - run: `python convert.py path/to/int64_model.onnx path/to/converted_int32_model.onnx`


## Also Checkout
- https://github.com/microsoft/onnxjs/issues/168#issuecomment-727219050
