using System;
using System.Collections.Generic;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        var set = new HashSet<int> { };
        for (int i = 0; i < 10; i++)
        {
            set.Add(int.Parse(Console.ReadLine()) % 42);
        }

        sb.Append(set.Count);
        Console.WriteLine(sb.ToString());
    }
}
