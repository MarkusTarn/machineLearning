# LAB 6
## Knowledge base in Prolog.

### Description:
Purpose for this lab was to familiarize with Prolog logical programming language.

I declared predicates (deceased(X) and alive(X)) based on the following facts.

> Marcus is man.  
Marcus lives in Pompeii.  
Marcus was born in the year 40.  
All men are mortal.  
All Pompeii occupants died due to volcanic eruption in year 79.
No mortal lives longer than 150 years.  
The current year is 2019.

Is Marcus alive?
What about Francesco?

### Instructions to run:
1. Load in the Knowledge base into Logic Engine
2. Run the queries in the end of file.

### Example:
```
alive(marcus).
alive(francesco).
```

### output:
```
false
true
```