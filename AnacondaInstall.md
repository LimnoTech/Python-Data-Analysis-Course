# Anaconda Installation Instructions

Even if you have Python installed on your computer, it is intended to be used with ArcGIS and other programs. In order to have a clean installation to use for data analysis and other purposes, we highly recommend downloading the Anaconda Python distribution. This includes Python and most of the libraries and modules that you will likely use. If you already have Anaconda Python installed, or if you know better, then you can skip this. 

It is required that you have a working Python installation before we meet on April 23. If you are bringing a laptop that is not your own, I suggest installing Anaconda on your desktop and use Remote Desktop Connection to connect to the desktop from your borrowed laptop. 

1. Download Anaconda distribution from <https://www.anaconda.com/download/> Use the Python 3.x distribution, unless you have some personal reason to download the Python 2.7 verson. We'll assume you have the Python 3.x version for the course.

2. **IMPORTANT** Progress through the installation until you get to the **Advanced Options** dialog. In the **Advanced Options** dialog, **check the box** for "Add anaconda to the system PATH environment variable". **Uncheck the box** for "Register Anaconda as the system Python". These settings will allow you to invoke Python from the command line by typing "python", but it will not interfere with any other Python installations you have on your computer. These go against the recommended settings for Anaconda, but they work, and they are easy to undo if any problems occur.

3. Test to make sure it works. Open a new command prompt. (Type windows+R and enter "cmd" to open a command prompt). Type "python". A Python prompt should open stating something similar to `Python 3.6 | Anaconda...`. Type `exit()` to exit the prompt. If that works, try typing `jupyter notebook` at the command prompt. It may think a moment, then a large amount of text will show up on the screen and a browser window will open that says "jupyter" on top. Type `control + C` in the command prompt to quit jupyter notebook.  If these two tests work, you should be good to go! If not, please email or contact Steve before April 23.

[Return to course guide](https://github.com/LimnoTech/Python-Data-Analysis-Course)