
candidateFactors :: Int -> [Int]
candidateFactors x = [2..((ceiling.sqrt.fromIntegral) x)]

isDivisible :: Int -> Int-> Bool
isDivisible x y = (mod x y) == 0

myMap :: (a -> b) -> [a] -> [b]
-- Function that applies a function to a list
myMap f l
    -- Check if l is null, if it is, return an empty list
    -- if l is null, it is the same as if the length is 0
    -- added benefit that this checks if the list is empty
    -- prevents runtime error of head function
    | null l = []
    -- Recursively perpend the head of the list 
    -- f (1) : myMap f [2, 3 , 4 ,5]
    -- f (2) : myMap f [3, 4, 5]
    -- ...
    -- f (5) : myMap f []
    -- f (1) : f (2) : ... f (5) : []
    -- which becomes [f (1), f (2),..., f (5)]
    | otherwise = f (head l) : myMap f (tail l)

myFilter :: (a -> Bool) -> [a] -> [a] 
-- Improved readability of the answer(???)
myFilter f l
    | null l = []
    -- If the boolean function evaluates to true, perpend head l to the list
    -- myFilter even [1,2,3,4,5,6]
    -- 2 : myFilter even [3,4,5,6]
    -- ...
    -- 2 : 4 : 6 : [] 
    | f (head l) = head l : myFilter f (tail l)
    -- If boolean function evaluates to false, move to the next element
    | otherwise = myFilter f (tail l)

myFoldl :: (a -> a -> a) -> [a] -> a -> a
myFoldl f l u
    | null l = u
    | otherwise = myFoldl f  (tail l) (f u (head l))

myFoldr :: (a -> a -> a) -> [a] -> a -> a
myFoldr f l u
    | null l = u
    -- Reverse the list and return the list without the original last item
    | otherwise = myFoldr f (tail (reverse l)) (f u (last l))

myZip :: (a -> b -> c) -> [a] -> [b] -> [c] 
myZip f l m
    | null l = []
    | otherwise = f (head l) (head m) : myZip f (tail l) (tail m)

composeAll :: [a -> a] -> (a -> a)
composeAll fl
    | null fl = id
    | otherwise = head fl . composeAll (tail fl)

isPrime :: Int -> Bool
isPrime x
    | x <= 1 = False
    | x == 2 = True
    | otherwise = all (not . isDivisible x) (candidateFactors x)

sumOfSquares :: Num a => [a] -> a
sumOfSquares l = myFoldl (+) (myMap (\x -> x * x) l) 0

wholeName :: [String] -> [String] -> [String] -> [String]
wholeName fl m l
    | null fl = []
    -- Parse the middle name string using myMap
    -- myMap (\s -> head s : ".")
    -- If ["Middle", "Center", "Name"], given is returns ["M.", "C.", "N."]
    
    -- Combine first name and middle initial using myZip
    -- myZip (\f mi -> f ++ " " ++ mi) fl {Parsed middle name list}
    -- returns ["Foo M.", "Bar C.", "Foo N."]

    -- Combine First name + middle initial with lasdt name using myZip
    -- myZip (\fmi ln -> fmi ++ " " ++ ln) {First name and middle initial list} l
    -- returns ["Foo M. Lastn", "Surname", "Abcd"]

    -- Filter this list using myFilter
    -- myFilter (even . length) {Full name list}
    -- (even . length) is the same as (\s -> even (length s))

    -- Can be written in a more imperative and readable way using the do keyword
    -- wholeName fl m l = do
    --    let middleInitials = myMap (\s -> head s : ".") m
    --    let firstAndMiddle = myZip (\f mi -> f ++ " " ++ mi) fl middleInitials
    --    let fullNames = myZip (\fmi ln -> fmi ++ " " ++ ln) firstAndMiddle l
    --    myFilter (even . length) fullNames

    | otherwise = myFilter (even . length) (myZip (\fmi ln -> fmi ++ " " ++ ln) (myZip (\f mi -> f ++ " " ++ mi) fl (myMap (\s -> head s : ".") m)) l)
