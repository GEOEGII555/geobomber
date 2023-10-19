<p align="center">
  <img src="https://raw.githubusercontent.com/GEOEGII555/geobomber/dev/logo.png" />
</p>
For Russian people: [Русский](https://github.com/GEOEGII555/geobomber/blob/dev/README.ru.md)

# What is this?
This is an SMS bomber to prank your friends, parents, teachers, and other people.
Please, do NOT use this illegally. Otherwise you might run into trouble, and I won't be liable for that (see disclaimer)

# What are the default modules?
The default modules *usually* have only support for Russian phone numbers (+7).

# What if I want to use other phone numbers, like +1?
Then develop your own modules! Check out modules/example.py.disabled for an example.
Note that each module can support only one service at a time.

# How to install this?
1. Clone this repository
2. Install Python (recommended: 3.10)
Windows 10/11: Get from Microsoft Store
Windows 8.1, 8 and 7: [Download the installer here](https://www.python.org/downloads)
Debian, Ubuntu and their derivatives: `apt install python3`
Arch Linux and derivatives: `pacman --sync python3`

3. Install the requirements: `python3 -m pip install -r requirements.txt`
If you get an error saying that packages are externally managed on Linux, you will need to install them through your package manager.
For example, to install the `distro` module on Ubuntu, run this: `apt install python3-distro`
4. If you're on a Linux distribution or on Termux, install the `dialog` program
Debian, Ubuntu and their derivatives: `apt install dialog`
Arch Linux and derivatives: `pacman --sync dialog`
Termux: `pkg install dialog`
Windows: not required
5. You can run it now: `python3 bomber.py`

# Disclaimer
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
