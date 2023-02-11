(clear)
(open $path)

(def f
  (get-frame))
(def rad
  (div f:h (add 2.0 (sqrt 3.0)))))
(def unit 10)

; Flush rows
(def y-row-1
  (sub f:h
    (mul 1.0 rad)))
(def y-row-2
  rad)
(def x-col-1
  rad)
(def x-col-2
  (mul 2.0 rad))
(def x-col-3
  (mul 3.0 rad))
(def x-col-4
  (mul 4.0 rad))
(def x-col-5
  (mul 5.0 rad))
(def x-col-6
  (mul 6.0 rad))
(def x-col-7
  (mul 7.0 rad))
(def x-col-8
  (mul 8.0 rad))

(def color-1
  (pick
    (guide
      (rect x-col-1 y-row-2 unit unit))))
(def color-2
  (pick
    (guide
      (rect x-col-2 y-row-1 unit unit))))
(def color-3
  (pick
    (guide
      (rect x-col-3 y-row-2 unit unit))))
(def color-4
  (pick
    (guide
      (rect x-col-4 y-row-1 unit unit))))
(def color-5
  (pick
    (guide
      (rect x-col-5 y-row-2 unit unit))))
(def color-6
  (pick
    (guide
      (rect x-col-6 y-row-1 unit unit))))
(def color-7
  (pick
    (guide
      (rect x-col-7 y-row-2 unit unit))))
(def color-8
  (pick
    (guide
      (rect x-col-8 y-row-1 unit unit))))

;;; Main Script ;;;

; Uncomment to clear background.
;(clear)

(fill 
  (circle x-col-1 y-row-2 rad) color-1)
(fill 
  (circle x-col-2 y-row-1 rad) color-2)
(fill 
  (circle x-col-3 y-row-2 rad) color-3)
(fill 
  (circle x-col-4 y-row-1 rad) color-4)
(fill 
  (circle x-col-5 y-row-2 rad) color-5)
(fill 
  (circle x-col-6 y-row-1 rad) color-6)
(fill 
  (circle x-col-7 y-row-2 rad) color-7)
(fill 
  (circle x-col-8 y-row-1 rad) color-8)