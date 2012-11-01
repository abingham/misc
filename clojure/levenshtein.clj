(def next-count
  (fn [new-row b-letter a-letter prev-row]
    (let [new-row-size (count new-row)]
      (conj new-row
            (if (= b-letter a-letter)
              (get prev-row
                   (- new-row-size 1))
              (+ 1
                 (min (last new-row)
                      (get prev-row
                           (- new-row-size 1))
                      (get prev-row new-row-size))))))))

(def next-row
  (fn [prev-row letter b]
    (reduce
     (fn [new-row b-letter]
       (next-count new-row b-letter letter prev-row))
     [(+ 1 (first prev-row))]
     b)))

(def levenshtein
  (fn [a b]
    ; reduce: row, letter-in-a -> next row
    (reduce
     (fn [row letter]
       (next-row row letter b))
     (apply vector (range (+ 1 (count b)))) ; first row
     a)))