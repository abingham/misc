(def second
  (fn [list] (nth list 1)))

(def square
  (fn [x] (* x x)))

(def add-squares
  (fn [& args]
    (apply + (map square args))))

(def factorial
  (fn [n]
    (apply * (range 1 (+ 1 n)))))

(def prefix-of?
  (fn [candidate seq]
    (= candidate (take (count candidate) seq))))

(def tails
  (fn [seq]
    (if (empty? seq) 
      '(()) 
      (cons seq (tails (rest seq))))))