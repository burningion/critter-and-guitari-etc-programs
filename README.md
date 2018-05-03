# Critter and Guitari ETC programs

Example Programs in Pygame for the Critter and Guitari ETC

## How to Run This

Copy the `T - 10 PRINT` and the `T - Sine Wave Rainbow` patches on to your ETC's drive. You should see them added to the list of patches.

If you have a WIFI dongle, you can paste the `sine-wave.py` or the `10-print.py` file contents directly into the ETC editor.

## Using the ETC Testing Environment

If you're trying to debug why a ETC program won't run, you can use my included `etc-test.py` program. It takes in the name of  another program, and runs it in a local Pygame environment. This is helpful for quick prototyping, as you're not waiting to see if your program is going to work or not.

Use it like this:

```bash
$ python3 etc-test.py test
```

And it will run the example test program I included, that draws a circle in the center of the screen.

## Example Images

Below are some example images from the programs. The `sine-wave.py` program starts from [this talk](https://www.youtube.com/watch?v=bmztlO9_Wvo) by Zach Lieberman. 

It basically adapts it to some of the parameters on the Critter and Guitari ETC. 

The other program `10-print.py` is adapted from an old program and book by the same name. It picks up from my original Pygame implementation, and adds audio analysis and some control knobs for the parameters again.

![Before Colors](https://github.com/burningion/critter-and-guitari-etc-programs/raw/master/images/10.jpg)
![Before Colors](https://github.com/burningion/critter-and-guitari-etc-programs/raw/master/images/12.jpg)
![Before Colors](https://github.com/burningion/critter-and-guitari-etc-programs/raw/master/images/9.jpg)
![10 Print](https://github.com/burningion/critter-and-guitari-etc-programs/raw/master/images/17.jpg)
![10 Print](https://github.com/burningion/critter-and-guitari-etc-programs/raw/master/images/20.jpg)
![10 Print](https://github.com/burningion/critter-and-guitari-etc-programs/raw/master/images/25.jpg)
