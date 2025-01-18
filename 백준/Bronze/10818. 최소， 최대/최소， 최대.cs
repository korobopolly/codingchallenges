using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int N = int.Parse(Console.ReadLine());
        int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();

        int max = numbers.Max();
        int min = numbers.Min();
        sb.Append($"{min} {max}");
        Console.WriteLine(sb.ToString());
    }
}
