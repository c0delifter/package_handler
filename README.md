# About
The following is a solution to Thoughtful.AI's code challenge.

Full requirements can be [found here](https://thoughtfulautomation.notion.site/Platform-Technical-Screen-b61b6f6980714c198dc49b91dd23d695)

The crux of the app is a Python script called `package_handler.py`, which invokes the `sort_package()` function.

Therein, we take 4 arguments: `width`, `height`, `length`, and `mass`.

Depending on these values, the function classifies the package into one of three categories.

`STANDARD`
`SPECIAL`
`REJECTED`

The return value of the function is a string.

# Arguments to Pass
The script expects one of two arguments:

`--dimensions` <width> <height> <length> <mass>: The end user specifies the package dimensions and gets the appropriate label in response.

`--tests`: Runs predefined tests.

# How to run

If you have Python installed on your machine - great. Feel free to just run the script.

E.g. `./package_handler.py --dimensions 10 20 30 40`

or

`./package_handler.py --tests`

If not, there's a handy Dockerfile attached. This will allow you to run the script in a stand-alone container.

Step #1 - build the Docker image.

`docker build -t package_handler ./`

Step #2 - spin up a container from the Docker image and pass the desired command-line arguments.

`docker run package_handler --dimensions 10 20 30 40`

or

`docker run package_handler --tests`
