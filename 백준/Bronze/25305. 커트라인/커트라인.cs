using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input[0];
        int k = input[1];
        var line = Console.ReadLine().Split().Select(int.Parse).ToArray();
        var list = new List<int>();
        for (int i = 0; i < N; i++) {
            list.Add(line[i]);
        }
        list.Sort();
        //Console.WriteLine(string.Join(" ",list));
        Console.WriteLine(list[^k]);
    }
}
