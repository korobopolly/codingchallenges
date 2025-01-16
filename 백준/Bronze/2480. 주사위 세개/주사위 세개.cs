using System;

class Program
{
    static void Main(string[] args)
    {
        var input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        Array.Sort(input);
        var numbers = new HashSet<int>(input);

        Console.WriteLine(
            numbers.Count == 1
                ? $"{10000 + input[0] * 1000}"
                : numbers.Count == 2
                    ? $"{1000 + input[1] * 100}"
                    : $"{input[^1] * 100}"
        );
    }
}
