using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        var list = new List<int>(Enumerable.Range(1, N));
        list.Reverse();
        Console.WriteLine(string.Join("\n", list));
    }
}