
cube :: Int -> Int
cube x = x * x * x

double :: Int -> Int
double x = x * 2

modulus :: Int -> Int -> Int
-- If x > y recurisvely call itself using smaller 
-- valus of x until either x = y or x < y
modulus x y
    | x > y = modulus (x - y) y 
    | x == y = 0
    | otherwise = x

factorial :: Int -> Int
-- This could be rewritten with guards
factorial 0 = 1
factorial n = n * factorial (n - 1)

summation :: Int -> Int
-- If n <= 0 then it stops the recursion otherwise it keeps 
-- recursively calling itself with smaller values of n
summation n 
    | n <= 0 = 0
    | otherwise = n + summation (n - 1)

compose :: (Int -> Int) -> (Int -> Int) -> (Int -> Int)
-- Take the input of function g and use it in function f
-- You can also just do f.g to compose functions
compose f g = \x -> f (g x)

subtractMaker :: Int -> (Int -> Int)
subtractMaker x = \y -> y - x

applyNTimes :: (Int -> Int) -> Int -> Int -> Int
-- If n is zero, return x, otherwise recursively call the function
-- with the new value of x resulting from (f x) and decreased value of n
-- Importantly, only when n is 0 does it return an int.
applyNTimes f x n
    | n == 0 = x
    | otherwise = applyNTimes f (f x) (n - 1)