digitalista:: Int -> [Int]
digitalista 0 = []
digitalista x = (mod x 10): lista(div x 10)  

main = print $ lista(151)
