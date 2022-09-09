## EclipseProject/camera


<---!
`camera_functions` library completely written in `Bash` 
-->



<---!
### Solar corona photography during total solar eclipse

Total solar eclipse is an astronomical event during which the Sun's photosphere completely covered by the Moon.

for the particular plase on the Earth's surface --- the Moon's shadow.  
-->


### Dependencies
1. `gPhoto2`

### `camera_functions`
Library containing functions for camera control. All functions are described below. 

#### `SETUP`
Setting camera parameters up before totality. TBD

#### `BURST`
Runs continuous shooting in the time interval `T1`--`T2`.  

```
BURST T1 T2 SHUTTER_SPEED
```

#### `AEB`
Runs Auto Exposure Bracketing (AEB) sequences continuously in the time interval `T1`--`T2`. `AEB` accepts 7 mandatory positional parameters:
```
AEB T1 T2 MID_SHUTTER_SPEED STEP N FPS MODE
```

All parameters are described below.

1. `T1`is moment of the beginning of shooting. The format is seconds since 1970-01-01 00:00:00 UTC. Example:
```
T=$(date -d 2022-06-15T18:44:15,100+03:00 +%s.%N)
```

If the actual start of the program later than `T1` then capturing starts immediately. If the actual start of the program later than `T2` then capturing stops immediately.

2. `T2`is moment of the end of shooting. The actual end of shooting might be later than T2 up to BRACKET_DURATION value if `MODE = LTC` (see below).

3. `MID_SHUTTER_SPEED` is shutter speed of the middle shot in bracketed sequence.

4. `STEP` is the difference in exposure values between (i+1)-th and i-th shot in bracketed sequence set by User.	
```   
STEP = log2( SHUTTER_SPEED_(i+1) / SHUTTER_SPEED_(i) )  
```

5. `N ` is number of frames in bracketed sequence. N depends on camera model.
 
6. `FPS` frames per second rate in continious shooting mode. Usually, FPS can be found in Users's manual for camera. Otherwise, FPS should be measured experimentally.

7. `MODE`. Most likely the interval `T2 - T1` do not contain whole number of bracketed sequences. Two different options provided to handle this conflict:

- `LTC`: Let To Complete bracket sequence if remaining time before `T2` is less than `BRACKET_DURATION`. 
- `ROT`: Right On Time. Capture completes if remaining time before `T2` is less than `BRACKET_DURATION`.

`BRACKET_DURATION` equals `ESTIMATED_BRACKET_DURATION` before first bracket. During first bracket and following real `BRACKET_DURATION` value measured.



### `script.sh`




