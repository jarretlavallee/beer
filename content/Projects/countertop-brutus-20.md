---
author: jarret
date: 2011-10-29
slug: countertop-brutus-20
tags:
- Brutus 20
categories:
 - Projects
title: Countertop Brutus 20
---

So this is something that I have been working on for a few months. Ok...
in reality its been over a year. I thought this would be a great idea
back in January 2010 and went out an bought all of the pieces. I ended
up building my kettle and the chiller/pump toolbox and never actually
making the controller. The design is mostly from [jkarp on HBT][]. I
customized this idea for my environment.


**The Controller:**
-------------------

So my girlfriend finally motivated me to start working on this again.
Last weekend I finally started on my controller. The enclosure turned
out horrible. I had a hard time cutting out the square holes in the
plastic. I ended up burning up a dremmel that I got from my old
roommate. I though it would be easier and cleaner to use a cut wheel
than to use the perpendicular cutter. Wow I was wrong. So one dremmel
later and some horrible cuts in the plastic I had all of the holes
drilled and pannel mount holes cut. Everything looks decent except for
holes that I cut out for the heatsinks. They do not fit properly. Well
fuck it, I put them in and let friction hold those bitches in there.


I wish I had some male pannel mount power connectors, but I can\'t find
any good ones. I would love to just have two pannel mount male power
connectors on the unit and then just use 12 guage extension cords. It
would be much cleaner and sexier. I will try to do this in V2.


So the pannel box that I purchased is 6x6x4. I stuffed the following in
the box.

-   2 GFCI outlets
-   1 Pannel mount 3 pin RTD connector
-   3 Toggle Switches
-   1 Auber 2362 PID
-   1 6 port terminal
-   2 40A SSRs with heatsinks mounted on the outside
-   2 12 guage 3 wire cord with bulk connects


It is an extremely tight fit and I am worried about the heat. the
Heatsinks will pull some of the heat out of the box, but I may disable
one of the SSRs to cut down on the heat. We will see whats up after I do
some tests.


Right now it is wired up so that I have 3 toggle switches. The left
switch turns on and off the PID (which is wired to the top cord). The
middle switch allows for the AUX SSR to power up. The right switch
allows for the primary SSR to be powered on. The PID has been setup with
autotune mode (thanks auber) and it also has manual mode. Manual mode
can be enabled by holding the . Otherwise I can set up an SV and the
PID will match the PV to the SV. (Autotune is done by holding "set")


**Kettle:**
-----------


I did this one first because I love the idea of not having to use
propane. By going electric, I can cut my costs down by at least \$3 per
brew depending on the season. Electricity is much cheaper in the winter.
Plus I can run it in my kitchen rather than on my balcony. So my vote
for an electric kettle is AWESOME.


My design was to take my existing 42qt aluminum kettle and modify it to
be all electric. So I drilled some holes in the kettle with my step bit.
In the bottom of my kettle I have 2 2000 watt heating elements held in
with 2 1in SS 304 couplers. In the front I put in a weldless bulkhead
that feeds into a 1/2in ball valve and a hop screen in the kettle. next
to this I have a level guage with a RTD thermometer probe .


This thing works great!. I just need to plug in each of the heating
elements into a separate circuit. Also I have problems with
too rigorous of a boil with both of them turned on, but it heats the
water very quickly. Since I am in the kitchen I can also supplement this
with my range burner and then I am roaring.


I drilled in a hole in the lid and mounted a male QD in there. I need to
add a 1/2 in FIP nipple to the lid and then add in a foot of silicon
tubing. This will serve for recirculating the wort back into the kettle.


**Chiller/pump toolbox:**
-------------------------


I built this one a while back. I do have to admit that this was not my
best design. I decided that I wanted to put the pump and the chiller in
one container. I decided on a toolbox for storage. Unlike most other
brewers, I put the pump completely into the toolbox. I then plumbed it
to have disconnects on the outside of the toolbox. I then stuck the
plate chiller in the box and put disconnects on the outside of the box.
I use a jumper to connect the pump to the plate chiller.


**Mash Tun:**
-------------


So I have 2 mash tuns. One is a 10 Gallon gott and the other is a 5
gallon. The 10 gallon has a false bottom and a thermowell. I use the 10
gallon with out the pump and do manual labor. Its kind of nice to get
some exercise.


The 5 gallon has just been redone. I put in a new SS braid that loops
around into a T. It now has 1/2in plumbing on it. I found that at
McGuckins sells most brass pieces higher in price than SS, so I have
some mixed SS and brass. I built in a male QD in the middle of the lid
of the lid. I still need to cut some silicon from other hoses that I am
using (A few are way too long). I may still put in a thermowell on this
mashtun. We will see how motivated I am.


**Design:**
-----------


So if I put all of the things above together I want to
make something that is easy and something that can control temperature.
I love the idea of only having to change the hoses once and having
consistent temperatures. This allows for low efficiency, but very
consistent results. Plus with the automated temps, I can make set it and
leave it.


  [jkarp on HBT]: http://www.homebrewtalk.com/f51/countertop-brutus-20-a-131411/
    "Credit where it is due"
