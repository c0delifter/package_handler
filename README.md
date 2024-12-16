# About
The following is a solution to Thoughtful.AI's code challenge.

Full requirements can be [found here](https://thoughtfulautomation.notion.site/Platform-Technical-Screen-b61b6f6980714c198dc49b91dd23d695)

The crux of the app is a Python script called `package_handler.py`

If you have Python installed on your machine - great. Feel free to just run the script.

If not, there's a handy Dockerfile attached. This will allow you to run the script in a stand-alone container.

# How to Run
The script expects one of two arguments:

`--dimensions` <width> <height> <length> <mass>: The end user specifies the package dimensions and gets the appropriate label in response.

`--tests`: Runs predefined tests.
