-- Conway's Game of Life
import qualified Data.Set as Set

mask :: (Ord t, Num t, Enum t) => (t, t) -> Set.Set (t, t)
mask (x, y) = Set.fromList [(x', y') | x' <- [x-1..x+1], y' <- [y-1..y+1]]

conway :: (Ord t, Num t, Enum t) => Set.Set (t, t) -> (t, t) -> Bool
conway u c = (Set.size $ Set.intersection u $ mask c) `elem` nlives
  where nlives = if c `Set.member` u then [3, 4] else [3]

lut :: (Ord t, Num t, Enum t) => Set.Set (t, t) -> Set.Set (t, t)
lut u = Set.filter (conway u) $ dilate u
  where dilate = Set.fold (Set.union . mask) Set.empty

-- a sample test data
begin :: Set.Set (Int, Int)
begin = Set.fromList [(0, 1), (-1, 0), (0, 0), (1, 0), (1, -1)]

-- see nine lives
main = mapM_ (putStrLn . show . Set.toList) $ take 9 $ iterate lut begin
