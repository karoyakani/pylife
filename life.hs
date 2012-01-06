-- Conway's Game of Life
import Control.Applicative
import qualified Data.Set as Set

mask :: (Ord t, Num t, Enum t) => (t, t) -> Set.Set (t, t)
mask (x,y) = Set.fromList $ liftA2 (,) (nbr x) (nbr y)
  where nbr = flip map [-1..1] . (+)

conway :: (Ord t, Num t, Enum t) => Set.Set (t, t) -> (t, t) -> Bool
conway u c = (Set.size $ Set.intersection u $ mask c) `elem` nlives
  where nlives = if c `Set.member` u then [3, 4] else [3]

dilate :: (Ord t, Num t, Enum t) => Set.Set (t, t) -> Set.Set (t, t)
dilate = Set.fold (Set.union . mask) Set.empty

lut :: (Ord t, Num t, Enum t) => Set.Set (t, t) -> Set.Set (t, t)
lut = liftA2 Set.filter conway dilate

-- a sample test data
begin :: Set.Set (Int, Int)
begin = Set.fromList [(-1, 0), (0, 0), (0, 1), (1, 0), (1, -1)]

-- see nine lives
main = mapM_ (putStrLn . show . Set.toList) $ take 9 $ iterate lut begin
