<img src="https://github.com/hypar-io/sdk/blob/master/hypar_logo.svg" width="300px" style="display: block;margin-left: auto;margin-right: auto;width: 50%;">

# python-starter
A python starter project for Hypar.

The `dotnet-starter` project is a dotnet core 2.0 library project which references the [Hypar SDK](https://github.com/hypar-io/sdk) and uses the [Hypar CLI](https://github.com/hypar-io/sdk/tree/master/src/cli) to bootstrap your project.

## Prerequisites
- Install [Python 3.6](https://www.python.org/downloads/release/python-360/).

## Getting Started
- Fork this repository.
- Clone your fork of the repository locally.
- Edit the `hypar.json` to describe your function.

## Test
Although not a strict requirement of Hypar, your code should have tests. The python-starter project uses Python's `unittest` module. To run the tests you can do the following:
```
cd test
python -m unittest
```

## Preview
Hypar functions generate geometry in the form of [glTF](https://www.khronos.org/gltf/) models. See the unit tests for a test which generates a `.glb` file that can be used to preview geometry. GlTF models can be previewed using the [online glTF viewer](https://gltf-viewer.donmccurdy.com/).
