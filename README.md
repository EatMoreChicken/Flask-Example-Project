# Flask Example Project and Base

## Description
This repository provides a basic example of a Python Flask project integrated with Bootstrap.

While this repository is a work in progress, you can use it as a simple reference for setting up Flask applications with Bootstrap. More features and improvements will be added over time. The upcoming enhancements are listed in the To-Do section below.

## Notes
- The project uses locally hosted `css` and `js` files from the `static/` directory. You have the option to switch to using CDNs, but the local setup is kept for simplicity.
- An example favicon is included. Refer to the setup process below to add your own favicon.
- By default, `app.debug = True` is set in `app.py`, enabling live reloads for file changes. You can adjust this setting as needed.

## Setup
1. Install Python.
2. Download and extract the project to your desired location.
3. Navigate to the project's root directory using your terminal/command prompt.
4. Install the required packages: `pip install -r requirements.txt`
5. Start the project: `python run.py`
6. Navigate to `http://127.0.0.1:8888/` to view the page (This is the default port.)

## Favicon Setup

For creating icons, you can use Pixlr: https://pixlr.com/x/

To convert a PNG to a favicon pack: https://favicon.io/favicon-converter/

After downloading favicons, extract them into the `static/images` directory and replace the default ones. Ensure the filenames match.

## To-Do
- [x] Update `requirements.txt`
- [ ] Add an example page that demonstrates sending and processing data
- [ ] Implement logging
- [ ] Add an example page with live updates

## Contributing
Contributions are welcome! Please feel free to contribute to this project by creating pull requests, filing bug reports, or providing feedback.