Feeding Nemo
============
I didn't want my fish to die while i was overseas, so i wrote this.
A tiny web site to feed my fish.
```
      /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´}
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸}
     `\\´´\¸.·´
```
Most of this was written on a sunday when i was fairly hung over, so the quality of the code reflects that.

Also if you decide to break my site please don't kill my fish (overfededing will kill them)

## Best Practices

No. Nope. Definitely not here....

## Overview

This all runs on a raspberry pi 3 which sits under my fish tank. 

It uses the motion package to capture images from the web cam and writes the to the root web directory every second. The python code should be configured to run on startup.

The display of the last feeding time is done by reading the last modified time of the robots.txt file.

## Installation

Not recommended or supported...

1. Buy Raspberry Pi
2. Install Raspbian (or other)
3. ?????
4. Profit

##TODO

Make code suck less
