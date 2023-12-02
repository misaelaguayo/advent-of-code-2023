import GHC.IO.IOMode (IOMode(ReadMode))
import Data.ByteString (hGetContents)
import Control.Exception (handle)
import System.IO (openFile)
import Data.ByteString as BS (putStr)
import Text.Read (readMaybe)
import Data.Char (digitToInt)
import GHC.Unicode (isDigit)

main = do
    let file = "p1input.txt"
    handle <- openFile file ReadMode
    contents <- hGetContents handle
    BS.putStr contents

handleFile :: [String] -> [String]
handleFile contents =
    [ x | x <- contents]

handleLine :: String -> String
handleLine = filter isDigit
