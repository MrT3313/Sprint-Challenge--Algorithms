#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I  --> SEE QUESTIONS FOR NOTES

a) Answer: O(n)


b) Answer: O(n log(n))


c) Answer: O(n)

## Exercise II

Notes:
- N = building height
- >= F  ==> egg BREAKS
- < F   ==> egg SAFE

Complexity: O(log(n))


(1) SELECT_FLOOR = Find Middle Floor (or choose a random integer < len(n))
  (2.a)   If SELECT_FLOOR === F 
            SafeFloor = F - 1
            return SafeFloor
  (2.b)   Else If SELECT_FLOOR < F          IT DOES NOT BREAK       
            (3.a)
              Eliminate anything < SELECT_FLOOR and repeat (1) with the new array ==> n[SELECT_FLOOR: ]

          Else If SELECT_FLOOR > F          IT BREAKS
            (3.b)
              Eliminate anything > SELECT_FLOOR and repeat (1) with the new array ==> n[ :SELECT_FLOOR]

