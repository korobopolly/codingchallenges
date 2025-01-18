using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int[] numbers = new int[9];
        for (int i = 0; i < 9; i++) {
            numbers[i] = int.Parse(Console.ReadLine());
        }

        int max = numbers.Max();
        int maxIndex = numbers
            .Select((value,index) => new { Value = value, Index = index })
            .First(x => x.Value == max)
            .Index;
        sb.Append($"{max} {maxIndex+1}");
        Console.WriteLine(sb.ToString());
    }
}
