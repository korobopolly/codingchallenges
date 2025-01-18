using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        while (true) { 
            string line = Console.ReadLine();
            if (line == null) break;
            var input = line.Split().Select(int.Parse).ToArray();
            sb.AppendLine(input.Sum().ToString());
        }
        Console.WriteLine(sb.ToString());
    }
}
