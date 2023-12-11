import Data.Maybe (fromMaybe)
import Data.List (elemIndex)
import Data.Map

main = do
    let file = "input.txt"
    contents <- readFile file
    let ls = lines contents
    let sPos = findS ls 0
    let loopLength = getLoopLength ls sPos
    print (loopLength `div` 2)

sInLine :: String -> Int
sInLine s = fromMaybe (-1) $ elemIndex 'S' s

findS :: [String] -> Int -> (Int, Int)
findS (x:xs) row
    | sInLine x /= -1 = (row, sInLine x)
    | otherwise = findS xs (row + 1)

getLoopLength' :: [String] -> (Int, Int) -> Int -> Char -> Int
getLoopLength' ls (row, col) res prev
    | ls !! row !! col == 'S' = res
    | ls !! row !! col == '|' = getLoopLength' ls (row + prevLookup, col) (res + 1) prev
    | ls !! row !! col == '-' = getLoopLength' ls (row, col + prevLookup) (res + 1) prev

    | ls !! row !! col == 'L' && prev == 'D' = getLoopLength' ls (row, col + 1) (res + 1) 'R'
    | ls !! row !! col == 'L' && prev == 'L' = getLoopLength' ls (row - 1, col) (res + 1) 'U'

    | ls !! row !! col == 'J' && prev == 'D' = getLoopLength' ls (row, col - 1) (res + 1) 'L'
    | ls !! row !! col == 'J' && prev == 'R' = getLoopLength' ls (row - 1, col) (res + 1) 'U'

    | ls !! row !! col == '7' && prev == 'R' = getLoopLength' ls (row + 1, col) (res + 1) 'D'
    | ls !! row !! col == '7' && prev == 'U' = getLoopLength' ls (row, col - 1) (res + 1) 'L'

    | ls !! row !! col == 'F' && prev == 'L' = getLoopLength' ls (row + 1, col) (res + 1) 'D'
    | ls !! row !! col == 'F' && prev == 'U' = getLoopLength' ls (row, col + 1) (res + 1) 'R'
    | otherwise = 0
    where mapping = fromList [('D', 1), ('U', -1), ('L', -1), ('R', 1)]
          prevLookup = fromMaybe 0 $ Data.Map.lookup prev mapping

isValidPipe :: [String] -> (Int, Int) -> Char -> Bool
isValidPipe ls (row, col) prev
    | ls !! row !! col == '|' && prev == 'U' = True
    | ls !! row !! col == '|' && prev == 'D' = True
    | ls !! row !! col == '-' && prev == 'L' = True
    | ls !! row !! col == '-' && prev == 'R' = True
    | ls !! row !! col == 'L' && prev == 'D' = True
    | ls !! row !! col == 'L' && prev == 'L' = True
    | ls !! row !! col == 'J' && prev == 'D' = True
    | ls !! row !! col == 'J' && prev == 'R' = True
    | ls !! row !! col == '7' && prev == 'R' = True
    | ls !! row !! col == '7' && prev == 'U' = True
    | ls !! row !! col == 'F' && prev == 'L' = True
    | ls !! row !! col == 'F' && prev == 'U' = True
    | otherwise = False

getLoopLength :: [String] -> (Int, Int) -> Int
getLoopLength ls (row, col)
    -- up
    | row - 1 >= 0 && isValidPipe ls (row - 1, col) 'U' = getLoopLength' ls (row - 1, col) 1 'U'
    -- down
    | row + 1 < length ls && isValidPipe ls (row + 1, col) 'D' = getLoopLength' ls (row + 1, col) 1 'D'
    -- left
    | col - 1 >= 0 && isValidPipe ls (row, col - 1) 'L' = getLoopLength' ls (row, col - 1) 1 'L'
    -- right
    | col + 1 < length (ls !! row) && isValidPipe ls (row, col + 1) 'R' = getLoopLength' ls (row, col + 1) 1 'R'
