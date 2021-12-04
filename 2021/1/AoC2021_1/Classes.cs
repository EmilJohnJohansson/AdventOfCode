namespace AoC2021_1
{
    internal class PuzzleInputParser
    {
        private const string PuzzleInputPath = "PuzzleInput.txt";
        public int[] PuzzleInput { get; init; }

        internal PuzzleInputParser()
        {
            PuzzleInput = File.ReadAllLines(PuzzleInputPath).Select(int.Parse).ToArray();
        }
    }

    internal class Sweeper
    {
        int[] depths;

        internal Sweeper()
        {
            var puzzleInputParser = new PuzzleInputParser();
            depths = puzzleInputParser.PuzzleInput;
        }

        internal int CountPointIncreases()
        {
            int depthIncreases = 0;
            for (int i = 1; i < depths.Length; i++)
            {
                depthIncreases += IsDepthIncreased(depths[i], depths[i-1]) ? 1 : 0;
            }
            return depthIncreases;
        }

        internal int CountSlidingWindowIncreases()
        {
            int depthIncreases = 0;
            for (int i = 3; i < depths.Length; i++)
            {
                depthIncreases += IsDepthIncreased(depths[i] + depths[i - 1] + depths[i - 2], depths[i - 1] + depths[i - 2] + depths[i - 3]) ? 1 : 0;
            }
            return depthIncreases;
        }

        private bool IsDepthIncreased(int newDepth, int oldDepth)
        {
            return newDepth > oldDepth;
        }
    }
}
